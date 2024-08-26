
import os


source_dir = os.path.join('.', 'Dateset', 'Initial_Data', 'fix_svg')
target_dir = os.path.join('.', 'Dateset', 'Initial_Data', 'finnal_svg')

# 检查目标目录是否存在，不存在则创建
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 遍历源目录中的所有SVG文件
for filename in os.listdir(source_dir):
    if filename.endswith(".svg"):
        file_path = os.path.join(source_dir, filename)
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 替换颜色
        content = content.replace('#FF8E46', '#008E8E')
        
        # 将修改后的内容写入到目标目录
        target_file_path = os.path.join(target_dir, filename)
        with open(target_file_path, 'w', encoding='utf-8') as file:
            file.write(content)

print("所有文件处理完成！")
