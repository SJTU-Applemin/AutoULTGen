import os

class Included_Parser(object):
#parse all included files to find matched typename

    def __init__(self,fileName,filePath,targetName=None):
        
        self.name=fileName
        self.path=filePath
        self.target_class=targetName
        self.lines=[]
        self.includes=set()
        self.var_name=set()

        self.classes=[]
        self.structs=[]
        self.enums=[]
        self.typedefs=[]

        self.types_in_ctor=[]
        self.class_info=[]
        self.struct_info=[]
        self.enum_info=[]
        self.typedef_info=[]

        #self.namespace = ''
        self.super_class = ''

        self.basic_type = {'int', 'bool', 'dword', 'uint8_t', 'uint16_t', 'uint32_t', 'uint64_t', 'char'}
        self.keywords = {'static', 'constexpr', 'const', 'unsigned', '*', '&'}
        

    def print_info(self):
        pass

    def read_file(self, name=None, path=None):
        """
        read file by lines and save to self.lines
        """
        if name:
            self.name = name
        if path:
            self.path = path
        with open(self.path + self.name, 'r') as fin:
            self.lines = fin.readlines()

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

    def parse_class_info(self,lines,is_typedef=False):
        class_info={
            'class_name':'',
            'var_name':'',
            'is_ptr':False,
            'is_refer':False,
            'super_class':'',
            'is_typedef':False
            }
        if is_typedef:
            class_info['is_typedef']=True
        s=lines[0]
        if(len(lines))>1:
            for i in lines[1:]:
                s=s+' '+i
        idx0=s.find('{')
        idx1=s.rfind('}')
        idx2=s.rfind(';')
        if idx0==-1:
            s=s[:idx2]
        else:
            s=s[:idx0]+s[idx1+1:idx2]
        s=s[6:]
        if not 'public' in s:
            idx=s.find(' ')
            s1=s[:idx]
            s2=s[idx+1:]
            class_info['class_name']=s1
            s2=s2.split(',')
            #print(s2)
            for s in s2:
                if '*' in s:
                    class_info['is_ptr']=True
                    class_info['var_name']=s[s.find('*')+1:]
                    self.var_name.add(s[s.find('*')+1:])
                    continue
                if '&' in s:
                    class_info['is_refer']=True
                    class_info['var_name']=s[s.find('&')+1:]
                    self.var_name.add(s[s.find('&')+1:])
                    continue
            self.class_info.append(class_info)
        else:
            idx=s.find(' ')
            s1=s[:idx].strip(':')
            class_info['class_name']=s1
            s2=s[s.find('public')+7:]
            s2=s2.split(',')
            for s in s2:
                class_info['super_class']=s
            self.class_info.append(class_info)


    def parse_struct_info(self,lines,is_typedef=False):
        struct_info={
            'struct_name':'',
            'var_name':'',
            'is_ptr':False,
            'is_refer':False,
            'super_struct':'',
            'is_typedef':False
            }
        if(is_typedef):
            struct_info['is_typedef']=True
        s=lines[0]
        if(len(lines))>1:
            for i in lines[1:]:
                s=s+' '+i
        idx0=s.find('{')
        idx1=s.rfind('}')
        idx2=s.rfind(';')
        if idx0==-1:
            s=s[:idx2]
        else:
            s=s[:idx0]+s[idx1+1:idx2]
        s=s[7:]

        if not 'public' in s:
            idx=s.find(' ')
            s1=s[:idx]
            s2=s[idx+1:]
            struct_info['struct_name']=s1
            s2=s2.split(',')
            #print(s2)
            for s in s2:
                if '*' in s:
                    struct_info['is_ptr']=True
                    struct_info['var_name']=s[s.find('*')+1:]
                    self.var_name.add(s[s.find('*')+1:])
                    continue
                if '&' in s:
                    struct_info['is_refer']=True
                    struct_info['var_name']=s[s.find('&')+1:]
                    self.var_name.add(s[s.find('&')+1:])
                    continue
            self.struct_info.append(struct_info)
        else:
            idx=s.find(' ')
            s1=s[:idx].strip(':')
            struct_info['struct_name']=s1
            s2=s[s.find('public')+7:]
            s2=s2.split(',')
            for s in s2:
                struct_info['super_struct']=s
            self.struct_info.append(struct_info)

    def parse_enum_info(self,lines,is_typedef=False):
        enum_info={
            'enum_name':'',
            'var_name':'',
            'all_nums':[],
            'is_ptr':False,
            'is_refer':False,
            'is_typedef':False
            }
        if is_typedef:
            enum_info['is_typedef']=True
        s=lines[0]
        if(len(lines)>1):
            for i in lines[1:]:
                s=s+' '+i
        #print(s)
        idx0=s.find('{')
        idx1=s.rfind('}')
        idx2=s.rfind(';')
        if idx0==-1:
            s_out=s[:idx2]
            s_in=''
        else:
            s_out=s[:idx0]+s[idx1+1:idx2]
            s_in=s[idx0+1:idx1]

        #print('here \n')
        #print(s_in)
        #print('\n')
        s_out=s_out[5:]
        idx=s_out.find(' ')
        s1=s_out[:idx]
        enum_info['enum_name']=s1
        s2=s_out[idx+1:]
        s2=s2.split(',')
        for _s in s2:
            enum_info['var_name']=_s.strip()
            if '*' in _s:
                enum_info['is_ptr']=True
                enum_info['var_name']=_s[_s.find('*')+1:]
                self.var_name.add(_s[_s.find('*')+1:])
                continue
            if '&' in _s:
                enum_info['is_refer']=True
                enum_info['var_name']=_s[s_.find('&')+1:]
                self.var_name.add(_s[s_.find('&')+1:])
                continue
        nums=[]
        s_in=s_in.split(',')
        last_num=0
        for _s in s_in:
            #print('\n')
            #print(_s)
            if _s.find('=')!=-1:
                _s=_s.split('=')
                #print(_s)
                try:
                    if '0x' in _s[1]:
                        last_num=int(_s[1],16)
                        nums.append(last_num)
                    else:
                        last_num=int(_s[1])
                        nums.append(last_num)
                except:
                    if('<<') in _s[1]:
                        s3=_s[1].split('<<')
                        last_num=int(s3[0])<<int(s3[1])
                #print('TRY now the num is'+_s[0]+':'+str(last_num))
            else:
                #print()
                nums.append(last_num)
                #print('EXCEPT now the num is'+':'+str(last_num))
            last_num=last_num+1

        enum_info['all_nums']=nums
        self.enum_info.append(enum_info)




    def parse_typedef_info(self,lines):

        lines[0]=lines[0][8:]
        if(lines[0].startswith('class')):
            self.parse_class_info(lines,True)
        if(lines[0].startswith('struct')):
            self.parse_struct_info(lines,True)
        if(lines[0].startswith('enum')):
            self.parse_enum_info(lines,True)





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
                #if tmp[0][-1] == '&':
                #    tmp[0] = tmp[0][:-1]
                #    tmp[1] = '&' + tmp[1]
                para = {'type': tmp[0].strip(), 'name': tmp[1].strip()}
                if ((para['type'][-1] == '*') or (para['type'][-1] == '&')):
                    para['name'] = para['type'][-1] + para['name']
                    para['type'] = para['type'][:-1]
                method_info['parameters'].append(para)
        if method_info['method_name'].startswith('*') or method_info['method_name'].startswith('&'):
            method_info['return_type'] = method_info['return_type'] + method_info['method_name'][1:]
            method_info['method_name'] = method_info['method_name'][1:]

        return method_info



    def parse_ctsor(self,line):
        """

        """
        idx=line.find('(');
        ridx=line.find(');')
        sub_line=line[idx+1:ridx].split(',')
        #print(sub_line)
        for var_name in sub_line:
            #print(var_name.strip().split(' ')[0].strip('*').strip('&'))
            self.types_in_ctor.append(var_name.strip().split(' ')[0].strip('*').strip('&'))



    """
    def parse_sub_domain(self,domain,line_clr,domain_start=Flase,brane_count=0):
        domain.append(line_clr)
        if(domain_start==False and line_clr.find('{')!=1):
            domain_start=True
            brace_count+=1
        if domain_start==True:
            if line_clr.find('{')!=-1:
                brace_count+=line_clr.count('{')
            if line_clr.find('}')!=-1:
                brace_count-=line_clr.count('}')
            if brace_count==0:
                return domain,False
            else return domain, True
    """


    def parse_file_info(self):

        if not self.lines:
            print("please read file first")
            return

        f_ignore = False
        f_method = False
        f_class=False
        f_struct = False
        f_enum=False
        f_typedef=False

        class_start=False
        struct_start=False
        enum_start=False
        typedef_start=False
        brace_count=0

        for line in self.lines:
            line_clr = ' '.join(line.split()).strip()

            if f_ignore:
                idx = line_clr.find('*/')
                if idx == -1:
                    continue
                else:
                    f_ignore = False
                    line_clr = line_clr[idx+2:]

