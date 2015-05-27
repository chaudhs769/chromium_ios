// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#import "ios/web/shell/app_delegate.h"

#import "base/mac/scoped_nsobject.h"
#include "base/memory/scoped_ptr.h"
#include "ios/web/public/app/web_main.h"
#include "ios/web/public/web_client.h"
#include "ios/web/public/web_state/web_state.h"
#include "ios/web/shell/shell_browser_state.h"
#include "ios/web/shell/shell_main_delegate.h"
#include "ios/web/shell/shell_web_client.h"
#import "ios/web/shell/view_controller.h"

@interface AppDelegate () {
  scoped_ptr<web::ShellMainDelegate> _delegate;
  scoped_ptr<web::WebMain> _webMain;
}
@end

@implementation AppDelegate

@synthesize window = _window;

- (BOOL)application:(UIApplication*)application
    didFinishLaunchingWithOptions:(NSDictionary*)launchOptions {
  _window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
  self.window.backgroundColor = [UIColor whiteColor];

  _delegate.reset(new web::ShellMainDelegate());
  web::WebMainParams params(_delegate.get());
  _webMain.reset(new web::WebMain(params));

  web::ShellWebClient* client =
      static_cast<web::ShellWebClient*>(web::GetWebClient());
  web::BrowserState* browserState = client->browser_state();

  base::scoped_nsobject<ViewController> controller(
      [[ViewController alloc] initWithBrowserState:browserState]);
  self.window.rootViewController = controller;
  [self.window makeKeyAndVisible];
  return YES;
}

- (void)applicationWillResignActive:(UIApplication*)application {
}

- (void)applicationDidEnterBackground:(UIApplication*)application {
}

- (void)applicationWillEnterForeground:(UIApplication*)application {
}

- (void)applicationDidBecomeActive:(UIApplication*)application {
}

- (void)applicationWillTerminate:(UIApplication*)application {
  _webMain.reset();
  _delegate.reset();
}

@end
