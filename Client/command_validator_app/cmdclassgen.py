##expand each cmd field, generat c++ code;

import lxml.etree as ET

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
                


#--------------------------------------------------------------------------------------------------------------------
def newclassname(name):
    #eg. change VDENC_PIPE_MODE_SELECT_CMD to VdencPipeModeSelectCmd
    new_item = []
    for item in name.split("_"):
        item=item[0]+item[1:].lower()
        new_item.append(item)
    newclassname = ''.join(new_item)
    return newclassname
#--------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------
def addfixed(lines, classname, cmdname):
    newcmdclassname = newclassname(cmdname)
    fixed_str = f"""
#include <vector>
class {newcmdclassname} : public gpucmditem<{classname}::{cmdname}>
{{
public:
    xml xml1;
    {newcmdclassname}() : gpucmditem() {{}};
    ~{newcmdclassname}() {{}};
    bool initialize(char *testname);
    std::vector validate();
    cmdtype m_reference;
    cmdtype m_fieldtovalidate;

}};

"""
    lines.append(fixed_str)
#--------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------
def expandfield(lines,filename):
    
    tree = ET.parse('config_'+file_name+'.xml')
    root = tree.getroot()

    #expand field for each cmd
    for test in root.xpath('//*[starts-with(local-name(), "TestName")]'):
        testname = test.tag
        for Class in test.xpath('//*[starts-with(local-name(), "mhw")]'):
            classname = Class.tag
            for cmd in Class.xpath('//*[contains(local-name(), "CMD")]'):
                if cmd.tag == 'VDENC_PIPE_MODE_SELECT_CMD':    ########temperate!!!!!
                    cmdname = cmd.tag
                    newcmdclassname = newclassname(cmdname)
                    addfixed(lines, classname, cmdname)
                    if cmd.xpath('//*[starts-with(local-name(), "DW")]'):
                            #######initialize part start
                        lines.append(f"""
bool {newcmdclassname}::initialize(char *testname)
{{
    //find the xml
    xml<cmdtype> xml(&m_reference, &m_fieldtovalidate);
    //read xml to configure the cmd memeber
    xml1.readconfig(testname);
}}
    """)
                            #######initialize part end

                            ######validate part start
                        lines.append(f"""
std::vector {newcmdclassname}::validate()
{{
        std::vector<bool> error_code;""")
                        for dw in cmd.xpath('//*[starts-with(local-name(), "DW")]'):
                            if dw.attrib:
                                dwname = dw.tag
                                for field,value in dw.attrib.items():
                        
                                    lines.append(f"""
        if(m_fieldtovalidate && m_reference.{dwname}.{field} != xml1.getfield({testname}, {cmdname}, {dwname}, {field}))
        {{
               error_code.push_back(false);
        }}
        else
        {{
               error_code.push_back(true);
        }}
""")
                        lines.append(f"""
        //find false index
        auto it = error_code.begin(), end = error_code.end();
        for ( int index = 0; it != end; ++it, ++index)
            if (*it == false)
                error_index.push_back(index);
        std::cout<<"error_index";
        for (auto i : error_index)
            std::cout << i << ' '<<std::endl;
        return error_index;
}}""")
                            ######validate part end
#--------------------------------------------------------------------------------------------------------------------

file_name, file_path = input();
lines = []
expandfield(lines,file_name)
print(''.join(lines))
#with open( file_name + '_expand.cpp', "w") as f:
#      f.write(''.join(lines))
