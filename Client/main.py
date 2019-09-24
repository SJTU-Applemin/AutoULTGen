import sys
import os
import re
import shutil
import copy
from functools import partial
import time

from ult_generator import header_parser
from ult_generator import test_generator
from ult_generator import test_case_generator
from ult_generator import xml_generator
from ult_generator import cpp_parser
import re
import os

# PLATFORMS = {'G12': 'gen12', 'common':'common'}
# COMPONENTS = {'encode'}
#
#
# def find_class_file(class_name, start_path='../../Source/media/media_embargo/media_driver_next/agnostic'):
#     pattern = "[A-Z]"
#     class_name = re.sub(pattern, lambda x: " " + x.group(0), class_name)
#     name_split = class_name.strip().split(' ')
#     platform = 'common'
#     for word in name_split:
#         if word in PLATFORMS:
#             platform = word
#             break

def finddir(startdir, target, root_path):
    try:
        # startdir = startdir.replace('/', '\\')
        os.chdir(startdir)
    except:
        # print('startdir err')
        # print(startdir)
        return None
    for new_dir in os.listdir(os.curdir):
        #print(new_dir)
        if new_dir == target:
            result = os.getcwd() + os.sep + new_dir
            #print(result)
            #os.chdir(root_path)
            return result
        if os.path.isdir(new_dir):
            result = finddir(new_dir, target, root_path)
            if result:
                return result
            os.chdir(os.pardir)
    return None


def find_super_class_file(class_name, includes, media_path):
    #print(includes)
    t1 = class_name.lower()
    t1 = t1.replace('pkt', 'packet')
    file_name = ''
    for i in includes:
        t2 = i[:-2].replace('_', '')
        # print(t1)
        # print(t2)
        if t2.find(t1) != -1:
            file_name = i
            break
    if file_name:
        #print(file_name)
        return finddir(media_path, file_name, os.getcwd())
    else:
        return None

def main(input_file=os.getcwd()+r'\Client\input.txt'):
    """

    :param input_file:
    :param media_path:
    :return:
    """
    with open(input_file, 'r') as fin:
        media_path = ''
        for line in fin:
            line = line.strip()
            if not line:
                continue
            idx = line.find('MediaPath:')
            if idx != -1:
                media_path = line[idx+11:]

            idx = line.rfind('\\')
            file_name = line[idx+1:]
            file_path = line[:idx+1]
            cpp_file_name = file_name[:(file_name.find('.h'))] + '.cpp'
            if not media_path:
                idx = file_path.find('\\gfx-driver\\Source\\media')
                if idx != -1:
                    media_path = line[:idx+1]+'gfx-driver\\Source\\media'
                else:
                    print('Error, Please input a correct media path such as MediaPath: xxxx')

            parser_list = [header_parser.HeaderParser(file_name, file_path)]
            print(os.getcwd())
            parser_list[0].read_file()
            parser_list[0].parse_file_info()
            parser_list[0].print_info()

            #while True:
            root_path = os.getcwd()
            for cur_class in parser_list[-1].classes:
                if not cur_class['super_class']:
                    continue#break
                print(cur_class['super_class'])
                s = find_super_class_file(cur_class['super_class'],parser_list[-1].includes, media_path)
                print(s)
                os.chdir(root_path)
                if s:
                    idx = s.rfind('\\')
                    cur_file_name = s[idx + 1:]
                    cur_file_path = s[:idx + 1]
                    parser_list.append(header_parser.HeaderParser(cur_file_name, cur_file_path))
                    parser_list[-1].read_file()
                    parser_list[-1].parse_file_info()
                else:
                    break
                #if not parser_list[-1].super_class:
                #    break
                #print(parser_list[-1].super_class)
                #s = find_super_class_file(parser_list[-1].super_class, parser_list[-1].includes, media_path)
                #print(s)
                #os.chdir(root_path)
                #if s:
                #    idx = s.rfind('/')
                #    file_name = s[idx + 1:]
                #    file_path = s[:idx + 1]
                #    parser_list.append(header_parser.HeaderParser(file_name, file_path))
                #    parser_list[-1].read_file()
                #    parser_list[-1].parse_file_info()
                #else:
                #    break
            print('------------------------')
            for super_list in parser_list[1:]:
                for sp_class in super_list.classes:
                    for sp_m in sp_class['methods_info']:
                        if sp_m['method_name'].startswith('~'):
                            continue
                        for cur_class in parser_list[0].classes:
                            f_override = False
                            for cur_m in cur_class['methods_info']:
                                if cur_m['method_name'] == sp_m['method_name']:
                                    f_override = True
                                    cur_m['override'] = True
                                    break
                            if not f_override:
                                cur_class['methods_info'].append(sp_m)
            #for i in parser_list[1:]:
            #    # print(i.name)
            #    # print(i.methods_info)
            #    for m in i.methods_info:
            #        f_override = False
            #        if m['method_name'].startswith('~'):
            #            continue
            #        for j in parser_list[0].methods_info:
            #            if m['method_name'] == j['method_name']:
            #                f_override = True
            #                break
            #        if not f_override:
            #            parser_list[0].method
            #            s_info.append(m)
            #    # parser_list[0].methods_info.extend(i.methods_info)

            cpp_parser_list = [cpp_parser.CppParser(cpp_file_name, file_path)]
            cpp_parser_list[0].read_file()

            test = test_generator.TestGenerator(parser_list[0], cpp_parser_list[0], None)
            test_case = test_case_generator.TestCaseGenerator(parser_list[0])
            xml_filename = parser_list[0].name[:-2] + '_header.xml'

            if os.path.exists(xml_filename):
                includes = xml_generator.read_header_xml(parser_list[0])
                if len(includes['test_h']) != 0 :
                    tmpList = list(set(includes['test_h']).difference(set(test.includes_h)))
                    if len(tmpList) != 0:
                        test.includes_h.extend(tempList)

                if len(includes['test_cpp']) != 0:
                   tmpList = list(set(includes['test_cpp']).difference(set(test.includes_cpp)))
                   #tmpList = set(includes['test_cpp']).difference(set(test.includes_cpp))
                   if len(tmpList) != 0:
                       for tmp in tmpList:
                           test.includes_cpp.add(tmp)
                       #test.includes_cpp.add(tmpList)

                if len(includes['test_case_h']) != 0:
                    tmpList = list(set(includes['test_case_h']).difference(set(test_case.includes_h)))
                    if len(tmpList) != 0:
                       test_case.includes_h.extend(tmpList)

                if len(includes['test_case_cpp']) != 0:
                    tmpList = list(set(includes['test_case_cpp']).difference(set(test_case.includes_cpp)))
                    if len(tmpList) != 0:
                       test_case.includes_cpp.extend(tempList)

            else:
                includes = {'test_h': test.includes_h, 'test_cpp': test.includes_cpp,
                            'test_case_h': test_case.includes_h, 'test_case_cpp': test_case.includes_cpp}
                xml_generator.generate_header_xml(parser_list[0], includes)

            test.generate()
            test_case.generate()


if __name__ == '__main__':
    main()
