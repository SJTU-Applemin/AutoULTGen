import os
import shutil
from htoxml.Parser.header_parser import HeaderParser
import pandas as pd
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import (
    Element, SubElement, XML, Comment
)
from ElementTree_pretty import prettify
import re
import copy
import time


class CmdFinder(object):
    def __init__(self, source, gen, ringpath, Buf = None):
        self.source = source
        self.gen = gen
        self.ringpath = ringpath
        self.ringfilename = ''
        self.ringfilelist = []
        #
        self.ringcmdset = set()
        self.ringcmdmodify = {}
        self.df_dic = {}
        self.full_ringinfo = {}   # {'0':[{'MI_LOAD_REGISTER_IMM': ['1108101d', '00000244']},...]} , '0' is frame_no
        #self.same = [['_ON_OFF','_CHECK'],['VEB','VEBOX'],['COST','COSTS'],['QMS','QM'],['IMAGE','IMG'],['WEIGHTSOFFSETS','WEIGHTS_OFFSETS'], ['CMD_HCP_VP9_RDOQ_STATE', 'HEVC_VP9_RDOQ_STATE_CMD']]
        self.same = [['_ON_OFF','_CHECK'],['VEB','VEBOX'],['COST','COSTS'],['QMS','QM'],['IMAGE','IMG'],['WEIGHTSOFFSETS','WEIGHTS_OFFSETS']]
        self.ignored = ['CMD', 'COMMAND', 'OBJECT', 'MEDIA', 'STATE']
        self.classpath = ['ats', 'tglhp', 'x']
        self.TestName = Element('TestName')  #create TestName as result root node
        self.filter = ['mi', 'hcp']
        self.Frame_Num = 0
        if Buf:
            self.Buf = Buf
        else:
            self.Buf = Element('Buf')
        

    def xmlbuf(self):
         # use for Test, search buf is in h2xml part
        # save all xml info into self.buf
        # if create xml seperately for each h
        for r,d,f in os.walk(self.source):
            #filter test folder
            if r'\ult\agnostic\test' not in r:
                continue
            os.chdir(r)
            for thing in f:
                # find required cmd in xml file
                if [i for i in self.classpath if i in thing] :
                    if thing.startswith('mhw_') and thing.endswith('.h.xml'):
                        if  self.gen == 'all' or self.gen != 'all' and str(self.gen) in thing:
                            tree = ET.parse(thing)
                            root = tree.getroot()
                            self.Buf.append(copy.deepcopy(root))
        #print(prettify(self.Buf))

    def writexml(self, output_path = '', index = 0):
        #output xml
        platform_group = SubElement(self.TestName, 'Platform', {'name': ''})
        # full_ringinfo: {'0':[{'MI_LOAD_REGISTER_IMM': ['1108101d', '00000244']},...]} , '0' is frame_no
        for frame_no, ringinfo in self.full_ringinfo.items():
            frame_group = SubElement(platform_group, 'Frame', {'NO': frame_no})
            for pair in ringinfo:
                for ringcmd, value_list in pair.items():
                    if not self.memory(self.TestName, ringcmd, value_list, frame_group, index):
                        # cal time
                        start1 = time.clock()
                        frame_group = self.mapcmd(ringcmd, value_list, frame_group, index)
                        #print("MAP Time used:", time.clock() - start1, ",  index = ", index)
                    index += 1
        if output_path :
            with open( os.path.join(output_path ,  "mapringinfo.xml") , "w") as f:
                f.write(prettify(self.TestName))
        else:
            with open( os.path.join(self.ringpath ,  "mapringinfo.xml") , "w") as f:
                f.write(prettify(self.TestName))
        return prettify(self.TestName)
    
    def modifyringcmd(self, wrong, right):
        #print(self.ringcmdset)
        self.ringcmdset.remove(wrong)
        self.ringcmdset.add(right)
        self.ringcmdmodify[wrong] = right

    def undate_full_ringinfo(self):
        # full_ringinfo: {'0':[{'MI_LOAD_REGISTER_IMM': ['1108101d', '00000244']},...]} , '0' is frame_no
        new_full_ringinfo = {}
        for frame_no, ringinfo in self.full_ringinfo.items():
            new_ringinfo = []
            for pair in ringinfo:
                for ringcmd, value_list in pair.items():
                    if ringcmd in self.ringcmdmodify:
                        new_ringinfo.append({self.ringcmdmodify[ringcmd] : value_list})
                    else:
                        new_ringinfo.append(pair)
            new_full_ringinfo[frame_no] = new_ringinfo

        self.full_ringinfo = new_full_ringinfo
        return new_full_ringinfo

    def updatexml(self, index = 0):
        TestName = self.TestName
        self.TestName = Element('TestName') # clear
        #output xml
        platform_group = SubElement(self.TestName, 'Platform', {'name': ''})
        # full_ringinfo: {'0':[{'MI_LOAD_REGISTER_IMM': ['1108101d', '00000244']},...]} , '0' is frame_no
        for frame_no, ringinfo in self.full_ringinfo.items():
            frame_group = SubElement(platform_group, 'Frame', {'NO': frame_no})
            for pair in ringinfo:
                for ringcmd, value_list in pair.items():
                    if not self.memory(TestName, ringcmd, value_list, frame_group, index):
                        # cal time
                        start1 = time.clock()
                        frame_group = self.mapcmd(ringcmd, value_list, frame_group, index)
                        #print("MAP Time used:", time.clock() - start1, ",  index = ", index)
                    index += 1

        with open( os.path.join(self.ringpath ,  "mapringinfo.xml") , "w") as f:
            f.write(prettify(self.TestName))
        return prettify(self.TestName)



    
    def setbitfield(self, current_group, fieldname, bit_value, bit_l, bit_h, dw_no, check = ''):
        #set bitfield attributes
        bitfield_group = SubElement(current_group, fieldname, {'default_value': bit_value, 
                                                                        'min_value': bit_value,
                                                                        'max_value': bit_value,
                                                                        'bitfield_l': bit_l,
                                                                        'bitfield_h': bit_h})   #set hex value , which represents defalt value of a bitfield
        
        if 'address' in fieldname.lower() and int(bit_h) - int(bit_l) > 16:
            bitfield_group.set('Address', 'Y')
            bitfield_group.set('CHECK', 'N')
        elif 'Reserved' in fieldname :
            bitfield_group.set('Address', 'N')
            bitfield_group.set('CHECK', 'N')
        #elif dw_no == '0':
        #    bitfield_group.set('CHECK', 'Y')
        else:
            bitfield_group.set('Address', 'N')
            bitfield_group.set('CHECK', 'Y')
        if check:
            bitfield_group.set('CHECK', check)
        return current_group

    def memory(self, Element, ringcmd, value_list, node, index):
        #check if ringcmd exists in current testname
        #if so, copy directly to save search time
        binv_list = [ bin(int(i, 16))[2:].zfill(32) for i in value_list ]
        input_dwsize = len(value_list)
        #print(ringcmd + '\n')
        #xpath = ".//CMD[@name='%s']" % ringcmd
        #print(xpath)
        #cmd = self.TestName.find(xpath)
        #cmd = self.TestName.find(".//CMD[@name='MI_FORCE_WAKEUP']")
        start2 = time.clock()
        for cmd in Element.findall(".//CMD"):
            if self.searchkword(ringcmd, cmd.attrib['name']):
                dupe = copy.deepcopy(cmd)
                dupe.attrib['input_dwsize'] = str(input_dwsize)
                dupe.attrib['index'] = str(index)

                for dword_group in dupe.findall("dword"):
                    if 'unmappedstr' not in dword_group.attrib:
                        dw_no = dword_group.attrib['NO']
                        val_str = self.findval(value_list, dw_no)['val_str']
                        dword_group.attrib['value'] = val_str
                    else:
                        #delete previous unmapped str
                        dupe.remove(dword_group)

                    for field in dword_group.findall(".//*[@bitfield_h]"):
                        fieldname, bit_l, bit_h = field.tag, field.attrib['bitfield_l'], field.attrib['bitfield_h']
                        bit_value = self.findbitval(binv_list, list((bit_l, bit_h)), dw_no)[0]
                        field.attrib['default_value'] = bit_value
                        field.attrib['max_value'] = bit_value
                        field.attrib['min_value'] = bit_value
                dupe= self.unmapdw( dupe, dw_no, value_list)
                node.append(dupe) #insert the new node
                #print("Search saved xml Time used:", time.clock() - start2)
                return True
        else:
            return False

    def mapcmd(self, ringcmd, value_list, node, index):
        # map each ringcmd
        # para ringcmd: in ringcmdinfo cmd stringcmd, e.g.  "CMD_SFC_STATE_OBJECT"
        # para value_list: hex stringcmd stream split in list,  eg. ['75010020', '00000041', '00ff00ff', '00000005', '00080350', '00ff00ff', '00000000', '00ff00ff', '00ff00ff', '00000000', '00000000', '00000000', '00000000', '000003ff', '00020000', '00020000', '00000000', '00f10000', '00000001', '00000000', '00e6b000', '00000001', '0000000e', '001b5000', '00000001', '0000000e', '00000000', '00000000', '00000000', '50000ffb', '00000000', '00000000', '00000000', '00000000']

        # return xml tree which map ringcmdinfo value in cmd struct definition
    

        binv_list = [ bin(int(i, 16))[2:].zfill(32) for i in value_list ]   #each dword length = 32 bits(include leading 0)
        
        #for platform in self.classpath:
        #    for r,d,f in os.walk(self.source):
        #        #filter test folder
        #        if r'\ult\agnostic\test' not in r:
        #            continue
        #        os.chdir(r)
        #        for thing in f:
        #            # find required cmd in xml file
        #            if [i for i in self.filter if i not in ringcmd.lower() or i in ringcmd.lower() and i in thing] :
        #                if thing.startswith('mhw_') and thing.endswith('.h.xml') and platform in thing:
        #                    if  self.gen == 'all' or self.gen != 'all' and str(self.gen) in thing:
                                #tree = ET.parse(thing)
                                #root = tree.getroot()
        for platform in self.classpath:
            for Class in self.Buf.findall('./content/class'):
                if 'name' in Class.attrib and platform in Class.attrib['name'].lower() and [i for i in self.filter if i not in ringcmd.lower() or i in ringcmd.lower() and i in Class.attrib['name'].lower()]:
                                #for Class in root.findall('class'):
                                    for structcmd in Class.iter('struct'):
                                        # search cmd in all the local files
                                        if 'name' in structcmd.attrib and self.searchkword(ringcmd, structcmd.attrib['name']):
                                            #Class_group = SubElement(ringcmd_group, 'class', {'name' : Class.attrib['name']})  #debug
                                            input_dwsize = len(value_list)
                                            structcmd_group = SubElement(node, 'CMD',  {'name' : structcmd.attrib['name'],
                                                                                        'class' : Class.attrib['name'],
                                                                                        'index' : str(index),
                                                                                        'input_dwsize' : str(input_dwsize)})
                                            dw_len = 0
                                            dw_no = ''
                                            for unionorcmd in structcmd.findall("./"):  #select all the direct children

                                                if unionorcmd.tag == 'union' and 'name' in unionorcmd.attrib and 'DW' in unionorcmd.attrib['name']:
                                                    dw_no = unionorcmd.attrib['name'].strip('DW')
                                                    val_str = self.findval(value_list, dw_no)['val_str']
                                                    dword_group = SubElement(structcmd_group, 'dword', {'NO' : dw_no,
                                                                                                        'value': val_str})
                                                    current_group = dword_group
                                                    for s in unionorcmd.findall('struct'):
                                                        # 1 dword has several objs
                                                        if 'name' in s.attrib:
                                                            obj_group = SubElement(current_group, s.attrib['name'], {'value': val_str})
                                                            current_group = obj_group
                                                        for elem in s.findall("./"):
                                                            if 'name' in elem.attrib:
                                                                fieldname = elem.attrib['name']
                                                                if 'bitfield' in elem.attrib :
                                                                    bit_item = elem.attrib['bitfield'].split(',')  #bitfield="0,  5"
                                                                else:
                                                                    bit_item = []
                                                                bit_value, bit_l, bit_h = self.findbitval(binv_list, bit_item, dw_no)
                                                                if structcmd_group.attrib['name'] == 'MI_NOOP_CMD':
                                                                    current_group = self.setbitfield(current_group, fieldname, bit_value, bit_l, bit_h, dw_no, 'N')
                                                                else:
                                                                    current_group = self.setbitfield(current_group, fieldname, bit_value, bit_l, bit_h, dw_no)

                                                                #complement undefined dword length, for unmapped buffer stream
                                                                if fieldname == "DwordLength":
                                                                    dw_len = int(bit_value,16) 
                                                                    structcmd_group.set('DW0_dwlen', str(dw_len))

                                                        current_group = dword_group
                                                if unionorcmd.tag == 'otherCMD' and 'otherCMD' in unionorcmd.attrib:
                                                    if 'arraysize' in unionorcmd.attrib:
                                                        structcmd_group, dw_no = self.findcmd(structcmd_group, unionorcmd.attrib['otherCMD'], value_list, dw_no, unionorcmd.attrib['arraysize'])
                                                    else:
                                                        structcmd_group, dw_no = self.findcmd(structcmd_group, unionorcmd.attrib['otherCMD'], value_list, dw_no)

                                                if unionorcmd.tag != 'otherCMD' and 'arraysize' in unionorcmd.attrib:
                                                    #filter the same layer containing 'arraysize' attrib with union or othercmd, not including those within union
                                                    asize = unionorcmd.attrib['arraysize']
                                                    if '_' in dw_no:
                                                        pre_dw = int(dw_no.split('_')[1].strip())
                                                    else:
                                                        pre_dw = int(dw_no)
                                                    #dtype: uint8_t, uint16_t, ...
                                                    if re.search('uint\d+_t', unionorcmd.tag):
                                                        uint = int(re.search('\d+', unionorcmd.tag)[0])
                                                    dw_end = pre_dw + int(int(asize)*uint/32)

                                                    for i in range(pre_dw+1, dw_end+1):
                                                        val_str = self.findval(value_list, str(i))['val_str']
                                                        dword_group = SubElement(structcmd_group, 'dword', {'NO' : str(i),
                                                                                                            'value' : val_str,
                                                                                                            'arrayname': unionorcmd.attrib['name'],
                                                                                                            'dtype': unionorcmd.tag})
                                                    dw_no = str(dw_end)

                                                #read defined dwsize if existed
                                                if 'name' in unionorcmd.attrib and unionorcmd.attrib['name'] == 'dwSize':
                                                    defined_dwSize = unionorcmd.attrib['value']
                                                    structcmd_group.set('def_dwSize', defined_dwSize)

                                            #print(prettify(Result))
                                            #break
                                        
                                            
                                            structcmd_group = self.unmapdw( structcmd_group, dw_no, value_list)
                                                #compare defined dwSize with real dwSize
                                                #sub1 = abs(int(defined_dwSize) - dw_len)
                                                #if sub1 != 1 and sub1 != 2:
                                                #    structcmd_group.set('dwSizeEqual', 'False')

                                            structcmd_group = self.checkdw(structcmd_group, value_list)


                                            return node



        #cmd not found in local file
        ringcmd_group = SubElement(node, 'ringcmd', {'name' : ringcmd, 
                                                     'class' : 'not found',
                                                     'index' : str(index)})
        print(ringcmd + ' not found')
        return node

    def checkdw(self, node, value_list):
        #check if any dword loses or duplicates
        lost_list = []
        dupe_list = []
        current_list = []
        for dw_g in node.findall("dword"):
            no = dw_g.attrib['NO']
            if '_' in no:
                dw_l = int(no.split('_')[0])
                dw_h = int(no.split('_')[1])
                for i in range(dw_l, dw_h+1):
                    current_list.append(i)
            else:
                current_list.append(int(no))
        max_dw = max(current_list)
        seen = {}
        for x in current_list:
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    dupe_list.append(str(x))
                seen[x] += 1
        for i in range(max_dw+1):
            if i not in current_list:
                lost_list.append(str(i))

        if lost_list:
            node.set('Lost_dw', ','.join(lost_list))
        if dupe_list:
            node.set('Dupe_dw', ','.join(dupe_list))
        return node

    def unmapdw(self, node, dw_no, value_list):
        #check if all the input dw has been mapped into dw
        dw_len = len(value_list)
        if '_' in dw_no:
            dw_end = int(dw_no.split('_')[-1])
        else:
            dw_end = int(dw_no)
        if dw_end < dw_len-1:
            for i in range(dw_end+1, dw_len):
                val_str = self.findval(value_list, str(i))['val_str']
                dword_group = SubElement(node, 'dword', {'NO' : str(i),
                                                         'unmappedstr' : val_str})
        return node

    def findcmd(self, node, cmd, value_list, base_dw_no, arraysize = ''):
        # find cmd according to name, append to node
        binv_list = [ bin(int(i, 16))[2:].zfill(32) for i in value_list ]   #each dword length = 32 bits(include leading 0)
        #for platform in self.classpath:
        #    for r,d,f in os.walk(self.source):
        #        #filter test folder
        #        if r'\ult\agnostic\test' not in r:
        #            continue
        #        os.chdir(r)
        #        for thing in f:
        #            # find required cmd in xml file
        #            if [i for i in self.filter if i not in ringcmd.lower() or i in ringcmd.lower() and i in thing] :
        #                if thing.startswith('mhw_') and thing.endswith('.h.xml') and platform in thing:
        #                    if  self.gen == 'all' or self.gen != 'all' and str(self.gen) in thing:
        #                        tree = ET.parse(thing)
        #                        root = tree.getroot()
        #                        for Class in root.findall('class'):
        for platform in self.classpath:
            for Class in self.Buf.findall('./content/class'):
                if 'name' in Class.attrib and platform in Class.attrib['name'].lower() and [i for i in self.filter if i not in cmd.lower() or i in cmd.lower() and i in Class.attrib['name'].lower()]:
                                    for structcmd in Class.iter('struct'):
                                        # search cmd in all the local files
                                        if 'name' in structcmd.attrib and structcmd.attrib['name'] == cmd:
                            
                                            dw_len = 0
                                            dw_no = base_dw_no
                                            #define iteration times according to cmd arraysize
                                            if not arraysize:
                                                times = 1
                                            else:
                                                times = int(arraysize)

                                            for i in range(times):
                                                for unionorcmd in structcmd.findall("./"):  #select all the direct children
                                        
                                                    if unionorcmd.tag == 'union' and 'name' in unionorcmd.attrib and 'DW' in unionorcmd.attrib['name']:
                                                        dword_group = SubElement(node, 'dword', {'otherCMD': cmd,
                                                                                                 'class' : Class.attrib['name']})
                                                        if arraysize:
                                                            dword_group.set('cmdarraysize', arraysize)
                                                            dword_group.set('arrayNO', str(i))
                                                        dw_no = unionorcmd.attrib['name'].strip('DW')
                                                        dic = self.findval(value_list, dw_no, base_dw_no)
                                                        dw_no = dic['dw_no_new']
                                                        dword_group.set('NO' , dw_no)
                                                        dword_group.set('value', dic['val_str'])
                                                        #dword_group = SubElement(structcmd_group, 'dword', {'NO' : dw_no,
                                                        #                                                    'value': val_str})
                                                        current_group = dword_group
                                                        for s in unionorcmd.findall('struct'):
                                                            # 1 dword has several objs
                                                            if 'name' in s.attrib:
                                                                obj_group = SubElement(current_group, s.attrib['name'], {'value': val_str})
                                                                current_group = obj_group
                                                            for elem in s.findall("./"):
                                                                if 'name' in elem.attrib:
                                                                    fieldname = elem.attrib['name']
                                                                    if 'bitfield' in elem.attrib :
                                                                        bit_item = elem.attrib['bitfield'].split(',')  #bitfield="0,  5"
                                                                    else:
                                                                        bit_item = []
                                                                    bit_value, bit_l, bit_h = self.findbitval(binv_list, bit_item, dw_no)
                                                                    if structcmd.attrib['name'] == 'MI_NOOP_CMD':
                                                                        current_group = self.setbitfield(current_group, fieldname, bit_value, bit_l, bit_h, dw_no, 'N')
                                                                    else:
                                                                        current_group = self.setbitfield(current_group, fieldname, bit_value, bit_l, bit_h, dw_no)


                                                                    #complement undefined dword length, for unmapped buffer stream
                                                            current_group = dword_group
                                                    if unionorcmd.tag == 'otherCMD' and 'otherCMD' in unionorcmd.attrib:
                                                        node, dw_no = self.findcmd(node, unionorcmd.attrib['otherCMD'], value_list, dw_no)
                                                base_dw_no = dw_no

                                            return node, dw_no
        #cmd not found in local file
        dword_group = SubElement(node, 'dword', {'otherCMD': cmd,
                                                 'class' : 'not found'})
        return node, base_dw_no

    def extractfull(self):
            # full_ringinfo : {'0':[{'MI_LOAD_REGISTER_IMM': ['1108101d', '00000244']},...]} , '0' is frame_no
            # extract full info from ringinfo text files
            for r,d,f in os.walk(self.ringpath):
                os.chdir(r)
                file_list = [file for file in f if re.search('VcsRingInfo_0_0.txt', file)]
                if len(file_list) > 1:
                    frame_no_list = [int(re.search('(\d)-VcsRingInfo_0_0.txt', file).group(1)) for file in file_list]
                elif len(file_list) == 1:
                    frame_no_list = [0]
            self.ringfilelist = file_list
            numset = set(frame_no_list)
            self.Frame_Num = len(numset)
            self.num_diff = min(numset)

            for thing in self.ringfilelist:
                if self.Frame_Num > 1:
                    frame_no = str(int(re.search('(\d)-VcsRingInfo_0_0.txt', thing).group(1)) - self.num_diff)
                elif self.Frame_Num == 1:
                    frame_no = '0'
                self.ringfilename = thing
                self.txt2df()
                self.extractdf(frame_no)
            

    def extractdf(self, frame_no, dfname = 'all'):
        #dfname options:
        #           'all': search in all the dfs
        #           'ContextRestore': search in ContextRestore portion
        #           'Workload': search in Workload portion
    
        #full_ringinfo : {'0':[{'MI_LOAD_REGISTER_IMM': ['1108101d', '00000244']},...]} , '0' is frame_no
    
        df = self.df_dic[dfname]
        ringinfo = [] #stores single file ringinfo
        for i in df.index:
            #ringcmd = []
            self.ringcmdset.add(df.loc[i,"Description"]) 
            ringinfo.append({df.loc[i,"Description"]:[x for x in df.loc[i,"Header":].values.tolist() if str(x) != 'nan']}) 
        self.full_ringinfo[frame_no] = ringinfo
            #ringcmd.append([x for x in df.loc[i,"Header":].values.tolist() if str(x) != 'nan'])
            #full_ringinfo.append(ringcmd)
        return self.full_ringinfo, self.ringcmdset

    def txt2df(self):
        #read ringcmdtringcmd text file into pd dataframe, which cmd stringcmd can be easily extracted
        ## only start after cmd "MI_BATCH_BUFFER_START"
        os.chdir(self.ringpath)
        comment_char = ['<', '-']
        with open(self.ringfilename, 'r') as f:
            df = pd.DataFrame()         #initialize
            start = 'MI_BATCH_BUFFER_START'

            start_fg = False

            for index, line in enumerate(f):

                # find header:
                if 'Count' in line:
                    columns = line.strip('-').split()  
                #elif '<ContextRestore' in line:
                #    c_start = in

                # skip the commented lines
                
                elif line[0] in comment_char:
                    continue

                elif start_fg: 
                    df = pd.concat( [df, pd.DataFrame([tuple(line.strip().split())])], ignore_index=True )

                elif not start_fg and start in line:
                    start_fg = True
                
        # 
        last_col = int(columns[-1]) #last dword num
        tar_last_col = len(df.columns) - len(columns) + last_col
        if tar_last_col > last_col:
            columns.extend( [str(i) for i in range(last_col+1,  tar_last_col+1)])
            df.columns = columns
        
        # df = df.iloc[0:0] #clear dataframe memory
        # df.loc[2] #select one column
        # df.loc[:,'Descriptiono'] #select one row

        #print(df)
        #df_dic = {'ContextRestore': df}
        self.df_dic = {'all':df}
        return self.df_dic

    def h2xml(self):
        #convert header to xml
        #use header_parser tool
        
        parser_list = []
        for r,d,f in os.walk(self.source):
            #modify target file
            #if r'\ult\agnostic\test' not in r:
            if r'\ult\agnostic\test' in r:
                continue
            for thing in f:
                # filter all mhw cmd header file
                #if thing.startswith('mhw_') and re.search('g\d', thing) and thing.endswith('.h'):
                if self.gen != 'all':
                    if thing.startswith('mhw_') and re.search(f'g{self.gen}', thing) and thing.endswith('.h'):
                        parser_list.append(HeaderParser(thing, r))
                else:
                    if thing.startswith('mhw_') and thing.endswith('.h'):
                        parser_list.append(HeaderParser(thing, r))

        for item in parser_list:
            item.read_file()
            #Do not create xml file for each h file, instead save in buf str
            #item.write_xml()
            root = ET.fromstring(item.parse_file_info())
            self.Buf.append(copy.deepcopy(root))
        return self.Buf

    def findbitval(self, binv_list, bit_item, dw_no, base_dw_no = ''):
        # for otherCMD inside struct cmd, has base_dw_no
        if base_dw_no:
            if '_' in base_dw_no:
                bd = int(base_dw_no.split('_')[1].strip())+1
            else:
                bd = int(base_dw_no)+1
        else:
            bd = 0
        ##----------------------------------------
        if '_' in dw_no:
            dw_no_l = int(dw_no.split('_')[0].strip()) + bd 
            dw_no_h = int(dw_no.split('_')[1].strip()) + bd
        else:
            dw_no_l = int(dw_no) + bd
            dw_no_h = int(dw_no) + bd

        if bit_item:
            #find defalt hex value by field index
            bit_l = int(bit_item[0].strip())
            bit_h = int(bit_item[1].strip())
        else:
            #not have bit attrib
            bit_l = 0
            bit_h = (dw_no_h - dw_no_l + 1)*32 - 1

        if bit_l == 0:
            bit_value_raw =  ''.join(binv_list[dw_no_l: dw_no_h+1])[-bit_h-1 : ]
        else:
            bit_value_raw =  ''.join(binv_list[dw_no_l: dw_no_h+1])[-bit_h-1 : -bit_l]

        if bit_value_raw:
            bit_value = hex(int(bit_value_raw, 2))
        # nothing
        else:
            bit_value = ''

        return bit_value, str(bit_l), str(bit_h)

    def findval(self, value_list, dw_no, base_dw_no = ''):
        # for otherCMD inside struct cmd, has base_dw_no
        if base_dw_no:
            if '_' in base_dw_no:
                bd = int(base_dw_no.split('_')[1].strip()) + 1
            else:
                bd = int(base_dw_no) + 1
        else:
            bd = 0
        ##----------------------------------------
        if '_' in dw_no:
            dw_no_l = int(dw_no.split('_')[0].strip()) + bd
            dw_no_h = int(dw_no.split('_')[1].strip()) + bd
            dw_no_new = str(dw_no_l) + '_' + str(dw_no_h)
        else:
            dw_no_l = int(dw_no) + bd
            dw_no_h = int(dw_no) + bd
            dw_no_new = str(dw_no_h)
        val_str =  ''.join(value_list[dw_no_l: dw_no_h+1])
        if [i for i in val_str if i != '0']:
            val_str = '0x'+val_str
        # all '0'
        elif re.search('^0+$', val_str):
            val_str = '0x0'

        return dict(val_str = val_str, dw_no_new = dw_no_new)

    def searchkword(self, ringcmd, localcmd):
        #ringcmd: in ringcmdinfo "CMD_SFC_STATE_OBJECT"
        #local: in header file "SFC_STATE_CMD"
        #For match purpose
        if self.equal_list(ringcmd, localcmd):
            return True
        else:
            for l in self.same:
                for index, item in enumerate(l):
                    if item in ringcmd:
                        ringcmd_new = ringcmd.replace(item, l[len(l)-1-index])
                        return self.equal_list(ringcmd_new, localcmd)
            return False

    def equal_list(self, str1, str2):
        #split str with '_'
        #compare 2 lists after ignoringcmd some keywords
        l1 = str1.split('_')
        l2 = str2.split('_')
        ignored = set(self.ignored)
        for k1 in l1:
            if k1 not in ignored and k1 not in l2:
                return False
        for k2 in l2:
            if k2 not in ignored and k2 not in l1:
                return False
        return True


