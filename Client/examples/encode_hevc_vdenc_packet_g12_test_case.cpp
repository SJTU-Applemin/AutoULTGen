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
//! \file     encode_hevc_vdenc_packet_g12_test_case.cpp
//! \brief    implementation file of HevcVdencPktG12TestCase class
//! \a mock derived from encode_hevc_vdenc_packet_g12_test_case and used for ult test
//!

#include "encode_hevc_vdenc_packet_g12_test_case.h"
#include "codechal_debug_ext.h"
#include "media_cmd_task.h"
#include "encode_hevc_vdenc_ult_test_data.h"
#include "codechal_setting_ext.h"
#include "codec_test_environment.h"

namespace encode
{

    void HevcVdencPktG12TestCase::SetUp()
    {


    }

    void HevcVdencPktG12TestCase::TearDown()
    {


    }
    void HevcVdencPktG12TestCase::GetPlatformByName(PLATFORM &platform)
    {


    }
    void HevcVdencPktG12TestCase::PrepareEncodeParams(EncoderParams &encodeParams)
    {


    }


    TEST_F(HevcVdencPktG12TestCase, SetHcpPicStateParams)
    {
        EXPECT_EQ(m_packet->SetHcpPicStateParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddVdencCmd1Cmd)
    {
        EXPECT_EQ(m_packet->AddVdencCmd1CmdTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddVdencCmd2Cmd)
    {
        EXPECT_EQ(m_packet->AddVdencCmd2CmdTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, PatchSliceLevelCommands)
    {
        EXPECT_EQ(m_packet->PatchSliceLevelCommandsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, PatchTileLevelCommands)
    {
        EXPECT_EQ(m_packet->PatchTileLevelCommandsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddOneTileCommands)
    {
        EXPECT_EQ(m_packet->AddOneTileCommandsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddSlicesCommandsInTile)
    {
        EXPECT_EQ(m_packet->AddSlicesCommandsInTileTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, UpdateParameters)
    {
        EXPECT_EQ(m_packet->UpdateParametersTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddPicStateWithNoTile)
    {
        EXPECT_EQ(m_packet->AddPicStateWithNoTileTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddPicStateWithTile)
    {
        EXPECT_EQ(m_packet->AddPicStateWithTileTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddHcpPipeBufAddrCmd)
    {
        EXPECT_EQ(m_packet->AddHcpPipeBufAddrCmdTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddPictureHcpCommands)
    {
        EXPECT_EQ(m_packet->AddPictureHcpCommandsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddVdencWalkerStateCmd)
    {
        EXPECT_EQ(m_packet->AddVdencWalkerStateCmdTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetHcpPipeBufAddrParams)
    {
        EXPECT_EQ(m_packet->SetHcpPipeBufAddrParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddPictureVdencCommands)
    {
        EXPECT_EQ(m_packet->AddPictureVdencCommandsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetVdencPipeBufAddrParams)
    {
        EXPECT_EQ(m_packet->SetVdencPipeBufAddrParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, PatchPictureLevelCommands)
    {
        EXPECT_EQ(m_packet->PatchPictureLevelCommandsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, InsertSeqStreamEnd)
    {
        EXPECT_EQ(m_packet->InsertSeqStreamEndTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, EnsureAllCommandsExecuted)
    {
        EXPECT_EQ(m_packet->EnsureAllCommandsExecutedTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetVdencPipeModeSelectParams)
    {
        EXPECT_EQ(m_packet->SetVdencPipeModeSelectParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetHcpSliceStateCommonParams)
    {
        EXPECT_EQ(m_packet->SetHcpSliceStateCommonParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, Construct3rdLevelBatch)
    {
        EXPECT_EQ(m_packet->Construct3rdLevelBatchTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, CalculateCommandSize)
    {
        EXPECT_EQ(m_packet->CalculateCommandSizeTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, ReadHcpStatus)
    {
        EXPECT_EQ(m_packet->ReadHcpStatusTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetPakPassType)
    {
        EXPECT_EQ(m_packet->SetPakPassTypeTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetHcpSrcSurfaceParams)
    {
        EXPECT_EQ(m_packet->SetHcpSrcSurfaceParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetHcpReconSurfaceParams)
    {
        EXPECT_EQ(m_packet->SetHcpReconSurfaceParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddHcpIndObjBaseAddrCmd)
    {
        EXPECT_EQ(m_packet->AddHcpIndObjBaseAddrCmdTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetHcpIndObjBaseAddrParams)
    {
        EXPECT_EQ(m_packet->SetHcpIndObjBaseAddrParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddHcpQmStateCmd)
    {
        EXPECT_EQ(m_packet->AddHcpQmStateCmdTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetHcpQmStateParams)
    {
        EXPECT_EQ(m_packet->SetHcpQmStateParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetVdencDSSurfaceStateParams)
    {
        EXPECT_EQ(m_packet->SetVdencDSSurfaceStateParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetVdencDsRefSurfaceStateParams)
    {
        EXPECT_EQ(m_packet->SetVdencDsRefSurfaceStateParamsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, VdencPipeModeSelect)
    {
        EXPECT_EQ(m_packet->VdencPipeModeSelectTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetVdencSurfaces)
    {
        EXPECT_EQ(m_packet->SetVdencSurfacesTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddVdencPipeBufAddrCmd)
    {
        EXPECT_EQ(m_packet->AddVdencPipeBufAddrCmdTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, ReadSliceSizeForSinglePipe)
    {
        EXPECT_EQ(m_packet->ReadSliceSizeForSinglePipeTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, ReadSliceSize)
    {
        EXPECT_EQ(m_packet->ReadSliceSizeTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, CopyDataBlock)
    {
        EXPECT_EQ(m_packet->CopyDataBlockTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, WaitHevcDone)
    {
        EXPECT_EQ(m_packet->WaitHevcDoneTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, WaitVdencDone)
    {
        EXPECT_EQ(m_packet->WaitVdencDoneTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, WaitHevcVdencDone)
    {
        EXPECT_EQ(m_packet->WaitHevcVdencDoneTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, ValidateVdboxIdx)
    {
        EXPECT_EQ(m_packet->ValidateVdboxIdxTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetPerfTag)
    {
        EXPECT_EQ(m_packet->SetPerfTagTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetSemaphoreMem)
    {
        EXPECT_EQ(m_packet->SetSemaphoreMemTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SendPrologCmds)
    {
        EXPECT_EQ(m_packet->SendPrologCmdsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AllocateBatchBufferForPakSlices)
    {
        EXPECT_EQ(m_packet->AllocateBatchBufferForPakSlicesTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetBatchBufferForPakSlices)
    {
        EXPECT_EQ(m_packet->SetBatchBufferForPakSlicesTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, ReadSseStatistics)
    {
        EXPECT_EQ(m_packet->ReadSseStatisticsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddForceWakeup)
    {
        EXPECT_EQ(m_packet->AddForceWakeupTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, AddHcpPakInsertNALUs)
    {
        EXPECT_EQ(m_packet->AddHcpPakInsertNALUsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, CalculatePSNR)
    {
        EXPECT_EQ(m_packet->CalculatePSNRTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, SetRowstoreCachingOffsets)
    {
        EXPECT_EQ(m_packet->SetRowstoreCachingOffsetsTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, FreeResources)
    {
        EXPECT_EQ(m_packet->FreeResourcesTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, DumpResources)
    {
        EXPECT_EQ(m_packet->DumpResourcesTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, GetActiveTask)
    {
        EXPECT_EQ(m_packet->GetActiveTaskTest(), MOS_STATUS_SUCCESS);
    }
    TEST_F(HevcVdencPktG12TestCase, StartStatusReport)
    {
        EXPECT_EQ(m_packet->StartStatusReportTest(), MOS_STATUS_SUCCESS);
    }
}
