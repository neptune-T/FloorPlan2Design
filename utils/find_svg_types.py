# 我们注意到数据集出现照片颜色不匹配等一系列问题
# 现在我们需要统计数据集中的标签种类

import os
from xml.etree import ElementTree as ET
from collections import defaultdict

def find_types(input_directory):
    type_counts = defaultdict(int)
    
    for filename in os.listdir(input_directory):
        if filename.endswith('.svg'):
            file_path = os.path.join(input_directory, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # 遍历所有子元素，检查类型
            for elem in root.iter():
                if 'class' in elem.attrib:
                    class_type = elem.attrib['class']
                    type_counts[class_type] += 1
    
    return type_counts

# 使用相对路径
input_directory = os.path.join('Dateset', 'Initial_Data', 'SVG')

# 获取类型信息
type_counts = find_types(input_directory)

# 打印类型和数量
for class_type, count in type_counts.items():
    print(f"Type: {class_type}, Count: {count}")
