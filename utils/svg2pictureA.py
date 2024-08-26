import os
import cairosvg
from PIL import Image

# 定义源SVG文件目录和目标图片目录
source_directory = os.path.join('.', 'Dataset', 'svg_a_b', 'a')
target_directory = os.path.join('.', 'Dataset', 'A')

# 创建输出目录（如果不存在）
os.makedirs(target_directory, exist_ok=True)

# 遍历source_directory中的所有SVG文件
for filename in os.listdir(source_directory):
    if filename.endswith('.svg'):
        svg_file_path = os.path.join(source_directory, filename)
        # 定义输出的PNG文件路径
        png_filename = filename.replace('.svg', '.png')
        output_image_path = os.path.join(target_directory, png_filename)
        
        # 将SVG文件转换为PNG图片并保存
        cairosvg.svg2png(url=svg_file_path, write_to=output_image_path)
        print(f'Converted {filename} to {png_filename} and saved to {target_directory}')

print("All SVG files have been converted to PNG images and saved.")
