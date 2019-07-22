COMMAND VALIDATOR Tool
========

Let's introduce how the command validator app works. 

## Requirements

We need to install some requirements to run this tool. 

Pyside2
lxml

## Usage

**command_validator.py** is the main module. It defines all the events of pushbutton, combobox, dialog. 
Try to start UI from running this module.

Within it 3 classes are integrated.
### MainWindow

As you can see, the first UI interface contains 2 tab widgets, main and input.

*[Main]*

<img src="./screenshots/main.png" alt="png" width="600"/>

For each TextEdit field, users should satisfy certain requirements.
1. TestName 
- input testname like `encodeHevcCQ`
2. Command Path
- It should be the folder you store all the mhw_xxx.h files that you want to use.
For general search, you can choose `....\gfx\gfx-driver\Source\media` as your command path.
If you want to search specifically, click **Add Folder** button.

<img src="./screenshots/Addpath.png" alt="png" width="600"/>

In this interface you can adjust search priority by folder order, but path need end in hw(if you want
to add more than 1 folder). Don't forget to click save button before close this window.
The first folder will be used to generate base media path: `....\gfx\gfx-driver\Source`. We will use
base media path to generate your workspace(talk it later). Besides, we will add `...\media\media_embargo\agnostic\gen12\hw`
to the bottom of search list in case you forget to add it. This folder contains `mhw..._x.h` files.

3. Ringinfo path
- This path should contain vcsringinfo with name like `1-VcsRingInfo_0_0.txt`. The leading `1` 
means the first frame. But in the final result, we will make `0` as the first frame number. 

<img src="./screenshots/ringinfopath.png" alt="png" width="300"/>

4. DDI input path
- This path should contain ddiinput with name like `0-0_1_DDIEnc_SlcParams_I_Frame.txt`.

<img src="./screenshots/ddiinputpath.png" alt="png" width="300"/>

5. Platform

- read from `igfxfmid.h`. This doesn't really matter in my search logic because the platform 
name is not unified with cmd class name in mhw header. So while searching, I simply search class
name without `_x` first, then name with `_x`.

6. Component
- We have introduced how we find base media path. If you select `VP`, your workspace would be
`.....\Source\media\media_embargo\media_driver_next\ult\windows\vp\test\test_data`. Else, your workspace would 
be `.....\Source\media\media_embargo\media_driver_next\ult\windows\codec\test\test_data`. 
7. Frame
- Auto fill when you finish editing Ringinfo path

Click `Generate All` button, we will switch to the second tab widget: input.
We organize different testname infomation by seperate folders in your workspace. For example, if your
input tesname is `aaa`, then all the infomation related will be saved in `.....\test\test_data\aaa`.

*[input-new testname]*

<img src="./screenshots/input.png" alt="png" width="600"/>

- The first 2 text fields(Input Path & Component) inherit from main widget. If this is a new tesname, you need to input the infomation
listed. If you need to rewrite a testname, this will load old configuration from files.

*[input-existed testname]*

<img src="./screenshots/input_u.png" alt="png" width="600"/>

- GUID should be str, Width and Height should be int(Add 0x if you prefer to use int16).

As for next 5 comboboxes, **get_enum_member.py** script is written to load their dropdown lists.

- RawTileType, ResTileType attributes load dropdown lists from  

`...\Source\media\media_driver\agnostic\common\os\mos_resource_defs.h`

		#typedef enum _MOS_TILE_TYPE
		#{
		#    MOS_TILE_X,
		#    MOS_TILE_Y,
		#    MOS_TILE_YF,            // 4KB tile
		#    MOS_TILE_YS,            // 64KB tile
		#    MOS_TILE_LINEAR,
		#    MOS_TILE_INVALID
		#} MOS_TILE_TYPE;

- RawFormat, ResFormat attributes also load dropdown lists from  

`...\Source\media\media_driver\agnostic\common\os\mos_resource_defs.h`

		#typedef enum _MOS_FORMAT
		#{
		#   ...
		#   Format_NV12     ,
		#   ...
		#   Format_Buffer      ,
		#   ...
		#} MOS_FORMAT, *PMOS_FORMAT;
		
- EncFunc attribute loads dropdown lists from  

