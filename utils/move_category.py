# 现在Initial_Data文件夹里面文件是png,svg文件存在混合在一块
# 我现在需要将其文件进行分开

import os
import shutil

# 定义源文件夹和目标文件夹路径
initial_data_dir = 'Dateset/Initial_Data'
png_folder = os.path.join(initial_data_dir, 'PNG')
svg_folder = os.path.join(initial_data_dir, 'SVG')

# 如果目标文件夹不存在，则创建
os.makedirs(png_folder, exist_ok=True)
os.makedirs(svg_folder, exist_ok=True)

# 遍历源文件夹中的文件
for filename in os.listdir(initial_data_dir):
    file_path = os.path.join(initial_data_dir, filename)
    
    # 检查是否是文件，而不是文件夹
    if os.path.isfile(file_path):
        # 如果是 PNG 文件，将其移动到 PNG 文件夹
        if filename.endswith('.png'):
            shutil.move(file_path, png_folder)
        
        # 如果是 SVG 文件，将其移动到 SVG 文件夹
        elif filename.endswith('.svg'):
            shutil.move(file_path, svg_folder)

print("文件已成功分类并移动到对应文件夹。")
