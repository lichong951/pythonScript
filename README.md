# Python小工具
## pandoc批量转换MD文档为docx文档
Pandoc 的安装
安装方法有很多种。

方案一：直接通过 Pandoc 提供的安装包

下载链接在 [github](https://github.com/jgm/pandoc/releases) 上

方案二：包管理应用

Mac 用户可以通过 Homebrew 来安装，brew install pandoc
Ubuntu / Debian 用户可以通过 sudo apt install pandoc 来安装
CentOS 可以通过 yum install pandoc 来安装
也可以安装科学包管理工具 Anaconda ，过程中会自动安装 Pandoc

### 可扩展转换为如下文档

|格式|	                参数|
-----|------------------------
|CSV 表格	|            csv|
|Word 文档	|            docx|
|EPUB 电子书	|            epub|
|HTML 网页	     |       html|
|Markdown 文档	  |      markdown|
|PDF 文档（仅支持输出）|	  pdf|
|PPt 文档（仅支持输出）|	  pptx|
|JSON 数据	          |  json|

## 定时清理Mac系统垃圾文件
Mac版定时删除build、tmp等文件

## GIF转换
### 环境准备
Python：3.8.5
如果是运行代码的上面即可
核心代码如下
```
import moviepy.editor as mpe
cache = mpe.VideoFileClip("").subclip(0,15)
cache.write_gif("xxx.gif",fps=2)
```

如果需要运行界面的需要如下库支持：
pip install pyqt5

pip install PyQt5-tools

pyqt5 官网访问地址：![http://code.py40.com/pyqt5/](http://code.py40.com/pyqt5/)

pip install moviepy

视频转换为gif动图