`...\Source\media\media_embargo\windows\common\codec\ddi\d3d9\dxvaencode_lh.h`

		#typedef enum tagENCODE_FUNC
		#{
		#    ENCODE_ENC          = 0x0001,
		#    ENCODE_PAK          = 0x0002,
		#    ENCODE_ENC_PAK      = 0x0004,
		#    ENCODE_HYBRIDPAK    = 0x0008,
		#    ENCODE_WIDI         = 0x8000
		#} ENCODE_FUNC;
		
- FrameNum is autofilled when you finish editing ddiinputpath in the main widget.

Then, click `Generate` or `Update` button. This step includes several oprations.
1. Firstly, combine all the DDIinput files in the path and 
your configuration in a new file (Name rule: TestName+Input.dat) in your workspace. 

<img src="./screenshots/aaaainput.png" alt="png" width="250"/>
<img src="./screenshots/aaaainput2.png" alt="png" width="450"/>

2. Secondly, update... (**Qichen**)
3. Also, start parsing cmd and related value in vcsringinfo files. Pop up commandinfo window 
when finished. 

### FormCommandInfo

*[CMD list]*

<img src="./screenshots/cmdlist.png" alt="png" width="800"/>

We give this cmd list to let users know whether there is any error in search process and 
in which class we find this cmd. As you can see in the image, we identify not found and size error.

- Size error means dword size isn't satisfy size rules: DW0_dwlength == Input_dwsize - 2, define_dwsize <=
Input_dwsize.Exceptions:

1. If DW0_dwlength doesn't exist, skip it.
2. If input_dwsize == 0/1, DW0_dwlength == 0
3. If cmd is `MI_STORE_DATA_IMM` or `MI_FLUSH_DW`, ignore its dwsize error. If `MI_NOOP` is its next cmd,
append `MI_NOOP value` to its last dword and delete this MI_NOOP

DW0_dwlength:
<img src="./screenshots/dw0_length.png" alt="png" width="800"/>

input_dwsize:
<img src="./screenshots/input_dwsize.png" alt="png" width="800"/>
input_dwsize for `MI_LOAD_REGISTER_IMM` is 3

define_dwsize:

<img src="./screenshots/def_dwsize.png" alt="png" width="400"/>

Besides, we also try to spot bitfield error in mhw. Like, : `__CODEGEN_BITFIELD(29, 32)` or bitfield overlap.
Currently, we do not find any:D


### Change cmd name or index

Double click cmd name or hitcount to modify it. You can modify any cmd in this list whether it reports error.
Type the new CMD name in the dialog.

<img src="./screenshots/modifycmd1.png" alt="png" width="800"/>
<img src="./screenshots/modifycmd2.png" alt="png" width="800"/>

Default setting of change scope is `Apply to All`. If you would like to change specific cmd in the sequence,
you can give the index like `1-4, 6` if the total hitcount is 7.

After finishing modifying, click `Save Changes & Update`. Wait till the Success window pops up.
<img src="./screenshots/modifycmd3.png" alt="png" width="800"/>

You can see the last modified CMD at the end of the list. (The true sequence of CMD would not change.)
<img src="./screenshots/modifycmd4.png" alt="png" width="800"/>

Click `Show All` to view the entire CMD validation form in details.

### Entire CMD validation form

<img src="./screenshots/All.png" alt="png" width="800"/>

**Qichen**

Features:
1. Check or uncheck a cmd or a dword on the left tree, or a field on the right table.
2. Double click the value to change it.
3. Deselect `Hide reserved field` to view the hidden reserved field

<img src="./screenshots/All2.png" alt="png" width="800"/>

4. View the value in hexadecimal, or in decimal, or in binary.
5. `save` and `generate` the updated configuration xml in your workspace for future reference:
`....\test\test_data\TestName\TestName_reference.xml` 








Other scripts you may need in the future
-------

## mvfiles.py

### countlines

count lines all the mhw header files  in desirable folder

### cpfiles

copy a batch of files to a batch of target locations

### clrfiles

clear files created in the previous opration

## ElementTree_pretty.py

pretty print XML elemt with indent


       <class name="mhw_vdbox_vdenc_g12_X">
           <public>