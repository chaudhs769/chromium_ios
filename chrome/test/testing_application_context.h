// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef IOS_CHROME_TEST_TESTING_APPLICATION_CONTEXT_H_
#define IOS_CHROME_TEST_TESTING_APPLICATION_CONTEXT_H_

#include "base/macros.h"
#include "base/memory/scoped_ptr.h"
#include "base/threading/thread_checker.h"
#include "ios/chrome/browser/application_context.h"

class TestingApplicationContext : public ApplicationContext {
 public:
  TestingApplicationContext();
  ~TestingApplicationContext() override;

  // Convenience method to get the current application context as a
  // TestingApplicationContext.
  static TestingApplicationContext* GetGlobal();

  // Sets the local state.
  void SetLocalState(PrefService* local_state);

  // Sets the last shutdown "clean" state.
  void SetLastShutdownClean(bool clean);

  // Sets the ChromeBrowserStateManager.
  void SetChromeBrowserStateManager(ios::ChromeBrowserStateManager* manager);

  // ApplicationContext implementation.
  void OnAppEnterForeground() override;
  void OnAppEnterBackground() override;
  bool WasLastShutdownClean() override;
  PrefService* GetLocalState() override;
  net::URLRequestContextGetter* GetSystemURLRequestContext() override;
  const std::string& GetApplicationLocale() override;
  ios::ChromeBrowserStateManager* GetChromeBrowserStateManager() override;
  metrics::MetricsService* GetMetricsService() override;
  variations::VariationsService* GetVariationsService() override;
  rappor::RapporService* GetRapporService() override;
  net_log::ChromeNetLog* GetNetLog() override;
  network_time::NetworkTimeTracker* GetNetworkTimeTracker() override;
  IOSChromeIOThread* GetIOSChromeIOThread() override;
  gcm::GCMDriver* GetGCMDriver() override;

 private:
  base::ThreadChecker thread_checker_;
  std::string application_locale_;
  PrefService* local_state_;
  ios::ChromeBrowserStateManager* chrome_browser_state_manager_;
  scoped_ptr<network_time::NetworkTimeTracker> network_time_tracker_;
  bool was_last_shutdown_clean_;

  DISALLOW_COPY_AND_ASSIGN(TestingApplicationContext);
};

#endif  // IOS_CHROME_TEST_TESTING_APPLICATION_CONTEXT_H_
