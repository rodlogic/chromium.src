# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'target_defaults': {
    'variables': {
      'chromium_code': 1,
    },
    'include_dirs': [
      '../../../..',
    ],
  },
  'targets' : [
    {
      'target_name': 'virtual_driver_setup',
      'type': 'executable',
      'dependencies': [
        '../../../../base/base.gyp:base',
        'virtual_driver_setup_resources',
      ],
      'sources': [
        'setup.cc',
        '../virtual_driver_consts.h',
        '../virtual_driver_consts.cc',
        '../virtual_driver_helpers.h',
        '../virtual_driver_helpers.cc',
        '../virtual_driver_common_resources.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_ar.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_bg.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_bn.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_ca.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_cs.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_da.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_de.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_el.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_en.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_en-GB.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_es.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_es-419.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_et.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_fa.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_fi.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_fil.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_fr.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_gu.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_he.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_hi.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_hr.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_hu.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_id.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_it.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_ja.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_kn.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_ko.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_lt.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_lv.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_ml.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_mr.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_ms.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_nb.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_nl.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_pl.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_pt-BR.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_pt-PT.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_ro.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_ru.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_sk.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_sl.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_sr.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_sv.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_ta.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_te.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_th.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_tr.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_uk.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_vi.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_zh-CN.rc',
        '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources/virtual_driver_setup_resources_zh-TW.rc',
      ],
      'msvs_settings': {
        'VCLinkerTool': {
          'SubSystem': '2',         # Set /SUBSYSTEM:WINDOWS
          'AdditionalDependencies': [
            'setupapi.lib',
          ],
          'DelayLoadDLLs': [
            'winspool.drv',
          ],
        },
      },
    },
    {
      'target_name': 'virtual_driver_setup_resources',
      'type': 'none',
      'variables': {
        'grit_out_dir': '<(SHARED_INTERMEDIATE_DIR)/virtual_driver_setup_resources',
      },
      'actions': [
        {
          'action_name': 'virtual_driver_setup_resources',
          'variables': {
            'grit_grd_file': 'virtual_driver_setup_resources.grd',
          },
          'includes': [ '../../../../build/grit_action.gypi' ],
        },
      ],
      'includes': [ '../../../../build/grit_target.gypi' ],
    },
  ],
}
