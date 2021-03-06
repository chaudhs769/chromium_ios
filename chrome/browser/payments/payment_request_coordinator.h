// Copyright 2016 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef IOS_CHROME_BROWSER_PAYMENTS_PAYMENT_REQUEST_COORDINATOR_H_
#define IOS_CHROME_BROWSER_PAYMENTS_PAYMENT_REQUEST_COORDINATOR_H_

#import <UIKit/UIKit.h>

#import "ios/chrome/browser/chrome_coordinator.h"
#import "ios/chrome/browser/payments/payment_items_display_coordinator.h"
#import "ios/chrome/browser/payments/payment_method_selection_coordinator.h"
#include "ios/chrome/browser/payments/payment_request.h"
#import "ios/chrome/browser/payments/payment_request_view_controller.h"
#import "ios/chrome/browser/payments/shipping_address_selection_coordinator.h"
#import "ios/chrome/browser/payments/shipping_option_selection_coordinator.h"

@class PaymentRequestCoordinator;

// Delegate protocol for PaymentRequestCoordinator.
@protocol PaymentRequestCoordinatorDelegate<NSObject>

// Notifies the delegate that the user has canceled the payment request.
- (void)paymentRequestCoordinatorDidCancel:
    (PaymentRequestCoordinator*)coordinator;

// Notifies the delegate that the user has confirmed the payment request.
- (void)paymentRequestCoordinator:(PaymentRequestCoordinator*)coordinator
    didConfirmWithPaymentResponse:(web::PaymentResponse)paymentResponse;

// Notifies the delegate that the user has selected a shipping address.
- (void)paymentRequestCoordinator:(PaymentRequestCoordinator*)coordinator
         didSelectShippingAddress:(web::PaymentAddress)shippingAddress;

// Notifies the delegate that the user has selected a shipping option.
- (void)paymentRequestCoordinator:(PaymentRequestCoordinator*)coordinator
          didSelectShippingOption:(web::PaymentShippingOption)shippingOption;

@end

// Coordinator responsible for creating and presenting the PaymentRequest view
// controller. The PR view controller will be presented by the view controller
// provided in the initializer.
@interface PaymentRequestCoordinator
    : ChromeCoordinator<PaymentRequestViewControllerDelegate,
                        PaymentItemsDisplayCoordinatorDelegate,
                        PaymentMethodSelectionCoordinatorDelegate,
                        ShippingAddressSelectionCoordinatorDelegate,
                        ShippingOptionSelectionCoordinatorDelegate>

// Creates a Payment Request coordinator that will present UI on
// |viewController| using data available from |personalDataManager|.
- (instancetype)initWithBaseViewController:(UIViewController*)viewController
    NS_DESIGNATED_INITIALIZER;

// The PaymentRequest object owning an instance of web::PaymentRequest as
// provided by the page invoking the Payment Request API. This pointer is not
// owned by this class and should outlive it.
@property(nonatomic, assign) PaymentRequest* paymentRequest;

// The favicon of the page invoking the PaymentRequest API. Should be set before
// calling |start|.
@property(nonatomic, retain) UIImage* pageFavicon;

// The title of the page invoking the Payment Request API. Should be set before
// calling |start|.
@property(nonatomic, copy) NSString* pageTitle;

// The host of the page invoking the Payment Request API. Should be set before
// calling |start|.
@property(nonatomic, copy) NSString* pageHost;

// The delegate to be notified when the user confirms or cancels the request.
@property(nonatomic, weak) id<PaymentRequestCoordinatorDelegate> delegate;

// Updates the payment details of the PaymentRequest and updates the UI.
- (void)updatePaymentDetails:(web::PaymentDetails)paymentDetails;

@end

#endif  // IOS_CHROME_BROWSER_PAYMENTS_PAYMENT_REQUEST_COORDINATOR_H_
