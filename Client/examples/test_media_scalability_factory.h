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
//! \file     test_media_scalability_factory.h
//! \brief    header file of TestMediaScalabilityFactory class
//! \details
//!

#ifndef __TEST_MEDIA_SCALABILITY_FACTORY_H__
#define __TEST_MEDIA_SCALABILITY_FACTORY_H__


namespace 
{
    class TestMediaScalabilityFactory : public MediaScalabilityFactory
    {

    public:


        virtual ~TestMediaScalabilityFactory() {};

        //!
        //! \brief     Test  CreateScalability
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CreateScalabilityTest();

        //!
        //! \brief     Test  CreateEncodeScalability
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CreateEncodeScalabilityTest();

        //!
        //! \brief     Test  CreateDecodeScalability
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CreateDecodeScalabilityTest();

        //!
        //! \brief     Test  CreateVpScalability
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CreateVpScalabilityTest();

        //!
        //! \brief     Test  CreateScalabilityMdf
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CreateScalabilityMdfTest();

        //!
        //! \brief     Test  CreateScalabilityCmdBuf
        //!
        //! \return    MOS_STATUS
        //!            MOS_STATUS_SUCCESS if success, else fail reason
        //!
        MOS_STATUS CreateScalabilityCmdBufTest();

    private:

    };
}
#endif
