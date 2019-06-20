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
//! \file     media_scalability_factory_test_case.cpp
//! \brief    implementation file of MediaScalabilityFactoryTestCase class
//! \a mock derived from media_scalability_factory_test_case and used for ult test
//!

#include "media_scalability_factory_test_case.h"

namespace 
{

    void MediaScalabilityFactoryTestCase::SetUp()
    {


    }

    void MediaScalabilityFactoryTestCase::TearDown()
    {


    }
    void MediaScalabilityFactoryTestCase::GetPlatformByName(PLATFORM &platform)
    {


    }
    void MediaScalabilityFactoryTestCase::PrepareEncodeParams(EncoderParams &encodeParams)
    {


    }


    TEST_F(MediaScalabilityFactoryTestCase, CreateScalability)
    {
        EXPECT_EQ(m_packet->CreateScalabilityTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(MediaScalabilityFactoryTestCase, CreateEncodeScalability)
    {
        EXPECT_EQ(m_packet->CreateEncodeScalabilityTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(MediaScalabilityFactoryTestCase, CreateDecodeScalability)
    {
        EXPECT_EQ(m_packet->CreateDecodeScalabilityTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(MediaScalabilityFactoryTestCase, CreateVpScalability)
    {
        EXPECT_EQ(m_packet->CreateVpScalabilityTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(MediaScalabilityFactoryTestCase, CreateScalabilityMdf)
    {
        EXPECT_EQ(m_packet->CreateScalabilityMdfTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(MediaScalabilityFactoryTestCase, CreateScalabilityCmdBuf)
    {
        EXPECT_EQ(m_packet->CreateScalabilityCmdBufTest(), MOS_STATUS_SUCCESS);
    }
}
