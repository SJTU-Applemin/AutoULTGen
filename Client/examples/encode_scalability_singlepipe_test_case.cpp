/*===================== begin_copyright_notice ==================================

INTEL CONFIDENTIAL
Copyright 2018
Intel Corporation All Rights Reserved.

The source code contained or described herein and all documents related to the
source code ("Material") are owned by Intel Corporation or its suppliers or
licensors. Title to the Material remains with Intel Corporation or its suppliers
and licensors. The Material contains trade secrets and proprietary and confidential
information of Intel or its suppliers and licensors. The Material is protected by
worldwide copyright and trade secret laws and treaty provisions. No part of the
Material may be used, copied, reproduced, modified, published, uploaded, posted,
transmitted, distributed, or disclosed in any way without Intel's prior express
written permission.

No license under any patent, copyright, trade secret or other intellectual
property right is granted to or conferred upon you by disclosure or delivery
of the Materials, either expressly, by implication, inducement, estoppel
or otherwise. Any license under such intellectual property rights must be
express and approved by Intel in writing.

======================= end_copyright_notice ==================================*/

//!
//! \file     encode_scalability_singlepipe_test_case.cpp
//! \brief    implementation file of EncodeScalabilitySinglePipeTestCase class
//! \a mock derived from encode_scalability_singlepipe_test_case and used for ult test
//!

#include "encode_scalability_singlepipe_test_case.h"

namespace encode
{

    void EncodeScalabilitySinglePipeTestCase::SetUp()
    {


    }

    void EncodeScalabilitySinglePipeTestCase::TearDown()
    {


    }
    void EncodeScalabilitySinglePipeTestCase::GetPlatformByName(PLATFORM &platform)
    {


    }
    void EncodeScalabilitySinglePipeTestCase::PrepareEncodeParams(EncoderParams &encodeParams)
    {


    }


    TEST_F(EncodeScalabilitySinglePipeTestCase, SetHintParams)
    {
        EXPECT_EQ(m_packet->SetHintParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(EncodeScalabilitySinglePipeTestCase, PopulateHintParams)
    {
        EXPECT_EQ(m_packet->PopulateHintParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(EncodeScalabilitySinglePipeTestCase, IsScalabilityModeMatched)
    {
        EXPECT_EQ(m_packet->IsScalabilityModeMatchedTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(EncodeScalabilitySinglePipeTestCase, IsGpuCtxCreateOptionMatched)
    {
        EXPECT_EQ(m_packet->IsGpuCtxCreateOptionMatchedTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(EncodeScalabilitySinglePipeTestCase, GetPipeNumber)
    {
        EXPECT_EQ(m_packet->GetPipeNumberTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(EncodeScalabilitySinglePipeTestCase, IsFrameTrackingEnabled)
    {
        EXPECT_EQ(m_packet->IsFrameTrackingEnabledTest(), MOS_STATUS_SUCCESS);
    }
}
