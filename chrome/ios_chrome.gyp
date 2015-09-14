# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'chromium_code': 1,
  },
  'targets': [
    {
      'target_name': 'ios_chrome_app',
      'type': 'static_library',
      'include_dirs': [
        '../..',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        'ios_chrome_browser',
      ],
      'link_settings': {
        'libraries': [
          '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
          '$(SDKROOT)/System/Library/Frameworks/UIKit.framework',
        ],
      },
      'sources': [
        'app/UIApplication+ExitsOnSuspend.h',
        'app/UIApplication+ExitsOnSuspend.mm',
        'app/deferred_initialization_runner.h',
        'app/deferred_initialization_runner.mm',
        'app/safe_mode_crashing_modules_config.h',
        'app/safe_mode_crashing_modules_config.mm',
        'app/safe_mode_util.cc',
        'app/safe_mode_util.h',
      ],
    },
    {
      'target_name': 'ios_chrome_browser',
      'type': 'static_library',
      'include_dirs': [
        '../..',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../base/base.gyp:base_prefs',
        '../../breakpad/breakpad.gyp:breakpad_client',
        '../../components/components.gyp:autofill_core_browser',
        '../../components/components.gyp:autofill_core_common',
        '../../components/components.gyp:autofill_ios_browser',
        '../../components/components.gyp:bookmarks_browser',
        '../../components/components.gyp:bookmarks_managed',
        '../../components/components.gyp:component_updater',
        '../../components/components.gyp:content_settings_core_browser',
        '../../components/components.gyp:crash_keys',
        '../../components/components.gyp:data_reduction_proxy_core_common',
        '../../components/components.gyp:dom_distiller_core',
        '../../components/components.gyp:dom_distiller_ios',
        '../../components/components.gyp:enhanced_bookmarks',
        '../../components/components.gyp:favicon_core',
        '../../components/components.gyp:gcm_driver',
        '../../components/components.gyp:google_core_browser',
        '../../components/components.gyp:history_core_browser',
        '../../components/components.gyp:history_ios_browser',
        '../../components/components.gyp:infobars_core',
        '../../components/components.gyp:invalidation_impl',
        '../../components/components.gyp:invalidation_public',
        '../../components/components.gyp:keyed_service_core',
        '../../components/components.gyp:keyed_service_ios',
        '../../components/components.gyp:leveldb_proto',
        '../../components/components.gyp:metrics',
        '../../components/components.gyp:network_time',
        '../../components/components.gyp:omnibox_browser',
        '../../components/components.gyp:open_from_clipboard',
        '../../components/components.gyp:password_manager_core_browser',
        '../../components/components.gyp:password_manager_sync_browser',
        '../../components/components.gyp:pref_registry',
        '../../components/components.gyp:proxy_config',
        '../../components/components.gyp:rappor',
        '../../components/components.gyp:search',
        '../../components/components.gyp:search_engines',
        '../../components/components.gyp:signin_core_browser',
        '../../components/components.gyp:signin_core_common',
        '../../components/components.gyp:signin_ios_browser',
        '../../components/components.gyp:suggestions',
        '../../components/components.gyp:sync_driver',
        '../../components/components.gyp:translate_core_browser',
        '../../components/components.gyp:translate_ios_browser',
        '../../components/components.gyp:undo_component',
        '../../components/components.gyp:update_client',
        '../../components/components.gyp:upload_list',
        '../../components/components.gyp:variations',
        '../../components/components.gyp:version_info',
        '../../components/components.gyp:web_resource',
        '../../components/components.gyp:webdata_services',
        '../../components/components.gyp:webp_transcode',
        '../../components/components_strings.gyp:components_strings',
        '../../google_apis/google_apis.gyp:google_apis',
        '../../net/net.gyp:net',
        '../../skia/skia.gyp:skia',
        '../../sync/sync.gyp:sync',
        '../../third_party/google_toolbox_for_mac/google_toolbox_for_mac.gyp:google_toolbox_for_mac',
        '../../ui/base/ui_base.gyp:ui_base',
        '../../ui/gfx/gfx.gyp:gfx',
        '../../url/url.gyp:url_lib',
        '../provider/ios_provider_chrome.gyp:ios_provider_chrome_browser',
        '../web/ios_web.gyp:ios_web',
        'injected_js',
        'ios_chrome_common',
        'ios_chrome_resources.gyp:ios_chrome_resources',
      ],
      'link_settings': {
        'libraries': [
          '$(SDKROOT)/System/Library/Frameworks/Accelerate.framework',
          '$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
          '$(SDKROOT)/System/Library/Frameworks/CoreLocation.framework',
          '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
          '$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework',
          '$(SDKROOT)/System/Library/Frameworks/UIKit.framework',
        ],
      },
      'sources': [
        'browser/app_startup_parameters.h',
        'browser/app_startup_parameters.mm',
        'browser/application_context.cc',
        'browser/application_context.h',
        'browser/application_context_impl.cc',
        'browser/application_context_impl.h',
        'browser/arch_util.cc',
        'browser/arch_util.h',
        'browser/autocomplete/autocomplete_classifier_factory.cc',
        'browser/autocomplete/autocomplete_classifier_factory.h',
        'browser/autocomplete/autocomplete_provider_client_impl.cc',
        'browser/autocomplete/autocomplete_provider_client_impl.h',
        'browser/autocomplete/autocomplete_scheme_classifier_impl.h',
        'browser/autocomplete/autocomplete_scheme_classifier_impl.mm',
        'browser/autocomplete/in_memory_url_index_factory.cc',
        'browser/autocomplete/in_memory_url_index_factory.h',
        'browser/autocomplete/shortcuts_backend_factory.cc',
        'browser/autocomplete/shortcuts_backend_factory.h',
        'browser/autofill/autofill_agent_utils.h',
        'browser/autofill/autofill_agent_utils.mm',
        'browser/autofill/form_input_accessory_view.h',
        'browser/autofill/form_input_accessory_view.mm',
        'browser/autofill/form_input_accessory_view_controller.h',
        'browser/autofill/form_input_accessory_view_controller.mm',
        'browser/autofill/form_input_accessory_view_delegate.h',
        'browser/autofill/form_suggestion_controller.h',
        'browser/autofill/form_suggestion_controller.mm',
        'browser/autofill/form_suggestion_label.h',
        'browser/autofill/form_suggestion_label.mm',
        'browser/autofill/form_suggestion_provider.h',
        'browser/autofill/form_suggestion_view.h',
        'browser/autofill/form_suggestion_view.mm',
        'browser/autofill/form_suggestion_view_client.h',
        'browser/autofill/personal_data_manager_factory.cc',
        'browser/autofill/personal_data_manager_factory.h',
        'browser/bookmarks/bookmark_client_factory.cc',
        'browser/bookmarks/bookmark_client_factory.h',
        'browser/bookmarks/bookmark_client_impl.cc',
        'browser/bookmarks/bookmark_client_impl.h',
        'browser/bookmarks/bookmark_model_factory.cc',
        'browser/bookmarks/bookmark_model_factory.h',
        'browser/bookmarks/startup_task_runner_service_factory.cc',
        'browser/bookmarks/startup_task_runner_service_factory.h',
        'browser/browser_state/browser_state_keyed_service_factories.h',
        'browser/browser_state/browser_state_keyed_service_factories.mm',
        'browser/browser_state/browser_state_otr_helper.cc',
        'browser/browser_state/browser_state_otr_helper.h',
        'browser/browsing_data_change_listening.h',
        'browser/chrome_paths.h',
        'browser/chrome_paths.mm',
        'browser/chrome_switches.cc',
        'browser/chrome_switches.h',
        'browser/chrome_url_constants.cc',
        'browser/chrome_url_constants.h',
        'browser/chrome_url_util.h',
        'browser/chrome_url_util.mm',
        'browser/component_updater/ios_component_updater_configurator.cc',
        'browser/component_updater/ios_component_updater_configurator.h',
        'browser/content_settings/cookie_settings_factory.cc',
        'browser/content_settings/cookie_settings_factory.h',
        'browser/content_settings/host_content_settings_map_factory.cc',
        'browser/content_settings/host_content_settings_map_factory.h',
        'browser/crash_loop_detection_util.h',
        'browser/crash_loop_detection_util.mm',
        'browser/crash_report/breakpad_helper.h',
        'browser/crash_report/breakpad_helper.mm',
        'browser/crash_report/crash_keys.cc',
        'browser/crash_report/crash_keys.h',
        'browser/crash_report/crash_report_background_uploader.h',
        'browser/crash_report/crash_report_background_uploader.mm',
        'browser/crash_report/crash_report_multi_parameter.h',
        'browser/crash_report/crash_report_multi_parameter.mm',
        'browser/crash_report/crash_report_user_application_state.h',
        'browser/crash_report/crash_report_user_application_state.mm',
        'browser/crash_report/crash_upload_list.cc',
        'browser/crash_report/crash_upload_list.h',
        'browser/dom_distiller/distiller_viewer.cc',
        'browser/dom_distiller/distiller_viewer.h',
        'browser/dom_distiller/dom_distiller_service_factory.cc',
        'browser/dom_distiller/dom_distiller_service_factory.h',
        'browser/enhanced_bookmarks/bookmark_server_cluster_service_factory.cc',
        'browser/enhanced_bookmarks/bookmark_server_cluster_service_factory.h',
        'browser/enhanced_bookmarks/enhanced_bookmark_model_factory.cc',
        'browser/enhanced_bookmarks/enhanced_bookmark_model_factory.h',
        'browser/experimental_flags.h',
        'browser/experimental_flags.mm',
        'browser/favicon/favicon_client_impl.cc',
        'browser/favicon/favicon_client_impl.h',
        'browser/favicon/favicon_service_factory.cc',
        'browser/favicon/favicon_service_factory.h',
        'browser/file_metadata_util.h',
        'browser/file_metadata_util.mm',
        'browser/find_in_page/find_in_page_controller.h',
        'browser/find_in_page/find_in_page_controller.mm',
        'browser/find_in_page/find_in_page_model.h',
        'browser/find_in_page/find_in_page_model.mm',
        'browser/find_in_page/js_findinpage_manager.h',
        'browser/find_in_page/js_findinpage_manager.mm',
        'browser/first_run/first_run.h',
        'browser/first_run/first_run.mm',
        'browser/first_run/first_run_configuration.h',
        'browser/first_run/first_run_configuration.mm',
        'browser/first_run/first_run_metrics.h',
        'browser/geolocation/CLLocation+OmniboxGeolocation.h',
        'browser/geolocation/CLLocation+OmniboxGeolocation.mm',
        'browser/geolocation/CLLocation+XGeoHeader.h',
        'browser/geolocation/CLLocation+XGeoHeader.mm',
        'browser/geolocation/location_manager.h',
        'browser/geolocation/location_manager.mm',
        'browser/geolocation/omnibox_geolocation_authorization_alert.h',
        'browser/geolocation/omnibox_geolocation_authorization_alert.mm',
        'browser/geolocation/omnibox_geolocation_config.h',
        'browser/geolocation/omnibox_geolocation_config.mm',
        'browser/geolocation/omnibox_geolocation_local_state.h',
        'browser/geolocation/omnibox_geolocation_local_state.mm',
        'browser/google/google_brand.h',
        'browser/google/google_brand.mm',
        'browser/google/google_url_tracker_client_impl.cc',
        'browser/google/google_url_tracker_client_impl.h',
        'browser/google/google_url_tracker_factory.cc',
        'browser/google/google_url_tracker_factory.h',
        'browser/history/history_backend_client_impl.cc',
        'browser/history/history_backend_client_impl.h',
        'browser/history/history_client_impl.cc',
        'browser/history/history_client_impl.h',
        'browser/history/history_service_factory.cc',
        'browser/history/history_service_factory.h',
        'browser/history/history_utils.cc',
        'browser/history/history_utils.h',
        'browser/history/top_sites_factory.cc',
        'browser/history/top_sites_factory.h',
        'browser/history/web_history_service_factory.cc',
        'browser/history/web_history_service_factory.h',
        'browser/infobars/confirm_infobar_controller.h',
        'browser/infobars/confirm_infobar_controller.mm',
        'browser/infobars/infobar.h',
        'browser/infobars/infobar.mm',
        'browser/infobars/infobar_container_ios.h',
        'browser/infobars/infobar_container_ios.mm',
        'browser/infobars/infobar_container_view.h',
        'browser/infobars/infobar_container_view.mm',
        'browser/infobars/infobar_controller.h',
        'browser/infobars/infobar_controller.mm',
        'browser/infobars/infobar_manager_impl.cc',
        'browser/infobars/infobar_manager_impl.h',
        'browser/infobars/infobar_utils.h',
        'browser/infobars/infobar_utils.mm',
        'browser/install_time_util.h',
        'browser/install_time_util.mm',
        'browser/installation_notifier.h',
        'browser/installation_notifier.mm',
        'browser/memory/memory_debugger.h',
        'browser/memory/memory_debugger.mm',
        'browser/memory/memory_debugger_manager.h',
        'browser/memory/memory_debugger_manager.mm',
        'browser/memory/memory_metrics.cc',
        'browser/memory/memory_metrics.h',
        'browser/metrics/field_trial_synchronizer.cc',
        'browser/metrics/field_trial_synchronizer.h',
        'browser/metrics/ios_stability_metrics_provider.h',
        'browser/metrics/ios_stability_metrics_provider.mm',
        'browser/metrics/previous_session_info.h',
        'browser/metrics/previous_session_info.mm',
        'browser/net/chrome_cookie_store_ios_client.h',
        'browser/net/chrome_cookie_store_ios_client.mm',
        'browser/net/connection_type_observer_bridge.h',
        'browser/net/connection_type_observer_bridge.mm',
        'browser/net/cookie_util.h',
        'browser/net/cookie_util.mm',
        'browser/net/http_server_properties_manager_factory.cc',
        'browser/net/http_server_properties_manager_factory.h',
        'browser/net/image_fetcher.h',
        'browser/net/image_fetcher.mm',
        'browser/net/ios_chrome_http_user_agent_settings.cc',
        'browser/net/ios_chrome_http_user_agent_settings.h',
        'browser/net/ios_chrome_network_delegate.cc',
        'browser/net/ios_chrome_network_delegate.h',
        'browser/net/metrics_network_client.h',
        'browser/net/metrics_network_client.mm',
        'browser/net/metrics_network_client_manager.h',
        'browser/net/metrics_network_client_manager.mm',
        'browser/net/proxy_service_factory.cc',
        'browser/net/proxy_service_factory.h',
        'browser/net/retryable_url_fetcher.h',
        'browser/net/retryable_url_fetcher.mm',
        'browser/open_from_clipboard/create_clipboard_recent_content.h',
        'browser/open_from_clipboard/create_clipboard_recent_content.mm',
        'browser/passwords/password_generation_utils.h',
        'browser/passwords/password_generation_utils.mm',
        'browser/pref_names.cc',
        'browser/pref_names.h',
        'browser/prefs/browser_prefs.cc',
        'browser/prefs/browser_prefs.h',
        'browser/prefs/pref_observer_bridge.h',
        'browser/prefs/pref_observer_bridge.mm',
        'browser/procedural_block_types.h',
        'browser/search/search_util.cc',
        'browser/search/search_util.h',
        'browser/search_engines/search_engines_util.cc',
        'browser/search_engines/search_engines_util.h',
        'browser/search_engines/template_url_service_client_impl.cc',
        'browser/search_engines/template_url_service_client_impl.h',
        'browser/search_engines/template_url_service_factory.cc',
        'browser/search_engines/template_url_service_factory.h',
        'browser/search_engines/ui_thread_search_terms_data.cc',
        'browser/search_engines/ui_thread_search_terms_data.h',
        'browser/signin/about_signin_internals_factory.cc',
        'browser/signin/about_signin_internals_factory.h',
        'browser/signin/account_consistency_service_factory.h',
        'browser/signin/account_consistency_service_factory.mm',
        'browser/signin/account_fetcher_service_factory.cc',
        'browser/signin/account_fetcher_service_factory.h',
        'browser/signin/account_reconcilor_factory.cc',
        'browser/signin/account_reconcilor_factory.h',
        'browser/signin/account_tracker_service_factory.cc',
        'browser/signin/account_tracker_service_factory.h',
        'browser/signin/chrome_identity_service_observer_bridge.h',
        'browser/signin/chrome_identity_service_observer_bridge.mm',
        'browser/signin/constants.h',
        'browser/signin/constants.mm',
        'browser/signin/gaia_auth_fetcher_ios.h',
        'browser/signin/gaia_auth_fetcher_ios.mm',
        'browser/signin/gaia_auth_fetcher_ios_private.h',
        'browser/signin/gaia_cookie_manager_service_factory.cc',
        'browser/signin/gaia_cookie_manager_service_factory.h',
        'browser/signin/oauth2_token_service_factory.cc',
        'browser/signin/oauth2_token_service_factory.h',
        'browser/signin/signin_client_factory.cc',
        'browser/signin/signin_client_factory.h',
        'browser/signin/signin_client_impl.cc',
        'browser/signin/signin_client_impl.h',
        'browser/signin/signin_error_controller_factory.cc',
        'browser/signin/signin_error_controller_factory.h',
        'browser/signin/signin_manager_factory.cc',
        'browser/signin/signin_manager_factory.h',
        'browser/signin/signin_manager_factory_observer.h',
        'browser/signin/signin_util.h',
        'browser/signin/signin_util.mm',
        'browser/snapshots/snapshot_cache.h',
        'browser/snapshots/snapshot_cache.mm',
        'browser/snapshots/snapshot_manager.h',
        'browser/snapshots/snapshot_manager.mm',
        'browser/snapshots/snapshot_overlay.h',
        'browser/snapshots/snapshot_overlay.mm',
        'browser/snapshots/snapshots_util.h',
        'browser/snapshots/snapshots_util.mm',
        'browser/suggestions/image_fetcher_impl.h',
        'browser/suggestions/image_fetcher_impl.mm',
        'browser/suggestions/suggestions_service_factory.h',
        'browser/suggestions/suggestions_service_factory.mm',
        'browser/sync/glue/sync_start_util.cc',
        'browser/sync/glue/sync_start_util.h',
        'browser/sync/sync_observer_bridge.h',
        'browser/sync/sync_observer_bridge.mm',
        'browser/sync/sync_setup_service.cc',
        'browser/sync/sync_setup_service.h',
        'browser/sync/sync_setup_service_factory.cc',
        'browser/sync/sync_setup_service_factory.h',
        'browser/translate/after_translate_infobar_controller.h',
        'browser/translate/after_translate_infobar_controller.mm',
        'browser/translate/before_translate_infobar_controller.h',
        'browser/translate/before_translate_infobar_controller.mm',
        'browser/translate/chrome_ios_translate_client.h',
        'browser/translate/chrome_ios_translate_client.mm',
        'browser/translate/never_translate_infobar_controller.h',
        'browser/translate/never_translate_infobar_controller.mm',
        'browser/translate/translate_accept_languages_factory.cc',
        'browser/translate/translate_accept_languages_factory.h',
        'browser/translate/translate_infobar_tags.h',
        'browser/translate/translate_message_infobar_controller.h',
        'browser/translate/translate_message_infobar_controller.mm',
        'browser/translate/translate_service_ios.cc',
        'browser/translate/translate_service_ios.h',
        'browser/ui/UIView+SizeClassSupport.h',
        'browser/ui/UIView+SizeClassSupport.mm',
        'browser/ui/animation_util.h',
        'browser/ui/animation_util.mm',
        'browser/ui/autofill/autofill_client_ios.h',
        'browser/ui/autofill/autofill_client_ios.mm',
        'browser/ui/background_generator.h',
        'browser/ui/background_generator.mm',
        'browser/ui/commands/UIKit+ChromeExecuteCommand.h',
        'browser/ui/commands/UIKit+ChromeExecuteCommand.mm',
        'browser/ui/commands/clear_browsing_data_command.h',
        'browser/ui/commands/clear_browsing_data_command.mm',
        'browser/ui/commands/generic_chrome_command.h',
        'browser/ui/commands/generic_chrome_command.mm',
        'browser/ui/commands/ios_command_ids.h',
        'browser/ui/commands/open_url_command.h',
        'browser/ui/commands/open_url_command.mm',
        'browser/ui/commands/set_up_for_testing_command.h',
        'browser/ui/commands/set_up_for_testing_command.mm',
        'browser/ui/commands/show_mail_composer_command.h',
        'browser/ui/commands/show_mail_composer_command.mm',
        'browser/ui/commands/show_signin_command.h',
        'browser/ui/commands/show_signin_command.mm',
        'browser/ui/file_locations.h',
        'browser/ui/file_locations.mm',
        'browser/ui/image_util.h',
        'browser/ui/image_util.mm',
        'browser/ui/keyboard/UIKeyCommand+Chrome.h',
        'browser/ui/keyboard/UIKeyCommand+Chrome.mm',
        'browser/ui/keyboard/hardware_keyboard_watcher.h',
        'browser/ui/keyboard/hardware_keyboard_watcher.mm',
        'browser/ui/legacy_size_class_support_util.h',
        'browser/ui/legacy_size_class_support_util.mm',
        'browser/ui/native_content_controller.h',
        'browser/ui/native_content_controller.mm',
        'browser/ui/omnibox/web_omnibox_edit_controller.cc',
        'browser/ui/omnibox/web_omnibox_edit_controller.h',
        'browser/ui/orientation_limiting_navigation_controller.h',
        'browser/ui/orientation_limiting_navigation_controller.mm',
        'browser/ui/reversed_animation.h',
        'browser/ui/reversed_animation.mm',
        'browser/ui/rtl_geometry.h',
        'browser/ui/rtl_geometry.mm',
        'browser/ui/show_mail_composer_util.h',
        'browser/ui/show_mail_composer_util.mm',
        'browser/ui/show_privacy_settings_util.h',
        'browser/ui/show_privacy_settings_util.mm',
        'browser/ui/side_swipe_gesture_recognizer.h',
        'browser/ui/side_swipe_gesture_recognizer.mm',
        'browser/ui/size_class_support_util.h',
        'browser/ui/size_class_support_util.mm',
        'browser/ui/ui_util.h',
        'browser/ui/ui_util.mm',
        'browser/ui/uikit_ui_util.h',
        'browser/ui/uikit_ui_util.mm',
        'browser/ui/url_loader.h',
        'browser/undo/bookmark_undo_service_factory.cc',
        'browser/undo/bookmark_undo_service_factory.h',
        'browser/updatable_config/updatable_array.h',
        'browser/updatable_config/updatable_array.mm',
        'browser/updatable_config/updatable_config_base.h',
        'browser/updatable_config/updatable_config_base.mm',
        'browser/updatable_config/updatable_dictionary.h',
        'browser/updatable_config/updatable_dictionary.mm',
        'browser/web/dom_altering_lock.h',
        'browser/web/dom_altering_lock.mm',
        'browser/web/web_view_type_util.h',
        'browser/web/web_view_type_util.mm',
        'browser/web_data_service_factory.cc',
        'browser/web_data_service_factory.h',
        'browser/web_resource/web_resource_util.cc',
        'browser/web_resource/web_resource_util.h',
        'browser/xcallback_parameters.h',
        'browser/xcallback_parameters.mm',
      ],
      'conditions': [
        ['enable_rlz==1', {
          'dependencies': [
            '../../components/components.gyp:rlz',
            'ios_chrome_browser_rlz',
          ],
        }],
        ['configuration_policy==1', {
          'dependencies': [
            '../../components/components.gyp:policy_component_browser',
            '../../components/components.gyp:policy_component_common',
          ],
        }],
      ],
    },
    {
      'target_name': 'ios_chrome_common',
      'type': 'static_library',
      'include_dirs': [
        '../..',
      ],
      'dependencies': [
        'app_group_mainapp',
        '../../base/base.gyp:base',
        '../../components/components.gyp:version_info',
      ],
      'link_settings': {
        'libraries': [
          '$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
          '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
        ],
      },
      'sources': [
        'common/channel_info.h',
        'common/channel_info.mm',
        'common/string_util.h',
        'common/string_util.mm',
      ]
    },
    {
      'target_name': 'injected_js',
      'type': 'none',
      'sources': [
        'browser/find_in_page/resources/find_in_page.js',
      ],
      'includes': [
        '../../ios/web/js_compile.gypi',
      ],
      'link_settings': {
        'mac_bundle_resources': [
          '<(SHARED_INTERMEDIATE_DIR)/find_in_page.js',
        ],
      },
    },
    {
      'target_name': 'app_group_common',
      'type': 'static_library',
      'sources': [
        'common/app_group/app_group_constants.h',
        'common/app_group/app_group_constants.mm',
        'common/app_group/app_group_metrics.h',
        'common/app_group/app_group_metrics.mm',
      ],
      'dependencies': [
        # This target will be included into application extensions and the list
        # of its dependencies must be kept as short as possible.
        '../../base/base.gyp:base',
        '../../components/components.gyp:version_info',
      ],
      'include_dirs': [
        '../..',
      ],
    },
    {
      'target_name': 'app_group_client',
      'type': 'static_library',
      'sources': [
        'common/app_group/app_group_metrics_client.h',
        'common/app_group/app_group_metrics_client.mm',
      ],
      'dependencies': [
        # This target will be included into application extensions and the list
        # of its dependencies must be kept as short as possible.
        'app_group_common',
      ],
      'include_dirs': [
        '../..',
      ],
    },
    {
      'target_name': 'app_group_mainapp',
      'type': 'static_library',
      'sources': [
        'common/app_group/app_group_metrics_mainapp.h',
        'common/app_group/app_group_metrics_mainapp.mm',
      ],
      'dependencies': [
        'app_group_common',
      ],
      'include_dirs': [
        '../..',
      ],
    },
  ],
  'conditions': [
    ['enable_rlz_support==1', {
      'targets': [
        {
          'target_name': 'ios_chrome_browser_rlz',
          'type': 'static_library',
          'sources': [
            'browser/rlz/rlz_tracker_delegate_impl.cc',
            'browser/rlz/rlz_tracker_delegate_impl.h',
          ],
          'dependencies': [
            '../../components/components.gyp:google_core_browser',
            '../../components/components.gyp:omnibox_browser',
            '../../components/components.gyp:rlz',
            '../../components/components.gyp:search_engines',
            '../../rlz/rlz.gyp:rlz_lib',
          ],
        },
      ],
    }],
  ],
}
