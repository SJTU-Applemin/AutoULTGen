from ult_generator.generator import Generator
from ult_generator.header_parser import HeaderParser


class TestCaseGenerator(Generator):
    """

    """

    def __init__(self, head_parser):
        Generator.__init__(self)
        if isinstance(head_parser, HeaderParser):
            self.info = head_parser
            self.test_case_filename_h = self.info.name[:-2] + '_test_case.h'
            self.test_case_filename_cpp = self.info.name[:-2] + '_test_case.cpp'
            self.test_case_class_name = self.info.class_name + 'TestCase'
            self.test_class_name = 'Test' + self.info.class_name
            if self.info.namespace == 'vp':
                self.includes_h = ['TestFixture.h', 'test_' + self.info.name]
            else:
                self.includes_h = ['memory_leak_detector.h', 'mock_platform.h', 'encode_test_fixture.h',
                                'test_' + self.info.name]
            self.includes_cpp = [self.test_case_filename_h]
            self.lines_h = []
            self.lines_cpp = []
        else:
            print('Use HeadParser Class to initialize!')

    def add_body_h(self, lines, info):
        """

        :param lines:
        :param info:
        :return:
        """
        lines.append('namespace ' + info.namespace + '\n')
        lines.append('{\n')
        if info.namespace == 'vp':
            lines.append('    class ' + self.test_case_class_name + ' : public ' + 'DxvaTestFixture' + '\n')
        else:
            lines.append('    class ' + self.test_case_class_name + ' : public ' + 'EncodeTestFixture' + '\n')
        lines.append('    {\n\n')
        lines.append('    protected:\n\n')
        lines.append('\n')
        lines.append('        //!\n')
        lines.append('        //! \\brief   Initialization work before executing a unit test\n')
        lines.append('        //!\n')
        lines.append('        virtual void SetUp();\n')
        lines.append('\n')
        lines.append('        //!\n')
        lines.append('        //! \\brief   Uninitializaiton and exception handling after the unit test done\n')
        lines.append('        //!\n')
        lines.append('        virtual void TearDown();\n')
        lines.append('\n')
        if info.namespace != 'vp':
            lines.append('        //!\n')
            lines.append('        //! \\brief   Get Platform\n')
            lines.append('        //! \\param   [in] platform\n')
            lines.append('        //! \\        Reference to PLATFORM\n')
            lines.append('        //!\n')
            lines.append('        void GetPlatformByName(PLATFORM &platform);\n')
            lines.append('\n')
            lines.append('        //!\n')
            lines.append('        //! \\brief   Prepare Encode Params\n')
            lines.append('        //! \\param   [in] encodeParams\n')
            lines.append('        //! \\        Reference to EncodeParams\n')
            lines.append('        //!\n')
            lines.append('        void PrepareEncodeParams(EncoderParams &encodeParams);\n')
            lines.append('\n')

        lines.append('        ' + self.test_class_name + '        *m_test = nullptr;\n')
        lines.append('\n')
        lines.append('    };\n')
        lines.append('}\n')
        lines.append('\n')
        lines.append('#endif\n')

    def generate_h(self):
        """

        :return:
        """
        self.add_file_header(self.lines_h)
        self.add_brief_intro_h(self.lines_h, self.test_case_filename_h,self.test_case_class_name)
        self.add_includes_h(self.lines_h, self.test_case_filename_h[:-2], self.includes_h)
        self.add_body_h(self.lines_h, self.info)
        self.write_file(self.test_case_filename_h, self.lines_h)

    def add_body_cpp(self, lines, info):
        """

        :return:
        """
        lines.append('namespace ' + info.namespace + '\n')
        lines.append('{\n')
        lines.append('\n')
        lines.append('    void ' + self.test_case_class_name + '::SetUp()\n')
        lines.append('    {\n')
        lines.append('\n\n')
        lines.append('    }\n')
        lines.append('\n')
        lines.append('    void ' + self.test_case_class_name + '::TearDown()\n')
        lines.append('    {\n')
        lines.append('\n\n')
        lines.append('    }\n')
        if info.namespace != 'vp':
            lines.append('    void ' + self.test_case_class_name + '::GetPlatformByName(PLATFORM &platform)\n')
            lines.append('    {\n')
            lines.append('\n\n')
            lines.append('    }\n')
            lines.append('    void ' + self.test_case_class_name + '::PrepareEncodeParams(EncoderParams &encodeParams)\n')
            lines.append('    {\n')
            lines.append('\n\n')
            lines.append('    }\n')
        lines.append('\n\n')
        for method in info.methods_info:
            if method['method_name'] == '' or method['virtual']:
                continue
            lines.append('    TEST_F(' + self.test_case_class_name + ', ' + method['method_name'] + ')\n')
            lines.append('    {\n')
            lines.append('        EXPECT_EQ(m_test->' + method['method_name'] + 'Test(), MOS_STATUS_SUCCESS);\n')
            lines.append('    }\n')
        lines.append('}\n')

    def generate_cpp(self):
        """

        :return:
        """
        self.add_file_header(self.lines_cpp)
        self.add_brief_intro_cpp(self.lines_cpp, self.test_case_filename_cpp, self.test_case_class_name)
        self.add_includes_cpp(self.lines_cpp, self.includes_cpp)
        self.add_body_cpp(self.lines_cpp, self.info)
        self.write_file(self.test_case_filename_cpp, self.lines_cpp)
