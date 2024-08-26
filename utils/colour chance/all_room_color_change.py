import os
import xml.etree.ElementTree as ET

# 设置源文件夹和目标文件夹的路径
source_directory = os.path.join('.', 'Dataset', 'Initial_Data', 'colour', '1_windows')
target_directory = os.path.join('.', 'Dataset', 'Initial_Data', 'colour', '2_all_room')

def update_color(element):
    for elem in element.findall(".//*[@class='Room']"):
        # 直接设置新颜色，不检查原颜色
        elem.set('fill', '#097bb9')

# 确保目标目录存在
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# 遍历源目录中的所有SVG文件
for filename in os.listdir(source_directory):
    if filename.endswith(".svg"):
        filepath = os.path.join(source_directory, filename)
        tree = ET.parse(filepath)
        root = tree.getroot()

        # 更新颜色
        update_color(root)

        # 将修改后的SVG保存到目标文件夹
        target_filepath = os.path.join(target_directory, filename)
        tree.write(target_filepath)

print("所有房间标注的颜色已更新为#097bb9，并且文件已保存到2_all_room目录。")
