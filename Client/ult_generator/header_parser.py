import os
import re
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
        self.system_includes = set()
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
        idx = len('namespace ')
        namespace = line[idx:].strip()
        if namespace and namespace[-1] == '{':
            namespace = namespace[:-1]
        while namespace[-1] == ' ':
            namespace = namespace[:-1]

        return namespace

    @staticmethod
    def get_class(line):
        #key word 'class' has 5 characters
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
            'override': False,
            'pure_virtual': False
        }
        s = lines[0].strip()

        if len(lines) > 1:
            for i in lines[1:]:
                s = s + ' ' + i.strip()

        if s.startswith('virtual'):
            method_info['override'] = True
            s = s[len('virtual '):].strip()

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
                para = {'type': tmp[0].strip(), 'name': tmp[1].strip()}
                if ((para['type'][-1] == '*') or (para['type'][-1] == '&')):
                    para['name'] = para['type'][-1] + para['name']
                    para['type'] = para['type'][:-1]
                method_info['parameters'].append(para)
        if method_info['method_name'].startswith('*') or method_info['method_name'].startswith('&'):
            method_info['return_type'] = method_info['return_type'] + method_info['method_name'][1:]
            method_info['method_name'] = method_info['method_name'][1:]

        return method_info

    def parse_define(self, line_index):
        curlines = self.lines[line_index:]
        skip_line_count = 0
        for iline in curlines:
            iline = iline.strip()
            if iline.endswith('\\') == False:
                break
            skip_line_count += 1
        return skip_line_count

    def parse_struct(self, line_index, left_brace_count, right_brace_count):
        if left_brace_count != 0 and left_brace_count == right_brace_count:
            return 0
        curlines = self.lines[line_index:]
        skip_line_count = 0
        for iline in curlines:
            skip_line_count += 1
            iline = iline.strip()
            if not iline:
                continue
            left_brace_count += iline.count('{')
            right_brace_count += iline.count('}')
            if left_brace_count == right_brace_count:
                return skip_line_count
        print('parse_struct failed!!!!!!, Line: ' + line_index + '/n')
        return 0

    def parse_comments(self, line_index, lines):
        skip_count = 0
        curlines = lines[line_index:]
        curline = curlines[0]
        if curline.find('//') != -1:
            idx = curline.find('//')
            curline = curline[:idx]
            return 0, curline

        if curline.find('/*') != -1:
            comment_satrt_count = curline.count('/*')
            comment_end_count =  curline.count('*/')
            if comment_satrt_count == comment_end_count:
                return 0, re.sub('[/][*].*?[*][/]','', curline)
            iline_index = 0
            for iline in curlines[1:]:
                comment_satrt_count += iline.count('/*')
                comment_end_count += iline.count('*/')
                iline_index += 1
                if comment_satrt_count == comment_end_count:
                    return iline_index, iline[:iline.rfind('*/')]
            print('comments error!!!!!!, Line: ' + line_index + '/n')
        return skip_count, curline

    def parse_class(self, line_index, left_brace_count, right_brace_count):
        if left_brace_count != 0 and left_brace_count == right_brace_count:
            print('parse_class error????? Line: ' + line_index + '/n')
            return 0
        curlines = self.lines[line_index:]
        skip_line_count = 0
        iline_index = 0
        f_ignore = False
        f_method = False
        method_type = 'private'
        imethod = ''
        semicolon_count = 0
        for iline in curlines:
            iline_index += 1
            if skip_line_count != 0:
                skip_line_count -= 1
                continue
            iline = iline.strip()
            if not iline:
                continue

            skip_line_count, line_clr = self.parse_comments(iline_index -1, curlines)
            line_clr = line_clr.strip()
            if not line_clr:
                continue
            #in case there is { or } in the comments
            left_brace_count += line_clr.count('{')
            right_brace_count += line_clr.count('}')
            if line_clr.startswith('public:'):
                method_type = 'public'
                continue
            if line_clr.startswith('protected:'):
                method_type = 'protected'
                continue
            if line_clr.startswith('private:'):
                method_type = 'private'
                continue
            if left_brace_count != 0 and left_brace_count == right_brace_count:
                line_clr = line_clr[:line_clr.find('};')]
                line_clr = line_clr.strip()
                if not line_clr:
                    return iline_index
            # memeber functions/ variables
            imethod += line_clr
            #Find a complete variable/method declaration
            bpurevirtualfunc = False
            if line_clr.endswith(';'):
                pure_virtual_pattern =  r'^virtual .*[(].*[)] *= *0 *;'
                if re.match(pure_virtual_pattern, line_clr):
                    bpurevirtualfunc = True
                bFind = True

            f_method = True
            
            if line_clr.find('(') != -1 and line_clr.find('=') == -1:
                self.methods.append([iline])
                if not(line_clr[-1] == ';' or line_clr[-1] == '}'):
                    f_method = True
                continue

            if left_brace_count != 0 and left_brace_count == right_brace_count:
                return iline_index
        print('parse_struct failed!!!!!!, Line: ' + line_index + '/n')
        return 0

    def parse_file_info(self):
        """

        :return:
        """
        if not self.lines:
            print('Please read file first\n')
            return
        f_method = False
        line_index = 0
        skip_line_count = 0
        for line in self.lines:
            line_index += 1
            line_clr = line.strip()
            if skip_line_count != 0:
                skip_line_count -= 1
                continue
            skip_line_count, line_clr = self.parse_comments(line_index -1, self.lines)
            if not line_clr or line_clr == '{' or line_clr == '}':
                continue
            if line_clr.startswith('#include'):
                line_clr = line_clr[len('#include'):].strip()
                if line_clr.find('<') != -1 :
                    line_clr = line_clr.strip('<')
                    line_clr = line_clr.strip('>')
                    self.system_includes.add(filename)
                    continue
                line_clr = line_clr.strip('"')
                self.includes.add(line_clr)
                continue
            if line_clr.startswith('#define'):
                if line_clr.endswith('\\'):
                    skip_line_count = self.parse_define(line_index)
                continue
            # such as #ifdef
            if line_clr.startswith('#'):
                continue
            if f_method:
                self.methods[-1].append(line)
                if line_clr[-1] == ';':
                    f_method = False
                continue
            if line_clr.startswith('namespace'):
                self.namespace = self.get_namespace(line_clr)
                continue
            if line_clr.startswith('typedef '):
                 if line_clr.endswith(';'):
                     continue
                 line_clr = line_clr.strip('typedef ')
                 line_clr = line_clr.strip()

            if line_clr.startswith('class'):
                # class A;
                if line_clr.endswith(';') == True:
                    continue
                self.class_name, self.super_class = self.get_class(line_clr)
                skip_line_count = self.parse_class(line_index, line_clr.count('{'), line_clr.count('}'))
                continue
            if line_clr.startswith('struct'):
                #struct A;
                if line_clr.endswith(';') == True:
                    continue
                skip_line_count = self.parse_struct(line_index, line_clr.count('{'), line_clr.count('}'))
                continue

            #Todo, add more semantic analysis
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

