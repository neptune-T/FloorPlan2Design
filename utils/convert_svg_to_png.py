# 现在有了新的svg,我们使用工具将svg变成对应的图片保存到B中

import os
import re
from cairosvg import svg2png

# 获取当前脚本的路径
script_dir = os.path.dirname(os.path.abspath(__file__))

svg_folder = os.path.join(script_dir, '..', 'Dateset', 'Initial_Data', 'fix_svg')
png_output_folder = os.path.join(script_dir, '..', 'Dateset', 'B')

# 确保目标文件夹存在
os.makedirs(png_output_folder, exist_ok=True)

# 定义默认尺寸
default_width = '512px'
default_height = '512px'

# 正则表达式来匹配宽度和高度属性
width_re = re.compile(r'width="([\d.]+)(px|%)?"')
height_re = re.compile(r'height="([\d.]+)(px|%)?"')

# 遍历源SVG文件夹中的所有文件
for svg_filename in os.listdir(svg_folder):
    if svg_filename.endswith('.svg'):
        # 构建SVG文件的完整路径
        svg_file_path = os.path.join(svg_folder, svg_filename)
        
        # 读取SVG内容
        with open(svg_file_path, "r", encoding="utf-8") as file:
            svg_content = file.read()
        
        # 确保SVG文件包含尺寸定义
        if not width_re.search(svg_content) or not height_re.search(svg_content):
            # 如果未定义尺寸，则在 <svg> 标签中添加默认尺寸
            svg_content = re.sub(r'<svg', f'<svg width="{default_width}" height="{default_height}"', svg_content, count=1)
        
        # 构建输出PNG文件的路径
        png_filename = os.path.splitext(svg_filename)[0] + '.png'
        png_file_path = os.path.join(png_output_folder, png_filename)
        
        # 将SVG转换为PNG并保存
        svg2png(bytestring=svg_content.encode('utf-8'), write_to=png_file_path)
        
        print(f"已将 {svg_filename} 转换为 {png_filename}")

print("所有SVG文件已成功转换为PNG格式并保存到B文件夹中。")
