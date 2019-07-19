COMMAND VALIDATOR APP
========

Let's introduce how the command validator app works. 
Every module used is listed as followed.

## command_validator.py

It's the main module. It defines all the events of pushbutton, combobox, dialog. 
Try to start UI from running this module.

Within it 3 classes are integrated.
### MainWindow

As you can see, the first UI interface contains 2 tab widgets, main and input.

*[Main]*

<img src="file:///./screenshots/main.png" alt="png" width="600"/>

For each TextEdit field, users should satisfy certain requirements.
1. TestName 
- input testname like `encodeHevcCQ`
2. Command Path
- It should be the folder you store all the mhw_xxx.h files that you want to use.
For general search, you can choose `....\gfx\gfx-driver\Source\media` as your command path.
If you want to search specifically, click **Add Folder** button.

<img src="file:///./screenshots/Addpath.png" alt="png" width="600"/>

In this interface you can adjust search priority by folder order, but path need end in hw(if you want
to add more than 1 folder). Don't forget to click save button before close this window.
The first folder will be used to generate base media path: `....\gfx\gfx-driver\Source`. We will use
base media path to generate your workspace(talk it later).

3. Ringinfo path
- This path should contain vcsringinfo with name like `1-VcsRingInfo_0_0.txt`. The leading `1` 
means the first frame. But in the final result, we will make `0` as the first frame number. 

<img src="file:///./screenshots/ringinfopath.png" alt="png" width="300"/>

4. DDI input path
- This path should contain ddiinput with name like `0-0_1_DDIEnc_SlcParams_I_Frame.txt`.

<img src="file:///./screenshots/ddiinputpath.png" alt="png" width="300"/>

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

<img src="file:///./screenshots/input.png" alt="png" width="600"/>

- The first 2 text fields(Input Path & Component) inherit from main widget. If this is a new tesname, you need to input the infomation
listed. If you need to rewrite a testname, this will load old configuration from files.

*[input-existed testname]*

<img src="file:///./screenshots/input_u.png" alt="png" width="600"/>

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

<img src="file:///./screenshots/aaaainput.png" alt="png" width="250"/>
<img src="file:///./screenshots/aaaainput2.png" alt="png" width="450"/>

2. Secondly, update... (**Qichen**)
3. Also, start parsing cmd and related value in vcsringinfo files. Pop up commandinfo window 
when finished. 

### FormCommandInfo

*[CMD list]*

<img src="file:///./screenshots/cmdlist.png" alt="png" width="800"/>

We give this cmd list to let users know whether there is any error in search process and 
in which class we find this cmd. As you can see in the image, we identify not found and size error.
Size error means dword size isn't satisfy size rules: DW0_dwlength == Input_dwsize, define_dwsize <=
Input_dwsize.

DW0_dwlength:


Step 1
--------

- Be awesome
- Make things faster

Installation
------------

Install project by running:

    install project

Contribute
----------

- Issue Tracker: github.com/$project/$project/issues
- Source Code: github.com/$project/$project

Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@google-groups.com

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