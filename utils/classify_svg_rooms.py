import os
from xml.etree import ElementTree as ET
from shapely.geometry import Polygon
import matplotlib.colors as mcolors

# 颜色定义
room_colors = {
    'Bedroom': '#1f77b4',     # 蓝色
    'LivingRoom': '#ff7f0e',  # 橙色
    'Kitchen': '#9467bd',     # 紫色
    'Bathroom': '#17becf',    # 青色
    'Door': '#2ca02c'         # 绿色
}

# 根据面积或位置映射房间类型
def classify_room(area):
    if area > 500:
        return 'LivingRoom'
    elif 200 < area <= 500:
        return 'Bedroom'
    elif 100 < area <= 200:
        return 'Kitchen'
    else:
        return 'Bathroom'

def fix_svg(file_path, save_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for elem in root.findall('.//{http://www.w3.org/2000/svg}polygon'):
        points = [(float(p.split(',')[0]), float(p.split(',')[1])) for p in elem.attrib['points'].split()]
        polygon = Polygon(points)
        area = polygon.area

        if 'class' in elem.attrib:
            elem_class = elem.attrib['class']
            if elem_class == 'Door':
                elem.set('fill', room_colors['Door'])
            elif elem_class == 'Room':
                room_type = classify_room(area)
                elem.set('class', room_type)
                elem.set('fill', room_colors[room_type])

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
