<u>问题：</u>在使用心知天气API时，里面提到了一段Python调用的[Demo代码](https://github.com/seniverse/seniverse-api-demos/tree/master/python)。按说明，这个是可以先把Demo代码下到自己的本机做测试的。但是把demo-requests.py文件下到本机，按说明用“python3 demo-requests.py”测试时，发现程序报错，如下：  
![issue](https://github.com/justin007755/Py101-004/blob/master/Chap2/resource/ModulePic_1.PNG)

<u>Solution：</u>  
* 首先考虑用"pip install utils"去安装该模块。如下：  
![Rebuild](https://github.com/justin007755/Py101-004/blob/master/Chap2/resource/ModulePic_2.PNG)

* 重新运行“python3 demo-requests.py”后结果如下：  
![fixed](https://github.com/justin007755/Py101-004/blob/master/Chap2/resource/ModulePic_3.PNG)  

* 所以问题变成了找不到utils模块下的子模块const_value，什么原因？

* 然后去模块utils的安装目录下查看这个子模块有没有装好。在win7的Python下，这些用pip安装的模块都放在比如“D:\Program Files\Python36\Lib\site-packages”目录下。查看了utils目录下的文件，确实没发现const_value.py文件，所以是utils模块没装全。重新uninstall和install该模块以后，问题还是一样。所以问题并不出在标准的utils模块上。

* 反过头去看心知天气API的说明和代码，发现在他们的github库里有一个utils的目录，点进去一看，const_value.py赫然在目。

* 把这个文件直接下载拷贝到本机的“D:\Program Files\Python36\Lib\site-packages\utils”目录下，运行成功。  
![fixed](https://github.com/justin007755/Py101-004/blob/master/Chap2/resource/ModulePic_4.PNG)

<u>总结一下：</u>  
* 对问题可以首先根据报错信息去排查，逐步靠近问题的本质。
* 走进死胡同的时候，要换个思路或者从头再捋一遍。
* 给程序写Readme/Usage的时候，一些关键点要单独列出来，否则用户可以要花很长时间来研究。其实就是把用户当成小白来对待，不能预设用户已经知道某些东西。所以心知天气API的说明文档可以改进。
