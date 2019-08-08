import os
import re

def parse_ifconditions(line_dic):
    para_dic={}
    line_clr_dic={}
    # return all the if conditions's parameters that can be set to 1(True)
    for num in line_dic:
        line_clr_dic[num] = line_dic[num].replace(" ", "")   #remove all the spaces
        if line_clr_dic[num].startswith('if('):
            if '=' not in line_clr_dic[num] and '<' not in line_clr_dic[num] and '>' not in line_clr_dic[num]:
                delimiters = "if(", "&&", ")","||","\n"
                regexpattern = '|'.join(map(re.escape, delimiters))
                para1 = re.split(regexpattern, line_clr_dic[num])
                para_list = [x for x in para1 if x]    #filter blank in the list
                para_dic[num] = para_list
    #temperately only parse bool variable
    only_bool_para_dic = filter_bool_type(para_dic, line_clr_dic)
    return only_bool_para_dic


def search_upper(para_dic, line_dic):
    #find each para_list's corresponding namespace and class name, save in the upper_dic with same line_num of para_list
    upper_dic={}
    for num in para_dic:
        upper_line_num = num
        while upper_line_num >= 1:
            if line_dic[upper_line_num].rfind('}') != -1: #exclude{}
                j = upper_line_num
                while j >= 1:
                    if line_dic[j].rfind('{') !=-1:
                        upper_line_num = j-1            #Cannot parse two '{' consecutively
                        break
                    j -=1

            elif line_dic[upper_line_num].rfind('{') !=-1: # find '{' right after class
                j = upper_line_num
                upper_para_str = ''
                while j >= 1:
                    if ')' not in line_dic[j]:  #) represents the end of parameters
                        j -= 1
                        continue
                    else:
                        while j >= 1:
                            if '::' not in line_dic[j]: # :: represents the appearance of namespace and class
                                upper_para_str = line_dic[j] + upper_para_str
                                j -= 1
                                continue
                            else:
                                upper_para_str = line_dic[j] + upper_para_str
                                upper_para_str_clr = line_dic[num].replace(" ", "")
                                upper_para_str = upper_para_str.replace('(', '\n(\n ') #make sure para besides '(' will be split up
                                upper_para_str = upper_para_str.replace(')', '\n)\n ')
                                delimiters = " ","\n","&","*"
                                regexpattern = '|'.join(map(re.escape, delimiters))
                                para1 = re.split(regexpattern, upper_para_str)
                                upper_para_list = [x for x in para1 if x]    #filter blank in the list
                                upper_dic[num]=upper_para_list      #num is same as para_num
                                break
                        break
                break
            upper_line_num -= 1
    return upper_dic

def generate_condition_test(para_dic, upper_dic):
    # return final test file content
    conditions_test_file = []
    indent = '    '
    for num in para_dic:
        upper_num = num
        test_dic = {}
        test_dic['if_condition_para'] = para_dic[num]
        for i in upper_dic[num]:
            if i.find('::') != -1:
                # find namespace and class name
                idx = i.find('::')
                test_dic['namespace'] = i[:idx]
                test_dic['classname'] = i[idx+2:]
                break
        upper_para_begin = upper_dic[num].index('(') + 1
        upper_para_end = upper_dic[num].index(')') 
        test_dic['upper_para_type'] = upper_dic[num][upper_para_begin:upper_para_end:2]
        test_dic['upper_para_name'] = upper_dic[num][upper_para_begin+1:upper_para_end:2]
        test_dic['upper_para_name'] = [w.replace(',', '') for w in test_dic['upper_para_name']]
        conditions_test_file.append( test_dic['classname'] + 'Test()' + '\n{\n')
        for i in test_dic['if_condition_para']:
            conditions_test_file.append( indent + i + ' = 1;\n')
        conditions_test_file.append( indent + test_dic['namespace'] + '::' + test_dic['classname'] + '(' + ', '.join(test_dic['upper_para_name']) + ');\n}\n')
    return conditions_test_file

def filter_bool_type(para_dic, line_clr_dic):
    #return only bool part of para_dic
    only_bool_para_dic = para_dic.copy()
    for num in para_dic:
        for para_name in para_dic[num]:
            for line_num in line_clr_dic:
                # type1: bool para_name
                bool_pass = False
                if line_clr_dic[line_num].find('bool'+para_name) != -1:
                    bool_pass = True
                    break
                # type2: paraname = xxx? true : false; xxx can be a, a.b, a->b
                regex = re.compile(r"(%s)=[a-zA-Z0-9_\.\-\>]*\?true:false;\n" %para_name)
                if regex.match(line_clr_dic[line_num]):
                    bool_pass = True
                    break
            if not bool_pass:
                #delete corresponding para_list
                del only_bool_para_dic[num]
                continue
    return only_bool_para_dic



def main():
    work_dir = [r'C:\\projects\\VPG\gfx-driver\\Source\\media\\media_embargo\\media_driver_next\\agnostic\\common\\vp\\hal']
    file_name = 'vp_render_sfc_base.cpp'
    test_name = 'test.cpp'
    line_dic = {}
    for dir in work_dir:
        completeName = os.path.join(dir, file_name)
        with open(completeName, 'r') as fin:            
            for num, line in enumerate(fin,1):
                line_dic[num] = line
        para_dic = parse_ifconditions(line_dic)
        upper_dic = search_upper(para_dic, line_dic)
        conditions_test_file = generate_condition_test(para_dic, upper_dic)
        with open(os.path.join(dir, test_name), 'w+') as fout:
            fout.writelines(conditions_test_file)

if __name__ == '__main__':
    main()