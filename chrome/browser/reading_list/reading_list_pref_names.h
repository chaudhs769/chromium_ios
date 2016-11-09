// Copyright 2016 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Constants for the names of various reading list preferences.

#ifndef IOS_CHROME_BROWSER_READING_LIST_READING_LIST_PREF_NAMES_H_
#define IOS_CHROME_BROWSER_READING_LIST_READING_LIST_PREF_NAMES_H_

namespace reading_list {
namespace prefs {

// Boolean to track if some reading list entries have never been seen on this
// device. Not synced.
extern const char kReadingListHasUnseenEntries[];

}  // namespace prefs
}  // namespace reading_list

#endif  // IOS_CHROME_BROWSER_READING_LIST_READING_LIST_PREF_NAMES_H_