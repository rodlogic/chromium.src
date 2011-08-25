# Copyright (c) 2011 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'test_support_content',
      'type': 'static_library',
      'dependencies': [
        'content_common',
        '../skia/skia.gyp:skia',
        '../testing/gmock.gyp:gmock',
        '../testing/gtest.gyp:gtest',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        # TODO(phajdan.jr): All of those files should live in content/test.
        'browser/geolocation/arbitrator_dependency_factories_for_test.cc',
        'browser/geolocation/arbitrator_dependency_factories_for_test.h',
        'browser/geolocation/fake_access_token_store.cc',
        'browser/geolocation/fake_access_token_store.h',
        'browser/geolocation/mock_location_provider.cc',
        'browser/geolocation/mock_location_provider.h',
        'browser/mock_content_browser_client.cc',
        'browser/mock_resource_context.cc',
        'browser/mock_resource_context.h',
        'browser/renderer_host/media/mock_media_observer.cc',
        'browser/renderer_host/media/mock_media_observer.h',
        'common/test_url_constants.cc',
        'common/test_url_constants.h',
        'renderer/mock_content_renderer_client.cc',
        'test/content_test_suite.cc',
        'test/content_test_suite.h',
        'test/test_browser_context.cc',
        'test/test_browser_context.h',
        'test/test_content_client.cc',
        'test/test_content_client.h',
        'test/test_url_fetcher_factory.cc',
        'test/test_url_fetcher_factory.h',

        # TODO(phajdan.jr): Those files should be moved to webkit
        # test support target.
        '../webkit/appcache/appcache_test_helper.cc',
        '../webkit/appcache/appcache_test_helper.h',
        '../webkit/quota/mock_special_storage_policy.cc',
        '../webkit/quota/mock_special_storage_policy.h',
      ],
    },
    {
      'target_name': 'content_unittests',
      'type': 'executable',
      'dependencies': [
        'content_browser',
        'content_gpu',
        'content_plugin',
        'content_renderer',
        'test_support_content',
        '../base/base.gyp:test_support_base',
        '../crypto/crypto.gyp:crypto',
        '../gpu/gpu.gyp:gpu_unittest_utils',
        '../ipc/ipc.gyp:test_support_ipc',
        '../media/media.gyp:media_test_support',
        '../net/net.gyp:net_test_support',
        '../skia/skia.gyp:skia',
        '../testing/gmock.gyp:gmock',
        '../testing/gtest.gyp:gtest',
        '../third_party/libjingle/libjingle.gyp:libjingle',
        '../ui/gfx/gl/gl.gyp:gl',
        '../ui/ui.gyp:ui',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'browser/appcache/chrome_appcache_service_unittest.cc',
        'browser/browser_thread_unittest.cc',
        'browser/browser_url_handler_unittest.cc',
        'browser/child_process_security_policy_unittest.cc',
        'browser/device_orientation/provider_unittest.cc',
        'browser/download/base_file_unittest.cc',
        'browser/download/download_status_updater_unittest.cc',
        'browser/geolocation/gateway_data_provider_common_unittest.cc',
        'browser/gpu/gpu_blacklist_unittest.cc',
        'browser/renderer_host/gtk_key_bindings_handler_unittest.cc',
        'browser/renderer_host/media/audio_input_device_manager_unittest.cc',
        'browser/renderer_host/media/audio_renderer_host_unittest.cc',
        'browser/renderer_host/media/media_stream_dispatcher_host_unittest.cc',
        'browser/renderer_host/media/video_capture_host_unittest.cc',
        'browser/renderer_host/media/video_capture_manager_unittest.cc',
        'browser/renderer_host/resource_dispatcher_host_unittest.cc',
        'browser/renderer_host/resource_queue_unittest.cc',
        'browser/resolve_proxy_msg_helper_unittest.cc',
        'browser/speech/endpointer/endpointer_unittest.cc',
        'browser/speech/speech_recognition_request_unittest.cc',
        'browser/speech/speech_recognizer_unittest.cc',
        'browser/ssl/ssl_host_state_unittest.cc',
        'browser/trace_subscriber_stdio_unittest.cc',
        'common/gpu/gpu_feature_flags_unittest.cc',
        'common/gpu/gpu_info_unittest.cc',
        'common/notification_service_unittest.cc',
        'common/process_watcher_unittest.cc',
        'common/property_bag_unittest.cc',
        'common/resource_dispatcher_unittest.cc',
        'common/url_fetcher_unittest.cc',
        'gpu/gpu_info_collector_unittest.cc',
        'renderer/active_notification_tracker_unittest.cc',
        'renderer/media/audio_message_filter_unittest.cc',
        'renderer/media/audio_renderer_impl_unittest.cc',
        'renderer/media/capture_video_decoder_unittest.cc',
        'renderer/media/media_stream_dispatcher_unittest.cc',
        'renderer/media/rtc_video_decoder_unittest.cc',
        'renderer/media/video_capture_impl_unittest.cc',
        'renderer/media/video_capture_message_filter_unittest.cc',
        'renderer/paint_aggregator_unittest.cc',
        'test/run_all_unittests.cc',
      ],
      'conditions': [
        ['os_posix!=1', {
          'sources!': [
            # TODO(port): port those unit tests.
            'common/process_watcher_unittest.cc',
          ],
        }],
        ['OS=="win" and win_use_allocator_shim==1', {
          'dependencies': [
            '../base/allocator/allocator.gyp:allocator',
          ],
        }],
        ['chromeos==1', {
          'sources/': [
            ['exclude', '^browser/renderer_host/gtk_key_bindings_handler_unittest.cc'],
            # TODO(jam): remove this
            ['exclude', '^browser/renderer_host/resource_dispatcher_host_unittest.cc'],
          ],
        }],
      ],
    },
  ],
}
