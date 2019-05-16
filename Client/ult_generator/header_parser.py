class HeaderParser(object):
    """

    """

    def __init__(self, name, path):
        """

        :param name:
        :param path:
        """
        self.name = name
        self.path = path
        self.lines = []
        self.class_name = ''
        self.methods = []
        self.methods_info = []
        self.constructor = []
        self.destructor = []
        self.includes = set()
        self.namespace = ''
        self.super_class = ''
        self.basic_type = {'int', 'bool', 'dword', 'uint8_t', 'uint16_t', 'uint32_t', 'uint64_t', 'char'}
        self.keywords = {'static', 'constexpr', 'const', 'unsigned', '*', '&'}
        self.vars = []

    def print_info(self):
        print('--------------' + self.name + '-----------------')
        #print(self.path)
        print('Class Name:       ' + self.class_name)
        print('Namespace:        ' + self.namespace)
        print('Super Class:      ' + self.super_class + '\n')
        print('Methods Info:')
        for i in self.methods_info:
            print('\nMethod Name:      ' + i['method_name'])
            print('Return Type:      ' + i['return_type'])
            for j in i['parameters']:
                print('Type: ' + j['type'] + '        Name: ' + j['name'])
        print('\nVar Info:\n')
        print(self.vars)
        for i in self.vars:
            print('Type: ' + i['type'] + '        Name: ' + i['name'] + '\n')
        print('\n\n')

    def read_file(self, name=None, path=None):
        """

        """
        if name:
            self.name = name
        if path:
            self.path = path
        with open(self.path + self.name, 'r') as fin:
            self.lines = fin.readlines()

    @staticmethod
    def get_namespace(line):
        namespace = line[10:]
        if namespace and namespace[-1] == '{':
            namespace = namespace[:-1]
        return namespace

    @staticmethod
    def get_class(line):
        idx1 = 6
        idx2 = line.find(':')
        super_class = ''
        class_name = ''
        if idx2 == -1:
            class_name = line[idx1:].strip()
        else:
            class_name = line[idx1:idx2].strip()
            idx2 = line.find('public') + 7
            super_class = line[idx2:].strip()
            idx3 = super_class.find(',')
            if idx3 != -1:
                super_class = super_class[:idx3]

        return class_name, super_class

    def parse_method_info(self, lines):
        method_info = {
            'return_type': '',
            'method_name': '',
            'parameters': [],
            'virtual': False
        }
        s = lines[0].strip()

        if len(lines) > 1:
            for i in lines[1:]:
                s = s + ' ' + i.strip()

        if s.startswith('virtual'):
            method_info['virtual'] = True
            s = s[8:].strip()

        idx0 = s.find(' ')
        if s[:idx0].find('(') == -1:
            method_info['return_type'] = s[:idx0].strip()
        else:
            method_info['return_type'] = 'Constructor'

        idx1 = s.find('(')
        idx2 = s.find(')')
        method_info['method_name'] = s[idx0 + 1:idx1].strip()
        s_para = s[idx1 + 1:idx2]
        paras = s_para.split(',')
        for i in paras:
            tmp = i.strip().split(' ')
            tmp = [i for i in tmp if i != '']
            for t in range(len(tmp)):
                if (tmp[t] == '*' or tmp[t] == '&') and tmp[t+1]:
                    tmp[t+1] = tmp[t] + tmp[t+1]
            tmp = list(filter(lambda x: x not in self.keywords, tmp))
            if len(tmp) == 2:
                if tmp[0][-1] == '&':
                    tmp[0] = tmp[0][:-1]
                    tmp[1] = '&' + tmp[1]
                para = {'type': tmp[0].strip(), 'name': tmp[1].strip()}
                if para['type'][-1] == '*':
                    para['type'] = para['type'][:-1]
                    para['name'] = '*' + para['name']
                method_info['parameters'].append(para)
        if method_info['method_name'].startswith('*'):
            method_info['method_name'] = method_info['method_name'][1:]
            method_info['return_type'] = method_info['return_type'] + '*'
        return method_info

    def parse_file_info(self):
        """

        :return:
        """
        if not self.lines:
            print('Please read file first\n')
            return

        f_ignore = False
        method_type = 'private'
        f_method = False
        f_struct = False

        for line in self.lines:
            line_clr = line.strip()
            if f_ignore:
                idx = line_clr.find('*/')
                if idx == -1:
                    continue
                else:
                    f_ignore = False
                    line_clr = line_clr[idx+2:]
            if line_clr.startswith('/*'):
                f_ignore = True
                continue                   # continue may ignore the content and cause some problem
            if line_clr.find('//') != -1:
                idx = line_clr.find('//')
                line_clr = line_clr[:idx]
            if not line_clr:
                continue
            if line_clr.startswith('#include'):
                self.includes.add(line_clr[10:-1])
            if f_method:
                self.methods[-1].append(line)
                if line_clr[-1] == ';':
                    f_method = False
                else:
                    f_method = True
                continue
            if f_struct:
                if line_clr.find('}') != -1:
                    f_struct = False
                continue
            if line_clr.startswith('namespace'):
                self.namespace = self.get_namespace(line_clr)
                continue
            if line_clr.startswith('class'):
                self.class_name, self.super_class = self.get_class(line_clr)
                continue
            if line_clr.startswith('struct'):
                f_struct = True
            if line_clr.startswith('public:'):
                method_type = 'public'
                continue                   # continue may ignore the content and cause some problem
            if line_clr.startswith('protected:'):
                method_type = 'protected'
                continue
            if line_clr.startswith('private:'):
                method_type = 'private'
                continue
            if line_clr.find('(') != -1 and line_clr.find('=') == -1:
                self.methods.append([line])
                if not(line_clr[-1] == ';' or line_clr[-1] == '}'):
                    f_method = True
                continue

            tmp0 = line_clr.split(' ')
            tmp = []
            for t in tmp0:
                if t and t not in self.keywords:
                    tmp.append(t)
            if len(tmp) > 2:
                if tmp[1][-1] == ';':
                    tmp[1] = tmp[1][:-1]
                if tmp[0] in self.basic_type:
                    self.vars.append({'type': tmp[0], 'name': tmp[1]})

        for i in self.methods:
            self.methods_info.append(self.parse_method_info(i))

