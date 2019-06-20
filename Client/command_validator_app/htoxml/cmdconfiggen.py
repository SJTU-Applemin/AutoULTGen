# generate unified cmd config file from .h.xml
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import (
    Element, SubElement, tostring, XML, Comment
)
from ElementTree_pretty import prettify
import random


def input():
    with open('input.txt', 'r') as fin:

            for line in fin:
                line = line.strip()
                if not line:
                    continue
                idx = line.rfind('/')
                file_name = line[idx+1:]
                file_path = line[:idx+1]
                return file_name, file_path
                

file_name, file_path = input();
tree = ET.parse(file_name+'.xml')
root = tree.getroot()
TestName = Element('TestName')
current_group = TestName

comment = Comment('This is cmd configure file')
TestName.append(comment)

for Class in root.findall('class'):
    Class_group = SubElement(current_group, Class.attrib['name'])
    current_group = Class_group

    for structcmd in Class.iter('struct'):
        if 'name' in structcmd.attrib and structcmd.attrib['name'].endswith('_CMD'):  #need change to _CMD
            structcmd_group = SubElement(current_group, structcmd.attrib['name'])
            #current_group = structcmd_group

            for union in structcmd.findall('union'):
                if 'name' in union.attrib :
                    union_name = SubElement(structcmd_group, union.attrib['name'])
                    for elem in union.iter():
                        if 'bitfield' in elem.attrib and 'name' in elem.attrib:
                            bitfield = SubElement(union_name, 'Bitfield')
                            bitfield.set('name', elem.attrib['name'])
                            bitfield.set('addr', elem.attrib['bitfield'])
                            bitfield.set('fixed', 'true')
                            #bit_item = elem.attrib['bitfield'].split(',')  #bitfield="0,  5"
                            #bitfield_start = int(bit_item[0].strip())
                            #bitfield_end = int(bit_item[1].strip())
                            #union_name.set(elem.attrib['name'], str(random.randint(bitfield_start, bitfield_end)))

with open( 'config_' + file_name + '.xml', "w") as f:
    f.write(prettify(TestName))
#print(prettify(TestName))