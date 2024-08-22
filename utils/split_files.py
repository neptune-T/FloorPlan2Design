# 数据集都在imagesGT里面,现在需要将文件全部分开出来

import os
import shutil

# 获取当前脚本的路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 定义源文件夹路径 (相对路径)
source_folder = os.path.join(script_dir, '..', 'Dateset', 'ImagesGT')

# 定义目标文件夹路径 (相对路径)
image_folder = os.path.join(script_dir, '..', 'Dateset', 'Original_Image')
svg_folder = os.path.join(script_dir, '..', 'Dateset', 'Color_pictures')

# 创建目标文件夹（如果不存在的话）
os.makedirs(image_folder, exist_ok=True)
os.makedirs(svg_folder, exist_ok=True)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    # 获取文件的扩展名
    file_ext = os.path.splitext(filename)[1].lower()
    
    # 根据扩展名分类
    if file_ext in ['.png', '.jpg', '.jpeg']:  # 图片文件扩展名
        shutil.move(os.path.join(source_folder, filename), os.path.join(image_folder, filename))
    elif file_ext == '.svg':  # SVG文件扩展名
        shutil.move(os.path.join(source_folder, filename), os.path.join(svg_folder, filename))

print("文件已成功分类并移动到目标文件夹。")
