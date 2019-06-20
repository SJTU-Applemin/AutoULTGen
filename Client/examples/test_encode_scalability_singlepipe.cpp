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
//! \file     test_encode_scalability_singlepipe.cpp
//! \brief    implementation file of TestEncodeScalabilitySinglePipe class
//! \a mock derived from test_encode_scalability_singlepipe and used for ult test
//!

#include "test_encode_scalability_singlepipe.h"

namespace encode
{
        MOS_STATUS TestEncodeScalabilitySinglePipe::InitializeTest()
        {
            MediaScalabilityOption option;
            memset(&option, 0, sizeof(option));

            EXPECT_EQ(EncodeScalabilitySinglePipe::Initialize(option), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::UpdateStateTest()
        {
            void *statePars = nullptr;

            EXPECT_EQ(EncodeScalabilitySinglePipe::UpdateState(statePars), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::VerifyCmdBufferTest()
        {
            uint32_t requestedSize = 0;

            uint32_t requestedPatchListSize = 0;

            bool singleTaskPhaseSupportedInPak = 0;

            EXPECT_EQ(EncodeScalabilitySinglePipe::VerifyCmdBuffer(requestedSize, requestedPatchListSize, singleTaskPhaseSupportedInPak), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::VerifySpaceAvailableTest()
        {
            uint32_t requestedSize = 0;

            uint32_t requestedPatchListSize = 0;

            bool singleTaskPhaseSupportedInPak = 0;

            EXPECT_EQ(EncodeScalabilitySinglePipe::VerifySpaceAvailable(requestedSize, requestedPatchListSize, singleTaskPhaseSupportedInPak), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::ResizeCommandBufferAndPatchListTest()
        {
            uint32_t requestedCommandBufferSize = 0;

            uint32_t requestedPatchListSize = 0;

            EXPECT_EQ(EncodeScalabilitySinglePipe::ResizeCommandBufferAndPatchList(requestedCommandBufferSize, requestedPatchListSize), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::SendAttrWithFrameTrackingTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            bool frameTrackingRequested = 0;

            EXPECT_EQ(EncodeScalabilitySinglePipe::SendAttrWithFrameTracking(cmdBuffer, frameTrackingRequested), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::GetGpuCtxCreationOptionTest()
        {
            MOS_GPUCTX_CREATOPTIONS *gpuCtxCreateOption;
            memset(&gpuCtxCreateOption, 0, sizeof(gpuCtxCreateOption));

            EXPECT_EQ(EncodeScalabilitySinglePipe::GetGpuCtxCreationOption(gpuCtxCreateOption), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::DestroyTest()
        {
            EXPECT_EQ(EncodeScalabilitySinglePipe::Destroy(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::GetCmdBufferTest()
        {
            PMOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(EncodeScalabilitySinglePipe::GetCmdBuffer(cmdBuffer), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::ReturnCmdBufferTest()
        {
            PMOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(EncodeScalabilitySinglePipe::ReturnCmdBuffer(cmdBuffer), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::SubmitCmdBufferTest()
        {
            PMOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(EncodeScalabilitySinglePipe::SubmitCmdBuffer(cmdBuffer), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::SyncPipeTest()
        {
            uint32_t syncType = 0;

            uint32_t semaphoreId = 0;

            PMOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(EncodeScalabilitySinglePipe::SyncPipe(syncType, semaphoreId, cmdBuffer), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::ResetSemaphoreTest()
        {
            uint32_t syncType = 0;

            uint32_t semaphoreId = 0;

            PMOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(EncodeScalabilitySinglePipe::ResetSemaphore(syncType, semaphoreId, cmdBuffer), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::SetHintParamsTest()
        {
            EXPECT_EQ(EncodeScalabilitySinglePipe::SetHintParams(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::PopulateHintParamsTest()
        {
            PMOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(EncodeScalabilitySinglePipe::PopulateHintParams(cmdBuffer), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::IsScalabilityModeMatchedTest()
        {
            ScalabilityPars *params;
            memset(&params, 0, sizeof(params));

            EXPECT_EQ(EncodeScalabilitySinglePipe::IsScalabilityModeMatched(params), true);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::IsGpuCtxCreateOptionMatchedTest()
        {
            PMOS_GPUCTX_CREATOPTIONS_ENHANCED gpuCtxCreateOption1;
            memset(&gpuCtxCreateOption1, 0, sizeof(gpuCtxCreateOption1));

            PMOS_GPUCTX_CREATOPTIONS_ENHANCED gpuCtxCreateOption2;
            memset(&gpuCtxCreateOption2, 0, sizeof(gpuCtxCreateOption2));

            EXPECT_EQ(EncodeScalabilitySinglePipe::IsGpuCtxCreateOptionMatched(gpuCtxCreateOption1, gpuCtxCreateOption2), true);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::GetQueueTest()
        {
            bool newQueue = 0;

            CmQueue *&queue;
            memset(&&queue, 0, sizeof(&queue));

            EXPECT_EQ(EncodeScalabilitySinglePipe::GetQueue(newQueue, &queue), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::GetPipeNumberTest()
        {
            EXPECT_EQ(EncodeScalabilitySinglePipe::GetPipeNumber(), 0);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestEncodeScalabilitySinglePipe::IsFrameTrackingEnabledTest()
        {
            EXPECT_EQ(EncodeScalabilitySinglePipe::IsFrameTrackingEnabled(), true);

            return MOS_STATUS_SUCCESS;
        }

}