#                                    if line_clr[-1] == ';':
#                    f_method = False
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

            if line_clr.startswith('namespace'):
                continue

            if self.target_class:
                if line_clr.startswith(self.target_class):
                    self.parse_ctsor(line_clr)
                    #print(self.types_in_ctors)
                    #continue

            if f_class:
                self.classes[-1].append(line_clr)
                if(class_start==False and line_clr.find('{')!=-1):
                    class_start=True
                    #brace_count+=1
                if class_start==True:
                    if line_clr.find('{')!=-1:
                        brace_count+=1
                    if line_clr.find('}')!=-1:
                        brace_count-=1
                    if brace_count==0:
                        f_class=False
                continue

            if f_struct:
                self.structs[-1].append(line_clr)
                if(struct_start==False and line_clr.find('{')!=-1):
                    struct_start=True
                    #brace_count+=1
                if class_start==True:
                    if line_clr.find('{')!=-1:
                        brace_count+=1
                    if line_clr.find('}')!=-1:
                        brace_count-=1
                    if brace_count==0:
                        f_struct=False
                continue
            if f_typedef:
                self.typedefs[-1].append(line_clr)
                if(typedef_start==False and line_clr.find('{')!=-1):
                    typedef_start=True
                    #brace_count+=1
                if typedef_start==True:
                    if line_clr.find('{')!=-1:
                        brace_count+=1
                    if line_clr.find('}')!=-1:
                        brace_count-=1
                    if brace_count==0:
                        f_typedef=False
                continue



            if f_enum:
                self.enums[-1].append(line_clr)
                if(enum_start==False and line_clr.find('{')!=-1):
                    enum_start=True
                    #brace_count+=1
                if enum_start==True:
                    if line_clr.find('{')!=-1:
                        brace_count+=1
                    if line_clr.find('}')!=-1:
                        brace_count-=1
                    if brace_count==0:
                        f_enum=False
                continue



            if line_clr.startswith('class'):
                self.classes.append([line_clr])
                if not (line_clr[-1]==';'):
                    f_class=True
                continue
            if line_clr.startswith('struct'):
                self.structs.append([line_clr])
                if not(line_clr[-1]==';'):
                    f_struct=True
                continue
            if line_clr.startswith('enum'):
                self.enums.append([line_clr])
                if not(line_clr[-1]==';'):
                    f_enum=True
                continue
            if line_clr.startswith('typedef'):
                self.typedefs.append([line_clr])
                if not(line_clr[-1]==';'):
                    f_typedef=True
                continue

            if f_method:
                self.methods[-1].append(line)
                if line_clr[-1] == ';':
                    f_method = False
                #else:
                #   f_method = True
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

            if line_clr.startswith('public:'):
                method_type = 'public'
                continue                   # continue may ignore the content and cause some problem
            if line_clr.startswith('protected:'):
                method_type = 'protected'
                continue
            if line_clr.startswith('private:'):
                method_type = 'private'
                continue

            #Todo, add more semantic analysis

#        for i in self.methods:
#            self.methods_info.append(self.parse_method_info(i))

        for i in self.classes:
            self.parse_class_info(i)

        for i in self.structs:
            self.parse_struct_info(i)

        for i in self.typedefs:
            self.parse_typedef_info(i)

        for i in self.enums:
            self.parse_enum_info(i)




"""
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
"""











