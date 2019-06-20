import os
import shutil
from ult_generator import header_parser
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import (
    Element, SubElement, XML, Comment
)
from ElementTree_pretty import prettify
import re


def countlines(start, lines=0, header=True, begin_start=None):
    if header:
        print('{:>10} |{:>10} | {:<20}'.format('COUNT', 'TOTAL', 'FILE'))
        print('{:->11}|{:->11}|{:->20}'.format('', '', ''))

    for r,d,f in os.walk(start):
        for thing in f:
            #ult folder is generated additionally for tests, skip them 
            if r'\ult' in r:
                continue
            # filter all mhw cmd header file
            if thing.startswith('mhw_')  and thing.endswith('.h'):
                thing = os.path.join(r, thing)
                with open(thing, 'rb') as f:    #'rb' fix reading errors
                    newlines = f.readlines()
                    newlines = len(newlines)
                    lines += newlines

                    if begin_start is not None:
                        reldir_of_thing = '.' + thing.replace(begin_start, '')
                    else:
                        reldir_of_thing = '.' + thing.replace(start, '')

                    print('{:>10} |{:>10} | {:<20}'.format(
                            newlines, lines, reldir_of_thing))

            if os.path.isdir(thing):
                lines = countlines(thing, lines, header=False, begin_start=start)
    return lines

def cpfiles(source, lines=0, header=True, begin_start=None):
    if header:
        print('{:>10} |{:>10} | {:<80} | {:<50}'.format('COPIED', 'TOTAL', 'FILE', 'TARGET'))
        print('{:->11}|{:->11}|{:->81} | {:-<50}'.format('', '', '', ''))

    for r,d,f in os.walk(source):
        #ult folder is generated additionally for tests, skip them 
        if r'\ult' in r:
            continue
        for thing in f:
            # filter all mhw cmd header file
            if thing.startswith('mhw_') and thing.endswith('.h'):
                fullthing = os.path.join(r, thing)
                if r'\agnostic' in r:
                    target = r.replace(r'\agnostic', r'\ult\agnostic\test')
                else:
                    target = os.path.join(r, r'ult\agnostic\test')
                ##dstdir =  os.path.join(target, r.replace(source, '.'))
                dstdir =  target
                if not os.path.exists(dstdir):
                    os.makedirs(dstdir) # create directories, raise an error if it already exists
                shutil.copy(fullthing, dstdir)

                with open(fullthing, 'rb') as f:    #'rb' fix reading errors
                    newlines = f.readlines()
                    newlines = len(newlines)
                    lines += newlines

                    print('{:>10} |{:>10} | {:<80} |{:<80}'.format(
                            newlines, lines, fullthing.replace(source, '.'), dstdir.replace(source, '.')))

            if os.path.isdir(thing):
                lines = countlines(thing, lines, header=False, begin_start=source)
    return lines

def clrfiles(source):
    for r,d,f in os.walk(source):
        #ult folder is generated additionally for tests, skip them 
        if r.endswith(r'\ult\agnostic\test'):
            shutil.rmtree(r, ignore_errors=True)


#----------------------------------------------------------------
ringpath = r'C:\projects\github\AutoULTGen\cmd_validation\vcstringinfo'
ringfilename = 'VcsRingInfo_0_0.txt'
gen = 12
source = r'C:\Users\jiny\gfx\gfx-driver\Source\media'
#----------------------------------------------------------------
#countlines(source)
cpfiles(source)
#clrfiles(source)



