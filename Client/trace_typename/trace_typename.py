import sys
import os
import re
import shutil
import copy
from functools import partial
import time


from included_file import Included_Parser


#from Client.ult_generator.header_parser import HeaderParser

#import Included_File
#from header_parser import HeaderParser
#from ult_generator import test_generator
#from ult_generator import test_case_generator
#from ult_generator import xml_generator
#from ult_generator import cpp_parser





def find_includes_file(start_dir,target_includes):
    cur_dir=os.getcwd()
    for r,d,f in os.walk(start_dir):
        #os.chdir(r)
        if(target_includes in f):
            if(not 'linux' in r):
                return r+os.sep
    #print("here is an error")
    return None

def match_var(type_name,file):
    print('{:>20}|{:>20}|{:<}'.format('matching',file.name,file.path))

    for _class in file.class_info:
        if type_name in _class['var_name']:
            #print(os.getcwd())
            with open(os.getcwd()+r'\Client\trace_typename\result.txt','a') as fout:
                fout.write('{:>20}|{:>20}|{:<}\n'.format(type_name,file.name,file.path))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','class_name',_class['class_name']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','is_typedef',_class['is_typedef']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','is_ptr',_class['is_ptr']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','is_refer',_class['is_refer']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','super_class',_class['super_class']))
                fout.write('{:->60}\n'.format(''))
            return True
    for _struct in file.struct_info:
        if type_name in _struct['var_name']:
            with open(os.getcwd()+r'\Client\trace_typename\result.txt','a') as fout:
                fout.write('{:>20}|{:>20}|{:<}\n'.format(type_name,file.name,file.path))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','struct_name',_struct['struct_name']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','is_typedef',_struct['is_typedef']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','is_ptr',_struct['is_ptr']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','is_refer',_struct['is_refer']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','super_sturct',_struct['super_struct']))
                fout.write('{:->60}\n'.format(''))
            return True
    for _enum in file.struct_info:
        if type_name in _enum['var_name']:
            with open(os.getcwd()+r'\Client\trace_typename\result.txt','a') as fout:
                fout.write('{:>20}|{:>20}|{:<}\n'.format(type_name,file.name,file.path))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','enum_name',_enum['enum_name']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','is_typedef',_enum['is_typedef']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','is_ptr',_enum['is_ptr']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','is_refer',_enum['is_refer']))
                fout.write('{:>20}|{:>20}|{:<}\n'.format('','all_nums',','.join([str(i) for i in _enum['all_nums']])))
                fout.write('{:->60}\n'.format(''))
            return True
    return False

def main(input_file=r'C:\work\ult\AutoULTGen\Client\trace_typename\input_2.txt'):
    """

    :param input_file:
    :param media_path:
    :return:
    """
    with open(input_file, 'r') as fin:
        media_path = ''
        for line in fin:
            line = line.strip()
            line=line.split(' ')
            if not line:
                continue
            target_class=line[1]
            line=line[0]
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

            parser_list = [Included_Parser(file_name, file_path,target_class)]
            print(os.getcwd())
            parser_list[0].read_file()
            parser_list[0].parse_file_info()
            #parser_list[0].print_info()


            types=parser_list[0].types_in_ctor
            includes=parser_list[0].includes

            parsed_includes=set()

            while(types):
                all_includes=includes
                if(not parsed_includes.issubset(all_includes)):
                    print("error occured, the parsed_includes has member not in all_includes")
                    return None

                unparsed_includes=list(all_includes-parsed_includes)
                if(len(unparsed_includes)==0):
                    print("there is no include file to parse")
                    return None

                for include in unparsed_includes:
                    file_name=include
                    parsed_includes.add(file_name)
                    file_path=find_includes_file(media_path,file_name)
                    if file_path:
                        print('{:>20}|{:>20}|{:<} '.format('File Found',file_name,file_path))
                        print('{:->20}|{:->20}|{:->20}'.format('', '', ''))
                        #print(file_name+" found in "+ file_path)
                        parser_list.append(Included_Parser(file_name,file_path))
                        parser_list[-1].read_file()
                        parser_list[-1].parse_file_info()
                        #parser_list[-1].print_info()
                        all_includes.update((parser_list[-1].includes))
                        #print('{:->15}|{:->19}|{:->20}'.format('', '', ''))
                        if parser_list[-1].var_name:
                            intersection=set(types)&parser_list[-1].var_name
                            for i in intersection:
                                if(match_var(i,parser_list[-1])):
                                    types.pop()
                    else :
                        print('{:>20}|{:>20}|{:->20}'.format('NOT Found',file_name,''))
                        continue


if __name__ == '__main__':
    time_start=time.time()
    input_file=os.getcwd()+r'\Client\trace_typename\input_2.txt'
    os.remove(os.getcwd()+r'\Client\trace_typename\result.txt')
    main(input_file)
    time_end=time.time()
    print('totally cost',time_end-time_start)

