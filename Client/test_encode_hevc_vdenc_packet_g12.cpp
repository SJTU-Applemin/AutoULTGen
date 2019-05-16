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
//! \file     test_encode_hevc_vdenc_packet_g12.cpp
//! \brief    implementation file of TestHevcVdencPktG12 class
//! \a mock derived from test_encode_hevc_vdenc_packet_g12 and used for ult test
//!

#include "test_encode_hevc_vdenc_packet_g12.h"
#include "gtest/gtest.h"
#include "mhw_utilities.h"

namespace encode
{
        MOS_STATUS TestHevcVdencPktG12::SubmitTest()
        {
            MOS_COMMAND_BUFFER *commandBuffer;
            memset(&commandBuffer, 0, sizeof(commandBuffer));

            EXPECT_EQ(HevcVdencPktG12::Submit(commandBuffer), MOS_STATUS_NULL_POINTER);

            // !tileEnabled
//            tileEnabled = 0;
            EXPECT_EQ(HevcVdencPktG12::Submit(commandBuffer), MOS_STATUS_NULL_POINTER);

//            tileEnabled = 1;
            EXPECT_EQ(HevcVdencPktG12::Submit(commandBuffer), MOS_STATUS_NULL_POINTER);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetHcpPicStateParamsTest()
        {
            MHW_VDBOX_HEVC_PIC_STATE picStateParams;
            memset(&picStateParams, 0, sizeof(picStateParams));


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddVdencCmd1CmdTest()
        {
            PMOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            bool addToBatchBufferHuCBRC = 0;

            bool isLowDelayB = 0;

            EXPECT_EQ(HevcVdencPktG12::AddVdencCmd1Cmd(cmdBuffer, addToBatchBufferHuCBRC, isLowDelayB), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddVdencCmd2CmdTest()
        {
            PMOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            bool addToBatchBufferHuCBRC = 0;

            bool isLowDelayB = 0;

            EXPECT_EQ(HevcVdencPktG12::AddVdencCmd2Cmd(cmdBuffer, addToBatchBufferHuCBRC, isLowDelayB), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::CalculatePictureStateCommandSizeTest()
        {
            EXPECT_EQ(HevcVdencPktG12::CalculatePictureStateCommandSize(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::PatchSliceLevelCommandsTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            uint8_t packetPhase = 0;

            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

            // m_hevcPicParams->tiles_enabled_flag
//            m_hevcPicParams->tiles_enabled_flag = 0;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_hevcPicParams->tiles_enabled_flag = 1;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);


            // m_pipeline->IsFirstPass()
//            m_pipeline->IsFirstPass() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFirstPass() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);


            // feature->IsACQPEnabled() || feature->IsBRCEnabled()
//            feature->IsACQPEnabled() = false ;
//            feature->IsBRCEnabled() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            feature->IsACQPEnabled() = true ;
//            feature->IsBRCEnabled() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            feature->IsACQPEnabled() = false ;
//            feature->IsBRCEnabled() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            feature->IsACQPEnabled() = true ;
//            feature->IsBRCEnabled() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);


            // m_useBatchBufferForPakSlices
//            m_useBatchBufferForPakSlices = 0;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_useBatchBufferForPakSlices = 1;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);


            // m_basicFeature->m_lastPicInSeq || m_basicFeature->m_lastPicInStream
//            m_basicFeature->m_lastPicInSeq = 0;
//            m_basicFeature->m_lastPicInStream = 0;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_basicFeature->m_lastPicInSeq = 1;
//            m_basicFeature->m_lastPicInStream = 0;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_basicFeature->m_lastPicInSeq = 0;
//            m_basicFeature->m_lastPicInStream = 1;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_basicFeature->m_lastPicInSeq = 1;
//            m_basicFeature->m_lastPicInStream = 1;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);


            // m_pipeline->IsLastPass() && m_pipeline->IsFirstPipe()
//            m_pipeline->IsLastPass() = false ;
//            m_pipeline->IsFirstPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsLastPass() = true ;
//            m_pipeline->IsFirstPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsLastPass() = false ;
//            m_pipeline->IsFirstPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsLastPass() = true ;
//            m_pipeline->IsFirstPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);


            // false == m_pipeline->IsFrameTrackingEnabled() && m_pipeline->IsLastPass() && m_pipeline->IsLastPipe()
//            m_pipeline->IsFrameTrackingEnabled() = false ;
//            m_pipeline->IsLastPass() = false ;
//            m_pipeline->IsLastPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFrameTrackingEnabled() = true ;
//            m_pipeline->IsLastPass() = false ;
//            m_pipeline->IsLastPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFrameTrackingEnabled() = false ;
//            m_pipeline->IsLastPass() = true ;
//            m_pipeline->IsLastPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFrameTrackingEnabled() = true ;
//            m_pipeline->IsLastPass() = true ;
//            m_pipeline->IsLastPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFrameTrackingEnabled() = false ;
//            m_pipeline->IsLastPass() = false ;
//            m_pipeline->IsLastPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFrameTrackingEnabled() = true ;
//            m_pipeline->IsLastPass() = false ;
//            m_pipeline->IsLastPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFrameTrackingEnabled() = false ;
//            m_pipeline->IsLastPass() = true ;
//            m_pipeline->IsLastPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFrameTrackingEnabled() = true ;
//            m_pipeline->IsLastPass() = true ;
//            m_pipeline->IsLastPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchSliceLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::PatchTileLevelCommandsTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            uint8_t packetPhase = 0;

            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

            // !m_hevcPicParams->tiles_enabled_flag
//            m_hevcPicParams->tiles_enabled_flag = 0;
            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_hevcPicParams->tiles_enabled_flag = 1;
            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);


            // (m_basicFeature->m_lastPicInSeq || m_basicFeature->m_lastPicInStream) && m_pipeline->IsLastPipe()
//            m_basicFeature->m_lastPicInSeq = 0;
//            m_basicFeature->m_lastPicInStream = 0;
//            m_pipeline->IsLastPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_basicFeature->m_lastPicInSeq = 1;
//            m_basicFeature->m_lastPicInStream = 0;
//            m_pipeline->IsLastPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_basicFeature->m_lastPicInSeq = 0;
//            m_basicFeature->m_lastPicInStream = 1;
//            m_pipeline->IsLastPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_basicFeature->m_lastPicInSeq = 1;
//            m_basicFeature->m_lastPicInStream = 1;
//            m_pipeline->IsLastPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_basicFeature->m_lastPicInSeq = 0;
//            m_basicFeature->m_lastPicInStream = 0;
//            m_pipeline->IsLastPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_basicFeature->m_lastPicInSeq = 1;
//            m_basicFeature->m_lastPicInStream = 0;
//            m_pipeline->IsLastPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_basicFeature->m_lastPicInSeq = 0;
//            m_basicFeature->m_lastPicInStream = 1;
//            m_pipeline->IsLastPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);

//            m_basicFeature->m_lastPicInSeq = 1;
//            m_basicFeature->m_lastPicInStream = 1;
//            m_pipeline->IsLastPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchTileLevelCommands(cmdBuffer, packetPhase), MOS_STATUS_NULL_POINTER);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddOneTileCommandsTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            uint32_t tileRow = 0;

            uint32_t tileCol = 0;

            uint32_t tileRowPass = 0;

            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);

            // (m_pipeline->GetPipeNum() > 1) && (tileCol != m_pipeline->GetCurrentPipe())
//            m_pipeline->SetPipeNum(0);
            tileCol = 0;
//            m_pipeline->SetCurrentPipe(0);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);

//            m_pipeline->SetPipeNum(1);
            tileCol = 0;
//            m_pipeline->SetCurrentPipe(0);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);

//            m_pipeline->SetPipeNum(0);
            tileCol = 1;
//            m_pipeline->SetCurrentPipe(0);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);

//            m_pipeline->SetPipeNum(1);
            tileCol = 1;
//            m_pipeline->SetCurrentPipe(0);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);

//            m_pipeline->SetPipeNum(0);
            tileCol = 0;
//            m_pipeline->SetCurrentPipe(1);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);

//            m_pipeline->SetPipeNum(1);
            tileCol = 0;
//            m_pipeline->SetCurrentPipe(1);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);

//            m_pipeline->SetPipeNum(0);
            tileCol = 1;
//            m_pipeline->SetCurrentPipe(1);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);

//            m_pipeline->SetPipeNum(1);
            tileCol = 1;
//            m_pipeline->SetCurrentPipe(1);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);


            // m_pipeline->GetNumPipes() > 1
//            m_pipeline->SetNumPipes(0);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);

//            m_pipeline->SetNumPipes(1);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);


            // m_pipeline->GetNumPipes() > 1
//            m_pipeline->SetNumPipes(0);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);

//            m_pipeline->SetNumPipes(1);
            EXPECT_EQ(HevcVdencPktG12::AddOneTileCommands(cmdBuffer, tileRow, tileCol, tileRowPass), MOS_STATUS_NULL_POINTER);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddSlicesCommandsInTileTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddSlicesCommandsInTile(cmdBuffer), MOS_STATUS_NULL_POINTER);

            // !sliceInTile
//            sliceInTile = 0;
            EXPECT_EQ(HevcVdencPktG12::AddSlicesCommandsInTile(cmdBuffer), MOS_STATUS_NULL_POINTER);

//            sliceInTile = 1;
            EXPECT_EQ(HevcVdencPktG12::AddSlicesCommandsInTile(cmdBuffer), MOS_STATUS_NULL_POINTER);


            // 0 == sliceNumInTile
//            sliceNumInTile = 0;
            EXPECT_EQ(HevcVdencPktG12::AddSlicesCommandsInTile(cmdBuffer), MOS_STATUS_NULL_POINTER);

//            sliceNumInTile = 1;
            EXPECT_EQ(HevcVdencPktG12::AddSlicesCommandsInTile(cmdBuffer), MOS_STATUS_NULL_POINTER);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::UpdateParametersTest()
        {

            // !m_pipeline->IsSingleTaskPhaseSupported()
//            m_pipeline->IsSingleTaskPhaseSupported() = false ;
//            m_pipeline->IsSingleTaskPhaseSupported() = true ;

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddPicStateWithNoTileTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddPicStateWithNoTile(cmdBuffer), MOS_STATUS_NULL_POINTER);

            // tileEnabled
//            tileEnabled = 0;
            EXPECT_EQ(HevcVdencPktG12::AddPicStateWithNoTile(cmdBuffer), MOS_STATUS_NULL_POINTER);

//            tileEnabled = 1;
            EXPECT_EQ(HevcVdencPktG12::AddPicStateWithNoTile(cmdBuffer), MOS_STATUS_NULL_POINTER);


            // brcFeature->IsBRCUpdateRequired()
//            brcFeature->IsBRCUpdateRequired() = false ;
            EXPECT_EQ(HevcVdencPktG12::AddPicStateWithNoTile(cmdBuffer), MOS_STATUS_NULL_POINTER);

//            brcFeature->IsBRCUpdateRequired() = true ;
            EXPECT_EQ(HevcVdencPktG12::AddPicStateWithNoTile(cmdBuffer), MOS_STATUS_NULL_POINTER);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddPicStateWithTileTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddPicStateWithTile(cmdBuffer), MOS_STATUS_NULL_POINTER);

            // !tileEnabled
//            tileEnabled = 0;
            EXPECT_EQ(HevcVdencPktG12::AddPicStateWithTile(cmdBuffer), MOS_STATUS_NULL_POINTER);

//            tileEnabled = 1;
            EXPECT_EQ(HevcVdencPktG12::AddPicStateWithTile(cmdBuffer), MOS_STATUS_NULL_POINTER);


            // brcFeature->IsBRCUpdateRequired()
//            brcFeature->IsBRCUpdateRequired() = false ;
            EXPECT_EQ(HevcVdencPktG12::AddPicStateWithTile(cmdBuffer), MOS_STATUS_NULL_POINTER);

//            brcFeature->IsBRCUpdateRequired() = true ;
            EXPECT_EQ(HevcVdencPktG12::AddPicStateWithTile(cmdBuffer), MOS_STATUS_NULL_POINTER);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddHcpPipeBufAddrCmdTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddHcpPipeBufAddrCmd(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddPictureHcpCommandsTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddPictureHcpCommands(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddVdencWalkerStateCmdTest()
        {
            MHW_VDBOX_HEVC_SLICE_STATE params;
            memset(&params, 0, sizeof(params));

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddVdencWalkerStateCmd(params, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetHcpPipeBufAddrParamsTest()
        {
            MHW_VDBOX_PIPE_BUF_ADDR_PARAMS pipeBufAddrParams;
            memset(&pipeBufAddrParams, 0, sizeof(pipeBufAddrParams));


            // m_pipeline->GetNumPipes() > 1
//            m_pipeline->SetNumPipes(0);
//            m_pipeline->SetNumPipes(1);

            // m_basicFeature->m_pictureCodingType == I_TYPE
//            m_basicFeature->m_pictureCodingType = 0;
//            I_TYPE = 0;
//            m_basicFeature->m_pictureCodingType = 1;
//            I_TYPE = 0;
//            m_basicFeature->m_pictureCodingType = 0;
//            I_TYPE = 1;
//            m_basicFeature->m_pictureCodingType = 1;
//            I_TYPE = 1;

            // pipeBufAddrParams.presReferences[i] == nullptr
//            pipeBufAddrParams.presReferences[i] = 0;
//            pipeBufAddrParams.presReferences[i] = 1;

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddPictureVdencCommandsTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddPictureVdencCommands(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetVdencPipeBufAddrParamsTest()
        {
            MHW_VDBOX_PIPE_BUF_ADDR_PARAMS pipeBufAddrParams;
            memset(&pipeBufAddrParams, 0, sizeof(pipeBufAddrParams));

            EXPECT_EQ(HevcVdencPktG12::SetVdencPipeBufAddrParams(pipeBufAddrParams), MOS_STATUS_NULL_POINTER);

            // m_pictureCodingType == I_TYPE
//            m_pictureCodingType = 0;
//            I_TYPE = 0;
            EXPECT_EQ(HevcVdencPktG12::SetVdencPipeBufAddrParams(pipeBufAddrParams), MOS_STATUS_NULL_POINTER);

//            m_pictureCodingType = 1;
//            I_TYPE = 0;
            EXPECT_EQ(HevcVdencPktG12::SetVdencPipeBufAddrParams(pipeBufAddrParams), MOS_STATUS_NULL_POINTER);

//            m_pictureCodingType = 0;
//            I_TYPE = 1;
            EXPECT_EQ(HevcVdencPktG12::SetVdencPipeBufAddrParams(pipeBufAddrParams), MOS_STATUS_NULL_POINTER);

//            m_pictureCodingType = 1;
//            I_TYPE = 1;
            EXPECT_EQ(HevcVdencPktG12::SetVdencPipeBufAddrParams(pipeBufAddrParams), MOS_STATUS_NULL_POINTER);


            // pipeBufAddrParams.presVdencReferences[i] == nullptr
//            pipeBufAddrParams.presVdencReferences[i] = 0;
            EXPECT_EQ(HevcVdencPktG12::SetVdencPipeBufAddrParams(pipeBufAddrParams), MOS_STATUS_NULL_POINTER);

//            pipeBufAddrParams.presVdencReferences[i] = 1;
            EXPECT_EQ(HevcVdencPktG12::SetVdencPipeBufAddrParams(pipeBufAddrParams), MOS_STATUS_NULL_POINTER);


            // i != 0
//            i = 0;
            EXPECT_EQ(HevcVdencPktG12::SetVdencPipeBufAddrParams(pipeBufAddrParams), MOS_STATUS_NULL_POINTER);

//            i = 1;
            EXPECT_EQ(HevcVdencPktG12::SetVdencPipeBufAddrParams(pipeBufAddrParams), MOS_STATUS_NULL_POINTER);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::PatchPictureLevelCommandsTest()
        {
            uint8_t packetPhase = 0;

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::PatchPictureLevelCommands(packetPhase, cmdBuffer), MOS_STATUS_NULL_POINTER);

            // (m_pipeline->IsFirstPass() && !feature->IsACQPEnabled())
//            m_pipeline->IsFirstPass() = false ;
//            feature->IsACQPEnabled() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchPictureLevelCommands(packetPhase, cmdBuffer), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFirstPass() = true ;
//            feature->IsACQPEnabled() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchPictureLevelCommands(packetPhase, cmdBuffer), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFirstPass() = false ;
//            feature->IsACQPEnabled() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchPictureLevelCommands(packetPhase, cmdBuffer), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFirstPass() = true ;
//            feature->IsACQPEnabled() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchPictureLevelCommands(packetPhase, cmdBuffer), MOS_STATUS_NULL_POINTER);


            // m_pipeline->IsFirstPipe()
//            m_pipeline->IsFirstPipe() = false ;
            EXPECT_EQ(HevcVdencPktG12::PatchPictureLevelCommands(packetPhase, cmdBuffer), MOS_STATUS_NULL_POINTER);

//            m_pipeline->IsFirstPipe() = true ;
            EXPECT_EQ(HevcVdencPktG12::PatchPictureLevelCommands(packetPhase, cmdBuffer), MOS_STATUS_NULL_POINTER);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::InsertSeqStreamEndTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::InsertSeqStreamEnd(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::EnsureAllCommandsExecutedTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::EnsureAllCommandsExecuted(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetHcpPipeModeSelectParamsTest()
        {
            MHW_VDBOX_PIPE_MODE_SELECT_PARAMS vdboxPipeModeSelectParams;
            memset(&vdboxPipeModeSelectParams, 0, sizeof(vdboxPipeModeSelectParams));


            // m_pipeline->GetPipeNum() > 1
//            m_pipeline->SetPipeNum(0);
//            m_pipeline->SetPipeNum(1);

            // m_pipeline->IsFirstPipe()
//            m_pipeline->IsFirstPipe() = false ;
//            m_pipeline->IsFirstPipe() = true ;

            // m_hevcPicParams->tiles_enabled_flag
//            m_hevcPicParams->tiles_enabled_flag = 0;
//            m_hevcPicParams->tiles_enabled_flag = 1;

            // m_hevcSeqParams->EnableStreamingBufferLLC || m_hevcSeqParams->EnableStreamingBufferDDR
//            m_hevcSeqParams->EnableStreamingBufferLLC = 0;
//            m_hevcSeqParams->EnableStreamingBufferDDR = 0;
//            m_hevcSeqParams->EnableStreamingBufferLLC = 1;
//            m_hevcSeqParams->EnableStreamingBufferDDR = 0;
//            m_hevcSeqParams->EnableStreamingBufferLLC = 0;
//            m_hevcSeqParams->EnableStreamingBufferDDR = 1;
//            m_hevcSeqParams->EnableStreamingBufferLLC = 1;
//            m_hevcSeqParams->EnableStreamingBufferDDR = 1;

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddHcpRefIdxCmdTest()
        {
            PMOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            PMHW_BATCH_BUFFER batchBuffer;
            memset(&batchBuffer, 0, sizeof(batchBuffer));

            PMHW_VDBOX_HEVC_SLICE_STATE params;
            memset(&params, 0, sizeof(params));

            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

            // cmdBuffer == nullptr && batchBuffer == nullptr
            cmdBuffer = 0;
            batchBuffer = 0;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

            cmdBuffer = 1;
            batchBuffer = 0;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

            cmdBuffer = 0;
            batchBuffer = 1;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

            cmdBuffer = 1;
            batchBuffer = 1;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);


            // hevcSlcParams->slice_type != encodeHevcISlice
//            hevcSlcParams->slice_type = 0;
//            encodeHevcISlice = 0;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

//            hevcSlcParams->slice_type = 1;
//            encodeHevcISlice = 0;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

//            hevcSlcParams->slice_type = 0;
//            encodeHevcISlice = 1;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

//            hevcSlcParams->slice_type = 1;
//            encodeHevcISlice = 1;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);


            // eStatus != MOS_STATUS_SUCCESS
//            eStatus = 0;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

//            eStatus = 1;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);


            // hevcSlcParams->slice_type == encodeHevcBSlice
//            hevcSlcParams->slice_type = 0;
//            encodeHevcBSlice = 0;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

//            hevcSlcParams->slice_type = 1;
//            encodeHevcBSlice = 0;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

//            hevcSlcParams->slice_type = 0;
//            encodeHevcBSlice = 1;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

//            hevcSlcParams->slice_type = 1;
//            encodeHevcBSlice = 1;
            EXPECT_EQ(HevcVdencPktG12::AddHcpRefIdxCmd(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddHcpPipeModeSelectTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddHcpPipeModeSelect(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddHcpSurfacesTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddHcpSurfaces(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetVdencPipeModeSelectParamsTest()
        {
            MHW_VDBOX_PIPE_MODE_SELECT_PARAMS vdboxPipeModeSelectParams;
            memset(&vdboxPipeModeSelectParams, 0, sizeof(vdboxPipeModeSelectParams));


            // m_enableSCC && (m_hevcPicParams->pps_curr_pic_ref_enabled_flag || m_hevcSeqParams->palette_mode_enabled_flag)
//            m_enableSCC = 0;
//            m_hevcPicParams->pps_curr_pic_ref_enabled_flag = 0;
//            m_hevcSeqParams->palette_mode_enabled_flag = 0;
//            m_enableSCC = 1;
//            m_hevcPicParams->pps_curr_pic_ref_enabled_flag = 0;
//            m_hevcSeqParams->palette_mode_enabled_flag = 0;
//            m_enableSCC = 0;
//            m_hevcPicParams->pps_curr_pic_ref_enabled_flag = 1;
//            m_hevcSeqParams->palette_mode_enabled_flag = 0;
//            m_enableSCC = 1;
//            m_hevcPicParams->pps_curr_pic_ref_enabled_flag = 1;
//            m_hevcSeqParams->palette_mode_enabled_flag = 0;
//            m_enableSCC = 0;
//            m_hevcPicParams->pps_curr_pic_ref_enabled_flag = 0;
//            m_hevcSeqParams->palette_mode_enabled_flag = 1;
//            m_enableSCC = 1;
//            m_hevcPicParams->pps_curr_pic_ref_enabled_flag = 0;
//            m_hevcSeqParams->palette_mode_enabled_flag = 1;
//            m_enableSCC = 0;
//            m_hevcPicParams->pps_curr_pic_ref_enabled_flag = 1;
//            m_hevcSeqParams->palette_mode_enabled_flag = 1;
//            m_enableSCC = 1;
//            m_hevcPicParams->pps_curr_pic_ref_enabled_flag = 1;
//            m_hevcSeqParams->palette_mode_enabled_flag = 1;

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetHcpSliceStateCommonParamsTest()
        {
            MHW_VDBOX_HEVC_SLICE_STATE sliceStateParams;
            memset(&sliceStateParams, 0, sizeof(sliceStateParams));


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetHcpSliceStateParamsTest()
        {
            MHW_VDBOX_HEVC_SLICE_STATE sliceStateParams;
            memset(&sliceStateParams, 0, sizeof(sliceStateParams));

            PCODEC_ENCODER_SLCDATA slcData;
            memset(&slcData, 0, sizeof(slcData));

            uint32_t currSlcIdx = 0;

            EXPECT_EQ(HevcVdencPktG12::SetHcpSliceStateParams(sliceStateParams, slcData, currSlcIdx), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::Construct3rdLevelBatchTest()
        {
            EXPECT_EQ(HevcVdencPktG12::Construct3rdLevelBatch(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AllocateResourcesTest()
        {
            EXPECT_EQ(HevcVdencPktG12::AllocateResources(), MOS_STATUS_SUCCESS);

            // eStatus != MOS_STATUS_SUCCESS
//            eStatus = 0;
            EXPECT_EQ(HevcVdencPktG12::AllocateResources(), MOS_STATUS_SUCCESS);

//            eStatus = 1;
            EXPECT_EQ(HevcVdencPktG12::AllocateResources(), MOS_STATUS_SUCCESS);


            // eStatus != MOS_STATUS_SUCCESS
//            eStatus = 0;
            EXPECT_EQ(HevcVdencPktG12::AllocateResources(), MOS_STATUS_SUCCESS);

//            eStatus = 1;
            EXPECT_EQ(HevcVdencPktG12::AllocateResources(), MOS_STATUS_SUCCESS);


            // eStatus != MOS_STATUS_SUCCESS
//            eStatus = 0;
            EXPECT_EQ(HevcVdencPktG12::AllocateResources(), MOS_STATUS_SUCCESS);

//            eStatus = 1;
            EXPECT_EQ(HevcVdencPktG12::AllocateResources(), MOS_STATUS_SUCCESS);


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::InitTest()
        {
            EXPECT_EQ(HevcVdencPktG12::Init(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::PrepareTest()
        {
            EXPECT_EQ(HevcVdencPktG12::Prepare(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::DestoryTest()
        {
            EXPECT_EQ(HevcVdencPktG12::Destory(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::CompletedTest()
        {
            void *mfxStatus = nullptr;

            void *rcsStatus = nullptr;

            void *statusReport = nullptr;

            EXPECT_EQ(HevcVdencPktG12::Completed(mfxStatus, rcsStatus, statusReport), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::GetVdencStateCommandsDataSizeTest()
        {
            uint32_t vdencPictureStatesSize = 0;

            uint32_t vdencPicturePatchListSize = 0;

            EXPECT_EQ(HevcVdencPktG12::GetVdencStateCommandsDataSize(vdencPictureStatesSize, vdencPicturePatchListSize), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::CalculateCommandSizeTest()
        {
            uint32_t commandBufferSize = 0;

            uint32_t requestedPatchListSize = 0;

            EXPECT_EQ(HevcVdencPktG12::CalculateCommandSize(commandBufferSize, requestedPatchListSize), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::GetPacketNameTest()
        {

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::GetHxxPrimitiveCommandSizeTest()
        {
            EXPECT_EQ(HevcVdencPktG12::GetHxxPrimitiveCommandSize(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::CalculateCommandBufferSizeTest()
        {
            EXPECT_EQ(HevcVdencPktG12::CalculateCommandBufferSize(), 0);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::CalculatePatchListSizeTest()
        {
            EXPECT_EQ(HevcVdencPktG12::CalculatePatchListSize(), 0);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::EndStatusReportTest()
        {
            uint32_t srType = 0;

            MOS_COMMAND_BUFFER *cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::EndStatusReport(srType, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::ReadHcpStatusTest()
        {
            MHW_VDBOX_NODE_IND vdboxIndex;
            memset(&vdboxIndex, 0, sizeof(vdboxIndex));

            MediaStatusReport *statusReport;
            memset(&statusReport, 0, sizeof(statusReport));

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::ReadHcpStatus(vdboxIndex, statusReport, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetPakPassTypeTest()
        {

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetHcpSrcSurfaceParamsTest()
        {
            MHW_VDBOX_SURFACE_PARAMS srcSurfaceParams;
            memset(&srcSurfaceParams, 0, sizeof(srcSurfaceParams));


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetHcpReconSurfaceParamsTest()
        {
            MHW_VDBOX_SURFACE_PARAMS reconSurfaceParams;
            memset(&reconSurfaceParams, 0, sizeof(reconSurfaceParams));


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddHcpIndObjBaseAddrCmdTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddHcpIndObjBaseAddrCmd(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetHcpIndObjBaseAddrParamsTest()
        {
            MHW_VDBOX_IND_OBJ_BASE_ADDR_PARAMS indObjBaseAddrParams;
            memset(&indObjBaseAddrParams, 0, sizeof(indObjBaseAddrParams));


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddHcpQmStateCmdTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddHcpQmStateCmd(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetHcpQmStateParamsTest()
        {
            MHW_VDBOX_QM_PARAMS fqmParams;
            memset(&fqmParams, 0, sizeof(fqmParams));

            MHW_VDBOX_QM_PARAMS qmParams;
            memset(&qmParams, 0, sizeof(qmParams));


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetVdencSurfaceStateParamsTest()
        {
            MHW_VDBOX_SURFACE_PARAMS srcSurfaceParams;
            memset(&srcSurfaceParams, 0, sizeof(srcSurfaceParams));

            MHW_VDBOX_SURFACE_PARAMS reconSurfaceParams;
            memset(&reconSurfaceParams, 0, sizeof(reconSurfaceParams));


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetVdencDSSurfaceStateParamsTest()
        {
            MHW_VDBOX_SURFACE_PARAMS ds8xSurfaceParams;
            memset(&ds8xSurfaceParams, 0, sizeof(ds8xSurfaceParams));

            MHW_VDBOX_SURFACE_PARAMS ds4xSurfaceParams;
            memset(&ds4xSurfaceParams, 0, sizeof(ds4xSurfaceParams));


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SendHwSliceEncodeCommandTest()
        {
            MHW_VDBOX_HEVC_SLICE_STATE params;
            memset(&params, 0, sizeof(params));

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::SendHwSliceEncodeCommand(params, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetVdencDsRefSurfaceStateParamsTest()
        {
            PMOS_SURFACE ds8xSurface;
            memset(&ds8xSurface, 0, sizeof(ds8xSurface));

            PMOS_SURFACE ds4xSurface;
            memset(&ds4xSurface, 0, sizeof(ds4xSurface));

            CODECHAL_MODE mode;
            memset(&mode, 0, sizeof(mode));

            MHW_VDBOX_SURFACE_PARAMS ds8xSurfaceParams;
            memset(&ds8xSurfaceParams, 0, sizeof(ds8xSurfaceParams));

            MHW_VDBOX_SURFACE_PARAMS ds4xSurfaceParams;
            memset(&ds4xSurfaceParams, 0, sizeof(ds4xSurfaceParams));


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::VdencPipeModeSelectTest()
        {
            MHW_VDBOX_PIPE_MODE_SELECT_PARAMS pipeModeSelectParams;
            memset(&pipeModeSelectParams, 0, sizeof(pipeModeSelectParams));

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::VdencPipeModeSelect(pipeModeSelectParams, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetVdencSurfacesTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::SetVdencSurfaces(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddVdencPipeBufAddrCmdTest()
        {
            MHW_VDBOX_PIPE_BUF_ADDR_PARAMS pipeBufAddrParams;
            memset(&pipeBufAddrParams, 0, sizeof(pipeBufAddrParams));

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddVdencPipeBufAddrCmd(pipeBufAddrParams, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::ReadSliceSizeForSinglePipeTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::ReadSliceSizeForSinglePipe(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::ReadSliceSizeTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::ReadSliceSize(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::CopyDataBlockTest()
        {
            PMOS_RESOURCE sourceSurface;
            memset(&sourceSurface, 0, sizeof(sourceSurface));

            uint32_t sourceOffset = 0;

            PMOS_RESOURCE destSurface;
            memset(&destSurface, 0, sizeof(destSurface));

            uint32_t destOffset = 0;

            uint32_t copySize = 0;

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::CopyDataBlock(sourceSurface, sourceOffset, destSurface, destOffset, copySize, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::WaitHevcDoneTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::WaitHevcDone(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::WaitVdencDoneTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::WaitVdencDone(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::WaitHevcVdencDoneTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::WaitHevcVdencDone(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddHcpWeightOffsetStateCmdTest()
        {
            CODEC_HEVC_ENCODE_SLICE_PARAMS hevcSlcParams;
            memset(&hevcSlcParams, 0, sizeof(hevcSlcParams));

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddHcpWeightOffsetStateCmd(hevcSlcParams, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddHcpHevcVp9RdoqStateCmdTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            PMHW_VDBOX_HEVC_PIC_STATE params;
            memset(&params, 0, sizeof(params));

            EXPECT_EQ(HevcVdencPktG12::AddHcpHevcVp9RdoqStateCmd(cmdBuffer, params), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddHcpPakInsertSliceHeaderTest()
        {
            MHW_VDBOX_HEVC_SLICE_STATE params;
            memset(&params, 0, sizeof(params));

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            PMHW_BATCH_BUFFER batchBuffer;
            memset(&batchBuffer, 0, sizeof(batchBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddHcpPakInsertSliceHeader(params, cmdBuffer, batchBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddVdencWeightOffsetStateCmdTest()
        {
            CODEC_HEVC_ENCODE_SLICE_PARAMS hevcSlcParams;
            memset(&hevcSlcParams, 0, sizeof(hevcSlcParams));

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddVdencWeightOffsetStateCmd(hevcSlcParams, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::ValidateVdboxIdxTest()
        {
            MHW_VDBOX_NODE_IND vdboxIndex;
            memset(&vdboxIndex, 0, sizeof(vdboxIndex));

            EXPECT_EQ(HevcVdencPktG12::ValidateVdboxIdx(vdboxIndex), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetPerfTagTest()
        {
            uint16_t type = 0;

            uint16_t mode = 0;

            uint16_t picCodingType = 0;


            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetSemaphoreMemTest()
        {
            MOS_RESOURCE semaphoreMem;
            memset(&semaphoreMem, 0, sizeof(semaphoreMem));

            uint32_t value = 0;

            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::SetSemaphoreMem(semaphoreMem, value, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SendPrologCmdsTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::SendPrologCmds(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AllocateBatchBufferForPakSlicesTest()
        {
            uint32_t numSlices = 0;

            uint8_t numPakPasses = 0;

            EXPECT_EQ(HevcVdencPktG12::AllocateBatchBufferForPakSlices(numSlices, numPakPasses), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetBatchBufferForPakSlicesTest()
        {
            EXPECT_EQ(HevcVdencPktG12::SetBatchBufferForPakSlices(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::ReadSseStatisticsTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::ReadSseStatistics(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddForceWakeupTest()
        {
            MOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::AddForceWakeup(cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::AddHcpPakInsertNALUsTest()
        {
            PMOS_COMMAND_BUFFER cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            PMHW_BATCH_BUFFER batchBuffer;
            memset(&batchBuffer, 0, sizeof(batchBuffer));

            PMHW_VDBOX_HEVC_SLICE_STATE params;
            memset(&params, 0, sizeof(params));

            EXPECT_EQ(HevcVdencPktG12::AddHcpPakInsertNALUs(cmdBuffer, batchBuffer, params), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::CalculatePSNRTest()
        {
            EncodeStatusMfx *encodeStatusMfx;
            memset(&encodeStatusMfx, 0, sizeof(encodeStatusMfx));

            EncodeStatusReportData *statusReportData;
            memset(&statusReportData, 0, sizeof(statusReportData));

            EXPECT_EQ(HevcVdencPktG12::CalculatePSNR(encodeStatusMfx, statusReportData), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetRowstoreCachingOffsetsTest()
        {
            EXPECT_EQ(HevcVdencPktG12::SetRowstoreCachingOffsets(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::FreeResourcesTest()
        {
            EXPECT_EQ(HevcVdencPktG12::FreeResources(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::DumpResourcesTest()
        {
            EncodeStatusMfx *encodeStatusMfx;
            memset(&encodeStatusMfx, 0, sizeof(encodeStatusMfx));

            EncodeStatusReportData *statusReportData;
            memset(&statusReportData, 0, sizeof(statusReportData));

            EXPECT_EQ(HevcVdencPktG12::DumpResources(encodeStatusMfx, statusReportData), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::GetActiveTaskTest()
        {

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::DumpOutputTest()
        {
            EXPECT_EQ(HevcVdencPktG12::DumpOutput(), MOS_STATUS_SUCCESS);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::StartStatusReportTest()
        {
            uint32_t srType = 0;

            MOS_COMMAND_BUFFER *cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::StartStatusReport(srType, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::UpdateStatusReportTest()
        {
            uint32_t srType = 0;

            MOS_COMMAND_BUFFER *cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::UpdateStatusReport(srType, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetStartTagTest()
        {
            MOS_RESOURCE *osResource;
            memset(&osResource, 0, sizeof(osResource));

            uint32_t offset = 0;

            uint32_t srType = 0;

            MOS_COMMAND_BUFFER *cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::SetStartTag(osResource, offset, srType, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

        MOS_STATUS TestHevcVdencPktG12::SetEndTagTest()
        {
            MOS_RESOURCE *osResource;
            memset(&osResource, 0, sizeof(osResource));

            uint32_t offset = 0;

            uint32_t srType = 0;

            MOS_COMMAND_BUFFER *cmdBuffer;
            memset(&cmdBuffer, 0, sizeof(cmdBuffer));

            EXPECT_EQ(HevcVdencPktG12::SetEndTag(osResource, offset, srType, cmdBuffer), MOS_STATUS_NULL_POINTER);

            return MOS_STATUS_SUCCESS;
        }

}
