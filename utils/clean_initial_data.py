# Initial_Data文件夹之中数据有些问题,存在孤立的svg和png的问题
# 现在需要新的文件将其中间剔除

import os

# 获取当前脚本的路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 定义Initial Data文件夹路径 (相对路径)
initial_data_folder = os.path.join(script_dir, '..', 'Dateset', 'Initial_Data')

# 获取Initial Data文件夹中的所有文件
files = os.listdir(initial_data_folder)

# 找到所有的PNG和SVG文件
png_files = set(f for f in files if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg'))
svg_files = set(f for f in files if f.endswith('.svg'))

# 获取去掉扩展名后的文件名集合
png_basenames = set(os.path.splitext(f)[0] for f in png_files)
svg_basenames = set(os.path.splitext(f)[0] for f in svg_files)

# 找到孤立的PNG文件和SVG文件
orphan_png_files = png_basenames - svg_basenames
orphan_svg_files = svg_basenames - png_basenames

# 删除孤立的PNG文件
for orphan in orphan_png_files:
    png_file_to_delete = os.path.join(initial_data_folder, orphan + '.png')
    if os.path.exists(png_file_to_delete):
        os.remove(png_file_to_delete)
        print(f"删除孤立的PNG文件: {png_file_to_delete}")

# 删除孤立的SVG文件
for orphan in orphan_svg_files:
    svg_file_to_delete = os.path.join(initial_data_folder, orphan + '.svg')
    if os.path.exists(svg_file_to_delete):
        os.remove(svg_file_to_delete)
        print(f"删除孤立的SVG文件: {svg_file_to_delete}")

print("数据清理完成。所有孤立文件已被删除。")
