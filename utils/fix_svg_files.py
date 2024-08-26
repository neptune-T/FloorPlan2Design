# 我们注意到数据集出现svg问题
#  <width> 和 <height> 标签从 SVG 文件中移除，并将它们作为 <svg> 元素的属性来保留
#  <width> 和 <height> 应该作为 <svg> 元素的属性，而不是独立的标签

import os
from xml.etree import ElementTree as ET

def fix_svg(file_path, save_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # 删除原始的 <width> 和 <height> 标签
    for elem in root.findall('*'):
        if elem.tag in ['width', 'height']:
            root.remove(elem)
    
    # 获取并添加宽度和高度信息到 <svg> 属性中
    width = '2550'
    height = '3300'
    
    root.set('width', width)
    root.set('height', height)
    
    # 将原始的宽度和高度信息保存到 <metadata> 中
    metadata = ET.SubElement(root, 'metadata')
    dimensions = ET.SubElement(metadata, 'dimensions')
    width_elem = ET.SubElement(dimensions, 'width')
    width_elem.text = width
    height_elem = ET.SubElement(dimensions, 'height')
    height_elem.text = height
    
    # 保存修改后的SVG文件到指定路径
    tree.write(save_path, encoding='utf-8', xml_declaration=True)

def batch_process(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.endswith('.svg'):
            file_path = os.path.join(input_directory, filename)
            save_path = os.path.join(output_directory, filename)
            fix_svg(file_path, save_path)
            print(f"Processed {filename} and saved to {save_path}")

# 使用相对路径
input_directory = os.path.join('Dateset', 'Initial_Data', 'SVG')
output_directory = os.path.join('Dateset', 'Initial_Data', 'fix_svg')

batch_process(input_directory, output_directory)
