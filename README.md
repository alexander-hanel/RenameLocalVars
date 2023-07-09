# RenameLocalVars

RenameLocalVars is an IDA plugin that renames local variables to something easier to read. For example, `var_F8` would be renamed to `_ceres`. The names are arbitiary math terms. RenameLocalVars does not rename arguments or variables already named by IDA's analysis. 

# Installation 
RenameLocalVars has to be installed as an IDA Plugin. The following steps can be used to 
install the plugin. 

```
git clone https://github.com/alexander-hanel/RenameLocalVars.git
cd RenameLocalVars
copy rename_local_vars.py %IDAUSR%\plugins 
```
Note: if `%IDAUSR%` is not present or you don't know where this path is on your host, it can be 
found using IDAPython from the Output Window.

```
Python>import ida_diskio
Python>ida_diskio.get_user_idadir()
'C:\\Users\\yolo\\AppData\\Roaming\\Hex-Rays\\IDA Pro'
```
If a directory named `plugins` is not present, it needs to be created. 


## Usage 

Right Click > Rename Local Variables 

<p align="center">
    <img width="600" alt="Example Results" src="media/rename.gif?raw=true">
</p>


## Example Output 
Before 
```
.text:0000000180087A1C var_108         = qword ptr -108h
.text:0000000180087A1C var_100         = qword ptr -100h
.text:0000000180087A1C var_F8          = qword ptr -0F8h
.text:0000000180087A1C var_F0          = qword ptr -0F0h
.text:0000000180087A1C var_E8          = qword ptr -0E8h
.text:0000000180087A1C var_E0          = _LARGE_INTEGER ptr -0E0h
.text:0000000180087A1C var_D8          = qword ptr -0D8h
.text:0000000180087A1C var_D0          = qword ptr -0D0h
.text:0000000180087A1C var_C8          = qword ptr -0C8h
.text:0000000180087A1C var_C0          = qword ptr -0C0h
.text:0000000180087A1C var_A0          = qword ptr -0A0h
.text:0000000180087A1C var_98          = qword ptr -98h
.text:0000000180087A1C var_90          = qword ptr -90h
.text:0000000180087A1C var_88          = qword ptr -88h
.text:0000000180087A1C var_80          = qword ptr -80h
.text:0000000180087A1C var_78          = qword ptr -78h
.text:0000000180087A1C var_60          = qword ptr -60h
.text:0000000180087A1C var_58          = qword ptr -58h
.text:0000000180087A1C var_50          = qword ptr -50h
.text:0000000180087A1C var_48          = _UNICODE_STRING ptr -48h
.text:0000000180087A1C arg_0           = qword ptr  10h
.text:0000000180087A1C arg_8           = _LARGE_INTEGER ptr  18h
.text:0000000180087A1C arg_10          = qword ptr  20h
.text:0000000180087A1C arg_18          = qword ptr  28h
.text:0000000180087A1C arg_20          = dword ptr  30h
.text:0000000180087A1C arg_28          = dword ptr  38h
```

After
```
.text:0000000180087A1C _abacus         = qword ptr -108h
.text:0000000180087A1C _aeon           = qword ptr -100h
.text:0000000180087A1C _alpha          = qword ptr -0F8h
.text:0000000180087A1C _arc            = qword ptr -0F0h
.text:0000000180087A1C _atlas          = qword ptr -0E8h
.text:0000000180087A1C _baryon         = _LARGE_INTEGER ptr -0E0h
.text:0000000180087A1C _beta           = qword ptr -0D8h
.text:0000000180087A1C _carat          = qword ptr -0D0h
.text:0000000180087A1C _ceres          = qword ptr -0C8h
.text:0000000180087A1C _chaos          = qword ptr -0C0h
.text:0000000180087A1C _chi            = qword ptr -0A0h
.text:0000000180087A1C _dean           = qword ptr -98h
.text:0000000180087A1C _delta          = qword ptr -90h
.text:0000000180087A1C _epsilon        = qword ptr -88h
.text:0000000180087A1C _eta            = qword ptr -80h
.text:0000000180087A1C _fermat         = qword ptr -78h
.text:0000000180087A1C _gamma          = qword ptr -60h
.text:0000000180087A1C _gaudi          = qword ptr -58h
.text:0000000180087A1C _gnomen         = qword ptr -50h
.text:0000000180087A1C _ides           = _UNICODE_STRING ptr -48h
.text:0000000180087A1C arg_0           = qword ptr  10h
.text:0000000180087A1C arg_8           = _LARGE_INTEGER ptr  18h
.text:0000000180087A1C arg_10          = qword ptr  20h
.text:0000000180087A1C arg_18          = qword ptr  28h
.text:0000000180087A1C arg_20          = dword ptr  30h
.text:0000000180087A1C arg_28          = dword ptr  38h
```

## Note
I'm not sure how this works on the decompiler view. I don't have a personal copy of the decompiler so I didn't test it. 