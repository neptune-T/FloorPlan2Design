import os
import xml.etree.ElementTree as ET

# 定义源目录和目标目录
source_directory = os.path.join('.', 'Dataset', 'Initial_Data', 'colour', 'finnal')
target_directory = os.path.join('.', 'Dataset', 'svg_a_b', 'a')

# 处理函数
def highlight_structure(element):
    for elem in element.iter():
        is_window = 'window' in elem.attrib.get('id', '').lower() or 'window' in elem.attrib.get('class', '').lower()
        is_door = 'door' in elem.attrib.get('id', '').lower() or 'door' in elem.attrib.get('class', '').lower()
        is_wall = 'wall' in elem.attrib.get('id', '').lower() or 'wall' in elem.attrib.get('class', '').lower()
        
        if 'style' in elem.attrib:
            style = elem.attrib['style']
            if is_window or is_door or is_wall:
                continue
            else:
                style_parts = style.split(';')
                new_style_parts = []
                for part in style_parts:
                    if 'fill' in part or 'stroke' in part:
                        new_style_parts.append(part.replace('fill:', 'fill:black;').replace('stroke:', 'stroke:black;'))
                    else:
                        new_style_parts.append(part)
                elem.attrib['style'] = ';'.join(new_style_parts)
        else:
            if is_window or is_door or is_wall:
                continue
            else:
                elem.attrib['fill'] = 'black'
                elem.attrib['stroke'] = 'black'

# 批量处理函数
def process_svg_files(source_directory, target_directory):
    for filename in os.listdir(source_directory):
        if filename.endswith('.svg'):
            file_path = os.path.join(source_directory, filename)
            
            # 解析SVG文件
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # 应用highlight_structure函数
            highlight_structure(root)
            
            # 将处理后的文件保存到指定目录
            output_path = os.path.join(target_directory, filename)
            tree.write(output_path)
            print(f'Processed and saved: {output_path}')

# 批量处理所有SVG文件
process_svg_files(source_directory, target_directory)
