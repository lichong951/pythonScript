# 背景：
# 由于经常要记录一些技术要点和效果。录制的视频太大不方便进行文章编辑和展示。
# 因此对视频进行gif转换，方便网站进行上传预览效果

###
# 功能如下:
# 视频转换为GIF

# 支持的视频格式如下
# *.mp4 
# *.wmv 
# *.rm 
# *.avi 
# *.flv 
# *.webm 
# *.wav 
# *.rmvb 
import moviepy.editor as mpe
cache = mpe.VideoFileClip("").subclip(0,15)
cache.write_gif("xxx.gif",fps=2)
