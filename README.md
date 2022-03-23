# Python小工具

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

视频转换为gif动图
