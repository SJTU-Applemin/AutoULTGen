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
//! \file     test_encode_hevc_vdenc_packet_g12.h
//! \brief    header file of TestHevcVdencPktG12 class
//! \details
//!

#ifndef __TEST_ENCODE_HEVC_VDENC_PACKET_G12_H__
#define __TEST_ENCODE_HEVC_VDENC_PACKET_G12_H__

#include "encode_hevc_vdenc_packet_g12.h"
#include "encode_hevc_vdenc_mock_pipeline_g12.h"

namespace encode
{
    class TestHevcVdencPktG12 : public HevcVdencPktG12
    {

    public:


        virtual ~TestHevcVdencPktG12() {};

        TestHevcVdencPktG12(MediaPipeline *pipeline, MediaTask *task, CodechalHwInterface *hwInterface) : HevcVdencPktG12(pipeline, task, hwInterface){};
        //!
        //! \brief     Test  Submit
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SubmitTest();

        //!
        //! \brief     Test  SetHcpPicStateParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetHcpPicStateParamsTest();

        //!
        //! \brief     Test  AddVdencCmd1Cmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddVdencCmd1CmdTest();

        //!
        //! \brief     Test  AddVdencCmd2Cmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddVdencCmd2CmdTest();

        //!
        //! \brief     Test  CalculatePictureStateCommandSize
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CalculatePictureStateCommandSizeTest();

        //!
        //! \brief     Test  PatchSliceLevelCommands
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS PatchSliceLevelCommandsTest();

        //!
        //! \brief     Test  PatchTileLevelCommands
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS PatchTileLevelCommandsTest();

        //!
        //! \brief     Test  AddOneTileCommands
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddOneTileCommandsTest();

        //!
        //! \brief     Test  AddSlicesCommandsInTile
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddSlicesCommandsInTileTest();

        //!
        //! \brief     Test  UpdateParameters
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS UpdateParametersTest();

        //!
        //! \brief     Test  AddPicStateWithNoTile
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddPicStateWithNoTileTest();

        //!
        //! \brief     Test  AddPicStateWithTile
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddPicStateWithTileTest();

        //!
        //! \brief     Test  AddHcpPipeBufAddrCmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddHcpPipeBufAddrCmdTest();

        //!
        //! \brief     Test  AddPictureHcpCommands
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddPictureHcpCommandsTest();

        //!
        //! \brief     Test  AddVdencWalkerStateCmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddVdencWalkerStateCmdTest();

        //!
        //! \brief     Test  SetHcpPipeBufAddrParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetHcpPipeBufAddrParamsTest();

        //!
        //! \brief     Test  AddPictureVdencCommands
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddPictureVdencCommandsTest();

        //!
        //! \brief     Test  SetVdencPipeBufAddrParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetVdencPipeBufAddrParamsTest();

        //!
        //! \brief     Test  PatchPictureLevelCommands
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS PatchPictureLevelCommandsTest();

        //!
        //! \brief     Test  InsertSeqStreamEnd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS InsertSeqStreamEndTest();

        //!
        //! \brief     Test  EnsureAllCommandsExecuted
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS EnsureAllCommandsExecutedTest();

        //!
        //! \brief     Test  SetHcpPipeModeSelectParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetHcpPipeModeSelectParamsTest();

        //!
        //! \brief     Test  AddHcpRefIdxCmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddHcpRefIdxCmdTest();

        //!
        //! \brief     Test  AddHcpPipeModeSelect
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddHcpPipeModeSelectTest();

        //!
        //! \brief     Test  AddHcpSurfaces
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddHcpSurfacesTest();

        //!
        //! \brief     Test  SetVdencPipeModeSelectParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetVdencPipeModeSelectParamsTest();

        //!
        //! \brief     Test  SetHcpSliceStateCommonParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetHcpSliceStateCommonParamsTest();

        //!
        //! \brief     Test  SetHcpSliceStateParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetHcpSliceStateParamsTest();

        //!
        //! \brief     Test  Construct3rdLevelBatch
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS Construct3rdLevelBatchTest();

        //!
        //! \brief     Test  AllocateResources
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AllocateResourcesTest();

        //!
        //! \brief     Test  Init
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS InitTest();

        //!
        //! \brief     Test  Prepare
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS PrepareTest();

        //!
        //! \brief     Test  Destory
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS DestoryTest();

        //!
        //! \brief     Test  Completed
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CompletedTest();

        //!
        //! \brief     Test  GetVdencStateCommandsDataSize
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS GetVdencStateCommandsDataSizeTest();

        //!
        //! \brief     Test  CalculateCommandSize
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CalculateCommandSizeTest();

        //!
        //! \brief     Test  GetPacketName
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS GetPacketNameTest();

        //!
        //! \brief     Test  GetHxxPrimitiveCommandSize
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS GetHxxPrimitiveCommandSizeTest();

        //!
        //! \brief     Test  CalculateCommandBufferSize
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CalculateCommandBufferSizeTest();

