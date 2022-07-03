# JsonCpp

## 安装和配置

```git
git clone https://github.com/open-source-parsers/jsoncpp.git
```
安装好了之后执行以下步骤
1. 进入安装好的jsoncpp-master文件可以看到有一个include 文件和 amalgamate.py文件
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/C++%20project/image/JsonCpp%E6%96%87%E4%BB%B6.PNG?raw=true)
2. 我们此时还需要一dist文件，它是由上述 amalgamate.py文件启动之后生成的 
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/C++%20project/image/JsonCpp%E7%94%9F%E6%88%90%E6%96%87%E4%BB%B6.PNG?raw=true)

3. 得到上述两个文件夹之后，为了使项目能够使用相应的头文件以及源文件，我们首先需要将 **dist** 和 **include**两个文件夹复制到项目文件中
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/C++%20project/image/Visual%20studio%20%E6%96%87%E4%BB%B6.PNG?raw=true)
4. 打开Visual Studio, 点开文件的 **properties**,选择 **C/C++**, 然后选择**General**,将之前所添加的include文件地址添加进去
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/C++%20project/image/C++linker.PNG?raw=true)
5. 同时点开dist中的json.cpp文件，添加到你项目源文件中。