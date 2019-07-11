import os
import re
import time
from collections import OrderedDict
class GetEnumMember(object):
    #attrib: EncFunc
    #file : ...\Source\media\media_embargo\windows\common\codec\ddi\d3d9\dxvaencode_lh.h
    #typedef enum tagENCODE_FUNC
    #{
    #    ENCODE_ENC          = 0x0001,
    #    ENCODE_PAK          = 0x0002,
    #    ENCODE_ENC_PAK      = 0x0004,
    #    ENCODE_HYBRIDPAK    = 0x0008,
    #    ENCODE_WIDI         = 0x8000
    #} ENCODE_FUNC;

    #attrib: RawFormat, ResFormat
    #file : ...\Source\media\media_driver\agnostic\common\os\mos_resource_defs.h
    #typedef enum _MOS_FORMAT
    #{
    #   ...
    #   Format_NV12     ,
    #   ...
    #   Format_Buffer      ,
    #   ...
    #} MOS_FORMAT, *PMOS_FORMAT;
    
    #attrib: RawTileType, ResTileType
    #file : ...\Source\media\media_driver\agnostic\common\os\mos_resource_defs.h
    #typedef enum _MOS_TILE_TYPE
    #{
    #    MOS_TILE_X,
    #    MOS_TILE_Y,
    #    MOS_TILE_YF,            // 4KB tile
    #    MOS_TILE_YS,            // 64KB tile
    #    MOS_TILE_LINEAR,
    #    MOS_TILE_INVALID
    #} MOS_TILE_TYPE;

    def __init__(self, base_media_path):
        self.base_media_path = base_media_path
        self.targetfiles = [r'media\media_embargo\windows\common\codec\ddi\d3d9\dxvaencode_lh.h',
                           r'media\media_driver\agnostic\common\os\mos_resource_defs.h']
        self.enumname = {'dxvaencode_lh.h' : ['tagENCODE_FUNC'], 
                         'mos_resource_defs.h' : ['_MOS_FORMAT', '_MOS_TILE_TYPE']}
        self.output = {} #{'tagENCODE_FUNC':{'ENCODE_ENC':1,...}, '_MOS_FORMAT':{...}}

    def read_files(self):
        py = '^([a-zA-Z_0-9]+)\s*=\s*([\-x0-9]+)*\s*,'  #with value, e.g. 'ENCODE_ENC          = 0x0001,'
        pn = '^([a-zA-Z_0-9]+)\s*,'                        #without value, e.g. 'MOS_TILE_X,'
        pen = '^([a-zA-Z_0-9]+)'                            #The final member, without ','
        pey = '^([a-zA-Z_0-9]+)\s*=\s*([\-x0-9]+)*'                            #The final member with value, without ','
        for file in self.targetfiles:
            self.filename = os.path.basename(file)
            with open(os.path.join(self.base_media_path, file), 'r',  encoding="ISO-8859-1") as fin:
                self.lines = fin.readlines()
            if not self.lines:
                print('Not Found %s' %self.filename)

            start = False
            
            for index, line in enumerate(self.lines):
                line = line.strip()
                if not start and [enum for enum in self.enumname[self.filename] if re.search('^typedef enum %s\s*{?$'% enum, line)]:
                    self.group = re.search('^typedef enum (.*)', line).group(1)
                    enum_dic = OrderedDict()
                    start = True    #find target enum
                    pre_v = -1
                    continue
                if start:
                    ry = re.search(py, line)
                    rn = re.search(pn, line)
                    ren = re.search(pen, line)
                    rey = re.search(pey, line)
                    if ry:
                        if '0x' in ry.group(2):
                            pre_v = int(ry.group(2), 16)
                            enum_dic[ry.group(1)] = pre_v
                        else:
                            pre_v= int(ry.group(2))
                            enum_dic[ry.group(1)] = pre_v
                    elif rn:
                        pre_v += 1
                        enum_dic[rn.group(1)] = pre_v
                    elif rey:
                        start = False
                        if '0x' in rey.group(2):
                            pre_v = int(rey.group(2), 16)
                            enum_dic[rey.group(1)] = pre_v
                        else:
                            pre_v= int(rey.group(2))
                            enum_dic[rey.group(1)] = pre_v
                        self.output[self.group] = enum_dic
                    elif ren:
                        start = False
                        pre_v += 1
                        enum_dic[ren.group(1)] = pre_v
                        self.output[self.group] = enum_dic
        return self.output
 

#obj = GetEnumMember(base_media_path='C:\\Users\\jiny\\gfx\\gfx-driver\\Source')
#obj.read_files()
#print(obj.output)
