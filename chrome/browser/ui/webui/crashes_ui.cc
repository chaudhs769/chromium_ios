// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "ios/chrome/browser/ui/webui/crashes_ui.h"

#include "base/bind.h"
#include "base/bind_helpers.h"
#include "base/memory/ref_counted_memory.h"
#include "base/strings/utf_string_conversions.h"
#include "base/values.h"
#include "components/crash/core/browser/crashes_ui_util.h"
#include "components/version_info/version_info.h"
#include "grit/components_chromium_strings.h"
#include "grit/components_google_chrome_strings.h"
#include "grit/components_resources.h"
#include "grit/components_scaled_resources.h"
#include "grit/components_strings.h"
#include "ios/chrome/browser/chrome_url_constants.h"
#include "ios/chrome/browser/crash_report/crash_upload_list.h"
#include "ios/chrome/browser/metrics/ios_chrome_metrics_service_accessor.h"
#include "ios/chrome/grit/ios_chromium_strings.h"
#include "ios/public/provider/chrome/browser/browser_state/chrome_browser_state.h"
#include "ios/public/provider/web/web_ui_ios.h"
#include "ios/public/provider/web/web_ui_ios_message_handler.h"
#include "ios/web/public/web_ui_ios_data_source.h"
#include "ui/base/resource/resource_bundle.h"

namespace {

web::WebUIIOSDataSource* CreateCrashesUIHTMLSource() {
  web::WebUIIOSDataSource* source =
      web::WebUIIOSDataSource::Create(kChromeUICrashesHost);

  for (size_t i = 0; i < crash::kCrashesUILocalizedStringsCount; ++i) {
    source->AddLocalizedString(
        crash::kCrashesUILocalizedStrings[i].name,
        crash::kCrashesUILocalizedStrings[i].resource_id);
  }

  source->AddLocalizedString(crash::kCrashesUIShortProductName,
                             IDS_IOS_SHORT_PRODUCT_NAME);

  source->SetJsonPath("strings.js");
  source->AddResourcePath(crash::kCrashesUICrashesJS, IDR_CRASH_CRASHES_JS);
  source->SetDefaultResource(IDR_CRASH_CRASHES_HTML);
  return source;
}

////////////////////////////////////////////////////////////////////////////////
//
// CrashesDOMHandler
//
////////////////////////////////////////////////////////////////////////////////

// The handler for Javascript messages for the chrome://crashes/ page.
class CrashesDOMHandler : public web::WebUIIOSMessageHandler,
                          public CrashUploadList::Delegate {
 public:
  CrashesDOMHandler();
  ~CrashesDOMHandler() override;

  // WebUIMessageHandler implementation.
  void RegisterMessages() override;

  // CrashUploadList::Delegate implemenation.
  void OnUploadListAvailable() override;

 private:
  // Asynchronously fetches the list of crashes. Called from JS.
  void HandleRequestCrashes(const base::ListValue* args);

  // Sends the recent crashes list JS.
  void UpdateUI();

  scoped_refptr<CrashUploadList> upload_list_;
  bool list_available_;
  bool first_load_;

  DISALLOW_COPY_AND_ASSIGN(CrashesDOMHandler);
};

CrashesDOMHandler::CrashesDOMHandler()
    : list_available_(false), first_load_(true) {
  upload_list_ = ios::CreateCrashUploadList(this);
}

CrashesDOMHandler::~CrashesDOMHandler() {
  upload_list_->ClearDelegate();
}

void CrashesDOMHandler::RegisterMessages() {
  upload_list_->LoadUploadListAsynchronously();
  web_ui()->RegisterMessageCallback(
      crash::kCrashesUIRequestCrashList,
      base::Bind(&CrashesDOMHandler::HandleRequestCrashes,
                 base::Unretained(this)));
}

void CrashesDOMHandler::HandleRequestCrashes(const base::ListValue* args) {
  if (first_load_) {
    first_load_ = false;
    if (list_available_)
      UpdateUI();
  } else {
    list_available_ = false;
    upload_list_->LoadUploadListAsynchronously();
  }
}

void CrashesDOMHandler::OnUploadListAvailable() {
  list_available_ = true;
  if (!first_load_)
    UpdateUI();
}

void CrashesDOMHandler::UpdateUI() {
  bool crash_reporting_enabled =
      IOSChromeMetricsServiceAccessor::IsMetricsAndCrashReportingEnabled();
  base::ListValue crash_list;
  if (crash_reporting_enabled)
    crash::UploadListToValue(upload_list_.get(), &crash_list);
  base::FundamentalValue enabled(crash_reporting_enabled);
  base::FundamentalValue dynamic_backend(false);
  base::StringValue version(version_info::GetVersionNumber());

  web_ui()->CallJavascriptFunction(crash::kCrashesUIUpdateCrashList, enabled,
                                   dynamic_backend, crash_list, version);
}

}  // namespace

///////////////////////////////////////////////////////////////////////////////
//
// CrashesUI
//
///////////////////////////////////////////////////////////////////////////////

CrashesUI::CrashesUI(web::WebUIIOS* web_ui) : web::WebUIIOSController(web_ui) {
  web_ui->AddMessageHandler(new CrashesDOMHandler());

  // Set up the chrome://crashes/ source.
  web::WebUIIOSDataSource::Add(ios::ChromeBrowserState::FromWebUIIOS(web_ui),
                               CreateCrashesUIHTMLSource());
}

// static
base::RefCountedMemory* CrashesUI::GetFaviconResourceBytes(
    ui::ScaleFactor scale_factor) {
  return ResourceBundle::GetSharedInstance().LoadDataResourceBytesForScale(
      IDR_CRASH_SAD_FAVICON, scale_factor);
}
