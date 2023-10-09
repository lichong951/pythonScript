import os
import subprocess

# 指定Markdown文件所在的目录
input_dir = '/Users/lichong/Downloads'

# 指定输出Word文档的目录
output_dir = '/Users/lichong/Documents/MD/docx'

# 遍历Markdown文件
for file in os.listdir(input_dir):
    if file.endswith('.md'):
        # 构建输入和输出文件的路径
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, os.path.splitext(file)[0] + '.docx')

        if os.path.exists(output_file):
            print(f'文件 {output_file} 存在')
        else:
            print(f'文件 {output_file} 不存在')
            # 使用Pandoc将Markdown文件转换为Word文档
            subprocess.run(['pandoc', input_file, '-o', output_file])
            print(f'{input_file} --转换完成')

print('批量转换完成')