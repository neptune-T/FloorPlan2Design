import os
import xml.etree.ElementTree as ET
import random

# 设置源文件夹的路径
source_directory = os.path.join('.', 'Dataset', 'Initial_Data', 'colour', '5_livingroom_room')
target_directory = os.path.join('.', 'Dataset', 'Initial_Data', 'colour', '6_bathroom_room')

def update_color_and_class_random(element):
    room_elements = element.findall(".//*[@class='Room']")
    if room_elements:
        # 随机选择一个元素进行修改
        chosen_room = random.choice(room_elements)
        chosen_room.set('class', 'bathRoom')
        chosen_room.set('fill', '#cf6fc2')

# 确保目标目录存在
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# 遍历源目录中的所有SVG文件
for filename in os.listdir(source_directory):
    if filename.endswith(".svg"):
        filepath = os.path.join(source_directory, filename)
        tree = ET.parse(filepath)
        root = tree.getroot()

        # 随机更新颜色和类
        update_color_and_class_random(root)

        # 将修改后的SVG保存到目标文件夹
        target_filepath = os.path.join(target_directory, filename)
        tree.write(target_filepath)

print("文件已保存。")
