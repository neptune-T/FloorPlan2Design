# 因为原来数据的文件名称存在png图片和svg图片不匹配的行为
# 所以将原来的数据重新更正名称并且放在新的文件夹里面Initial_Data里面

import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))

source_folder = os.path.join(script_dir, '..', 'Dateset', 'ImagesGT')

# 定义目标文件夹路径 (相对路径)
destination_folder = os.path.join(script_dir, '..', 'Dateset', 'Initial_Data')

# 确保目标文件夹存在
os.makedirs(destination_folder, exist_ok=True)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    # 如果文件是图片文件
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # 获取文件名（不含扩展名）
        base_name = os.path.splitext(filename)[0]
        
        # 找到对应的 SVG 文件
        for svg_filename in os.listdir(source_folder):
            if svg_filename.endswith('.svg') and svg_filename.startswith(base_name):
                # 构建新的文件名
                new_svg_filename = base_name + '.svg'
                
                # 获取原 SVG 文件的完整路径
                old_svg_file_path = os.path.join(source_folder, svg_filename)
                
                # 获取新的 SVG 文件的完整路径
                new_svg_file_path = os.path.join(destination_folder, new_svg_filename)
                
                # 如果目标文件已存在，添加唯一后缀
                count = 1
                while os.path.exists(new_svg_file_path):
                    new_svg_filename = f"{base_name}_{count}.svg"
                    new_svg_file_path = os.path.join(destination_folder, new_svg_filename)
                    count += 1
                
                # 移动并重命名 SVG 文件到目标文件夹
                shutil.move(old_svg_file_path, new_svg_file_path)
                print(f"重命名并移动 {svg_filename} 为 {new_svg_filename}")

            # 处理图片文件
            image_new_path = os.path.join(destination_folder, filename)
            if not os.path.exists(image_new_path):
                shutil.move(os.path.join(source_folder, filename), image_new_path)

print("所有文件已成功重命名并移动到 Initial_Data 文件夹。")
