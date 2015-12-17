// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#import "ios/chrome/browser/passwords/ios_chrome_password_manager_client.h"

#include "base/memory/scoped_ptr.h"
#include "components/autofill/core/common/password_form.h"
#include "components/browser_sync/browser/profile_sync_service.h"
#include "components/keyed_service/core/service_access_type.h"
#include "components/password_manager/core/browser/password_form_manager.h"
#include "components/password_manager/core/browser/password_manager_util.h"
#include "components/password_manager/core/common/password_manager_pref_names.h"
#include "components/signin/core/browser/signin_manager_base.h"
#include "ios/chrome/browser/passwords/ios_chrome_password_store_factory.h"
#include "ios/chrome/browser/signin/signin_manager_factory.h"
#include "ios/chrome/browser/sync/ios_chrome_profile_sync_service_factory.h"
#include "ios/public/provider/chrome/browser/browser_state/chrome_browser_state.h"
#include "url/gurl.h"

using password_manager::PasswordFormManager;
using password_manager::PasswordStore;
using password_manager::PasswordSyncState;

namespace {

const sync_driver::SyncService* GetSyncService(
    ios::ChromeBrowserState* browser_state) {
  return IOSChromeProfileSyncServiceFactory::GetForBrowserStateIfExists(
      browser_state);
}

const SigninManagerBase* GetSigninManager(
    ios::ChromeBrowserState* browser_state) {
  return ios::SigninManagerFactory::GetForBrowserState(browser_state);
}

}  // namespace

IOSChromePasswordManagerClient::IOSChromePasswordManagerClient(
    id<PasswordManagerClientDelegate> delegate)
    : delegate_(delegate),
      credentials_filter_(
          this,
          base::Bind(&GetSyncService, delegate_.browserState),
          base::Bind(&GetSigninManager, delegate_.browserState)) {
  saving_passwords_enabled_.Init(
      password_manager::prefs::kPasswordManagerSavingEnabled, GetPrefs());
}

IOSChromePasswordManagerClient::~IOSChromePasswordManagerClient() = default;

PasswordSyncState IOSChromePasswordManagerClient::GetPasswordSyncState() const {
  ProfileSyncService* sync_service =
      IOSChromeProfileSyncServiceFactory::GetForBrowserState(
          delegate_.browserState);
  return password_manager_util::GetPasswordSyncState(sync_service);
}

bool IOSChromePasswordManagerClient::PromptUserToChooseCredentials(
    ScopedVector<autofill::PasswordForm> local_forms,
    ScopedVector<autofill::PasswordForm> federated_forms,
    const GURL& origin,
    base::Callback<void(const password_manager::CredentialInfo&)> callback) {
  NOTIMPLEMENTED();
  return false;
}

bool IOSChromePasswordManagerClient::PromptUserToSaveOrUpdatePassword(
    scoped_ptr<PasswordFormManager> form_to_save,
    password_manager::CredentialSourceType type,
    bool update_password) {
  if (form_to_save->IsBlacklisted())
    return false;
  [delegate_ showSavePasswordInfoBar:form_to_save.Pass()];
  return true;
}

void IOSChromePasswordManagerClient::AutomaticPasswordSave(
    scoped_ptr<PasswordFormManager> saved_form_manager) {
  NOTIMPLEMENTED();
}

bool IOSChromePasswordManagerClient::IsOffTheRecord() const {
  return (delegate_.browserState)->IsOffTheRecord();
}

PrefService* IOSChromePasswordManagerClient::GetPrefs() {
  return (delegate_.browserState)->GetPrefs();
}

PasswordStore* IOSChromePasswordManagerClient::GetPasswordStore() const {
  return IOSChromePasswordStoreFactory::GetForBrowserState(
             delegate_.browserState, ServiceAccessType::EXPLICIT_ACCESS)
      .get();
}

void IOSChromePasswordManagerClient::NotifyUserAutoSignin(
    ScopedVector<autofill::PasswordForm> local_forms) {}

void IOSChromePasswordManagerClient::ForceSavePassword() {
  NOTIMPLEMENTED();
}

bool IOSChromePasswordManagerClient::IsSavingAndFillingEnabledForCurrentPage()
    const {
  return *saving_passwords_enabled_ && !IsOffTheRecord() &&
         !DidLastPageLoadEncounterSSLErrors() &&
         IsFillingEnabledForCurrentPage();
}

const GURL& IOSChromePasswordManagerClient::GetLastCommittedEntryURL() const {
  return delegate_.lastCommittedURL;
}

const password_manager::CredentialsFilter*
IOSChromePasswordManagerClient::GetStoreResultFilter() const {
  return &credentials_filter_;
}