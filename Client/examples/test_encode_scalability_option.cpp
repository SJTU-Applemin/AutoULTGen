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
//! \file     test_encode_scalability_option.cpp
//! \brief    implementation file of TestEncodeScalabilityOption class
//! \a mock derived from test_encode_scalability_option and used for ult test
//!


namespace encode 
{
        MOS_STATUS TestEncodeScalabilityOption::SetScalabilityOptionTest()
        {
            ScalabilityPars *params;
            memset(&params, 0, sizeof(params));

            EXPECT_EQ(EncodeScalabilityOption::SetScalabilityOption(params), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilityOption::IsScalabilityOptionMatchedTest()
        {
            ScalabilityPars *params;
            memset(&params, 0, sizeof(params));

            EXPECT_EQ(EncodeScalabilityOption::IsScalabilityOptionMatched(params), true);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilityOption::GetNumPipeTest()
        {
            EXPECT_EQ(EncodeScalabilityOption::GetNumPipe(), 0);

            return MOS_STATUS_SUCCESS;
        }

}