#----------------------------------------------------------------
#ringpath = r'C:\projects\github\AutoULTGen\cmd_validation\vcstringinfo\HEVC-VDENC-Grits001 - 1947\VcsRingInfo'
#gen = 12
#source = r'C:\Users\jiny\gfx\gfx-driver\Source\media'
#----------------------------------------------------------------

#----------------------------------------------------------------
#init
#start = time.clock()
#obj = CmdFinder(source, gen, ringpath)
#Buf = obj.h2xml()
#obj.extractfull()
#obj.writexml()
#elapsed = (time.clock() - start)
#print("Total Time used:",elapsed)   #25s 
##----------------------------------------------------------------

##----------------------------------------------------------------
## show ringcmd if user want to update cmd
#print(obj.ringcmdset)  #show cmd list
#start = time.clock()
#obj.modifyringcmd('CMD_HCP_VP9_RDOQ_STATE', 'HEVC_VP9_RDOQ_STATE_CMD')
#print(obj.ringcmdset)  #show cmd list
#obj.undate_full_ringinfo()
#obj.updatexml()
#elapsed = (time.clock() - start)
#print("Total Time used:",elapsed)   #13s 
##----------------------------------------------------------------

##----------------------------------------------------------------
##after running once
#start = time.clock()
#obj = CmdFinder(source, gen, ringpath, Buf)
#obj.extractfull()
#obj.writexml()
#elapsed = (time.clock() - start)
#print("Total Time used:", elapsed)   #18s 
#----------------------------------------------------------------
