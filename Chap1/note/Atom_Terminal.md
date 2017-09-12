<u>缘起：</u>在观看大妈关于MVP演示的视频里，他使用了一个编辑器和cmd窗口合一的工具。如果我们用的是Atom编辑器，那么直接下一个platformio-ide-terminal的插件就可以实现这个功能了。

<u>这个工具的好处：</u>有点像个自制的Python IDE工具，可以让你在编写完源代码以后不用离开当前窗口即可开始调试。

<u>问题：</u>当下载和激活插件以后，在Atom里去toggle这个插件，但是cmd terminal窗口出不来。

<u>解决方案：</u>其实很简单。在Atom里，如果激活插件以后再窗口的右下角出现一个红色的小虫子图标，则表示插件build有问题。直接点进去，按Re-build即可。如下。感谢同学们的提示，自己对Atom的机制还是不太了解。

![issue](https://github.com/justin007755/Py101-004/blob/master/Chap1/resource/terminalPic_1.png)  

![Rebuild](https://github.com/justin007755/Py101-004/blob/master/Chap1/resource/terminalPic_2.png)  

![fixed](https://github.com/justin007755/Py101-004/blob/master/Chap1/resource/terminalPic_3.png)  
