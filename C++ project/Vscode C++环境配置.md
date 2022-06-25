## Error: gcc not recognized in Vscode 
1. First: open the link: https://www.msys2.org/
2. Go to the installation and download the installer .. install the exe file.
3. search mingw in windows search(windows start)
4. there is an app named--> **MSYS2 MinGW {64/32}-bit**
5. run it as administrator
6. Found command shell ---> type: **pacman -Syu**
7. Will ask you for some installation click on Y
8. Then again go to the same app **MSYS2 MinGW {64/32}-bit** and run as admin
9. and write--> pacman -Ss gcc (in shell that opend after click)
10. after clicking there will be bunch of things and now you have to care about your windows arch.. if it is 64 bit then write---> **pacman -S mingw-w64-x86_64-gcc** (and if its 32 you will find something like that where 64 will replaced by 32 in bunch of commands that are showing in your shell)
11. after executing this command gcc will be installed in your system to check write: **gcc --version || g++ --version**
12. After that to install the debugger write **pacman -S mingw-w64-x86_64-gdb**
13. to check write: **gdb --version**
    

##运行多个Cpp文件,包括头文件

因为使用的使code runner, 默认每次编译单个Cpp文件，所以需要修改一下json配置
**tasks.json**配置
``` javascript
{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: g++.exe 生成活动文件",
            "command": "C:\\msys64\\mingw64\\bin\\g++.exe",
            "args": [
                "-g",
                "${fileDirname}\\**.cpp",
                //"${fileDirname}\\**.h",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe",
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "调试器生成的任务。"
        }
    ],
    "version": "2.0.0"
}
```