import os
import xml.etree.ElementTree as ET

# 使用相对路径设置源文件夹和目标文件夹
source_directory = os.path.join('.', 'Dataset', 'Initial_Data', 'colour','finnal')
target_directory = os.path.join('.', 'Dataset', 'Initial_Data', 'colour','finnal')

def update_color(element):
    for elem in element.findall(".//*[@class='Door']"):
        elem.set('fill', '#8BBA00')

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

print("完成。")