        //!
        //! \brief     Test  CalculatePatchListSize
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CalculatePatchListSizeTest();

        //!
        //! \brief     Test  EndStatusReport
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS EndStatusReportTest();

        //!
        //! \brief     Test  ReadHcpStatus
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS ReadHcpStatusTest();

        //!
        //! \brief     Test  SetPakPassType
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetPakPassTypeTest();

        //!
        //! \brief     Test  SetHcpSrcSurfaceParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetHcpSrcSurfaceParamsTest();

        //!
        //! \brief     Test  SetHcpReconSurfaceParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetHcpReconSurfaceParamsTest();

        //!
        //! \brief     Test  AddHcpIndObjBaseAddrCmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddHcpIndObjBaseAddrCmdTest();

        //!
        //! \brief     Test  SetHcpIndObjBaseAddrParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetHcpIndObjBaseAddrParamsTest();

        //!
        //! \brief     Test  AddHcpQmStateCmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddHcpQmStateCmdTest();

        //!
        //! \brief     Test  SetHcpQmStateParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetHcpQmStateParamsTest();

        //!
        //! \brief     Test  SetVdencSurfaceStateParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetVdencSurfaceStateParamsTest();

        //!
        //! \brief     Test  SetVdencDSSurfaceStateParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetVdencDSSurfaceStateParamsTest();

        //!
        //! \brief     Test  SendHwSliceEncodeCommand
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SendHwSliceEncodeCommandTest();

        //!
        //! \brief     Test  SetVdencDsRefSurfaceStateParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetVdencDsRefSurfaceStateParamsTest();

        //!
        //! \brief     Test  VdencPipeModeSelect
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS VdencPipeModeSelectTest();

        //!
        //! \brief     Test  SetVdencSurfaces
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetVdencSurfacesTest();

        //!
        //! \brief     Test  AddVdencPipeBufAddrCmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddVdencPipeBufAddrCmdTest();

        //!
        //! \brief     Test  ReadSliceSizeForSinglePipe
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS ReadSliceSizeForSinglePipeTest();

        //!
        //! \brief     Test  ReadSliceSize
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS ReadSliceSizeTest();

        //!
        //! \brief     Test  CopyDataBlock
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CopyDataBlockTest();

        //!
        //! \brief     Test  WaitHevcDone
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS WaitHevcDoneTest();

        //!
        //! \brief     Test  WaitVdencDone
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS WaitVdencDoneTest();

        //!
        //! \brief     Test  WaitHevcVdencDone
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS WaitHevcVdencDoneTest();

        //!
        //! \brief     Test  AddHcpWeightOffsetStateCmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddHcpWeightOffsetStateCmdTest();

        //!
        //! \brief     Test  AddHcpHevcVp9RdoqStateCmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddHcpHevcVp9RdoqStateCmdTest();

        //!
        //! \brief     Test  AddHcpPakInsertSliceHeader
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddHcpPakInsertSliceHeaderTest();

        //!
        //! \brief     Test  AddVdencWeightOffsetStateCmd
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddVdencWeightOffsetStateCmdTest();

        //!
        //! \brief     Test  ValidateVdboxIdx
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS ValidateVdboxIdxTest();

        //!
        //! \brief     Test  SetPerfTag
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetPerfTagTest();

        //!
        //! \brief     Test  SetSemaphoreMem
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetSemaphoreMemTest();

        //!
        //! \brief     Test  SendPrologCmds
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SendPrologCmdsTest();

        //!
        //! \brief     Test  AllocateBatchBufferForPakSlices
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AllocateBatchBufferForPakSlicesTest();

        //!
        //! \brief     Test  SetBatchBufferForPakSlices
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetBatchBufferForPakSlicesTest();

        //!
        //! \brief     Test  ReadSseStatistics
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS ReadSseStatisticsTest();

        //!
        //! \brief     Test  AddForceWakeup
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddForceWakeupTest();

        //!
        //! \brief     Test  AddHcpPakInsertNALUs
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS AddHcpPakInsertNALUsTest();

        //!
        //! \brief     Test  CalculatePSNR
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CalculatePSNRTest();

        //!
        //! \brief     Test  SetRowstoreCachingOffsets
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetRowstoreCachingOffsetsTest();

        //!
        //! \brief     Test  FreeResources
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS FreeResourcesTest();

        //!
        //! \brief     Test  DumpResources
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS DumpResourcesTest();

        //!
        //! \brief     Test  GetActiveTask
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS GetActiveTaskTest();

        //!
        //! \brief     Test  DumpOutput
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS DumpOutputTest();

        //!
        //! \brief     Test  StartStatusReport
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS StartStatusReportTest();

        //!
        //! \brief     Test  UpdateStatusReport
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS UpdateStatusReportTest();

        //!
        //! \brief     Test  SetStartTag
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetStartTagTest();

        //!
        //! \brief     Test  SetEndTag
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetEndTagTest();

    private:

    };
}
#endif
