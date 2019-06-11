import httplib
httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'
import urllib
import urllib2
import os
import time
#from PIL import ImageGrab
import random
import os
s = os.sep
root = 'C:\\Users\\zhijiezh\\Desktop\\intel\\media_driver_next' 
#Only files under os (or subdirs) should be modified; only .h and .c files should be modified.
WFC=[] #Wait For Check

print "ready"
file_number=1

for rt,dirs,files in os.walk(root):
    if "os" in dirs:
        #print rt
        #print dirs

        WFC.append(rt+"/"+"os")
        for file in os.listdir(rt):
            if not os.path.isdir(rt+"/"+file):
                pass 


print WFC

for osdir in WFC:
    for rt,dirs,files in os.walk(osdir):
        #print rt
        for file in os.listdir(rt):
            if rt.find("i915", 0, len(rt))!=-1:
                break
            if not os.path.isdir(rt+"/"+file):
                if file=="media_srcs.cmake":
                    file_data = ""
                    with open(rt+"/"+file, "r") as f:
                        for line in f:
                            temp_line=line.split('/')
                            if temp_line[-1].find("mos_", 0, 5)!=-1:
                                if temp_line[-1].find(".h",-5, len(temp_line[-1]))!=-1:
                                    line=line.replace(".h","_next.h")
                                if temp_line[-1].find(".c",-5, len(temp_line[-1]))!=-1:
                                    line=line.replace(".c","_next.c")
                            file_data += line
                    with open(rt+"/"+file,"w") as f:
                        f.write(file_data)                         
                if file.find("mos_", 0, 5)!=-1:
                    print rt+"/"+file
                    file_data = ""
                    with open(rt+"/"+file, "r") as f:
                        for line in f:
                            temp_line=line
                            if line.split(' ')[0]=="#ifndef" or line.split(' ')[0]=="#define" or line.split(' ')[0]=="#endif":
                                line=line.replace("_H","_NEXT_H")
                                #print line
                            if line.split(' ')[0]=="#include" and line.split(' ')[1].find("\"mos_", 0, 5)!=-1:
                                line=line.replace(".h\"","_next.h\"")
                                #print line
                            file_data += line
                    with open(rt+"/"+file,"w") as f:
                        f.write(file_data)
                    if file.find(".h", -5, len(file))!=-1:
                        #print ".h"
                        os.rename(rt+"/"+file,(rt+"/"+file).replace(".h","_next.h"))
                    if file.find(".c", -5, len(file))!=-1:
                        #print ".c"
                        os.rename(rt+"/"+file,(rt+"/"+file).replace(".c","_next.c"))                
