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
//! \file     test_encode_scalability_singlepipe.h
//! \brief    header file of TestEncodeScalabilitySinglePipe class
//! \details
//!

#ifndef __TEST_ENCODE_SCALABILITY_SINGLEPIPE_H__
#define __TEST_ENCODE_SCALABILITY_SINGLEPIPE_H__

#include "memory_leak_detector.h"
#include "mock_platform.h"
#include "encode_test_fixture.h"
#include "encode_scalability_singlepipe.h"

namespace encode
{
    class TestEncodeScalabilitySinglePipe : public EncodeScalabilitySinglePipe
    {

    public:


        virtual ~TestEncodeScalabilitySinglePipe() {};

        TestEncodeScalabilitySinglePipe(void *hwInterface, MediaContext *mediaContext, uint8_t componentType) : EncodeScalabilitySinglePipe(hwInterface, mediaContext, componentType){};
        //!
        //! \brief     Test  Initialize
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS InitializeTest();

        //!
        //! \brief     Test  UpdateState
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS UpdateStateTest();

        //!
        //! \brief     Test  VerifyCmdBuffer
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS VerifyCmdBufferTest();

        //!
        //! \brief     Test  VerifySpaceAvailable
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS VerifySpaceAvailableTest();

        //!
        //! \brief     Test  ResizeCommandBufferAndPatchList
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS ResizeCommandBufferAndPatchListTest();

        //!
        //! \brief     Test  SendAttrWithFrameTracking
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SendAttrWithFrameTrackingTest();

        //!
        //! \brief     Test  GetGpuCtxCreationOption
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS GetGpuCtxCreationOptionTest();

        //!
        //! \brief     Test  Destroy
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS DestroyTest();

        //!
        //! \brief     Test  GetCmdBuffer
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS GetCmdBufferTest();

        //!
        //! \brief     Test  ReturnCmdBuffer
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS ReturnCmdBufferTest();

        //!
        //! \brief     Test  SubmitCmdBuffer
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SubmitCmdBufferTest();

        //!
        //! \brief     Test  SyncPipe
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SyncPipeTest();

        //!
        //! \brief     Test  ResetSemaphore
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS ResetSemaphoreTest();

        //!
        //! \brief     Test  SetHintParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS SetHintParamsTest();

        //!
        //! \brief     Test  PopulateHintParams
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS PopulateHintParamsTest();

        //!
        //! \brief     Test  IsScalabilityModeMatched
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS IsScalabilityModeMatchedTest();

        //!
        //! \brief     Test  IsGpuCtxCreateOptionMatched
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS IsGpuCtxCreateOptionMatchedTest();

        //!
        //! \brief     Test  GetQueue
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS GetQueueTest();

        //!
        //! \brief     Test  GetPipeNumber
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS GetPipeNumberTest();

        //!
        //! \brief     Test  IsFrameTrackingEnabled
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS IsFrameTrackingEnabledTest();

    private:

    };
}
#endif
