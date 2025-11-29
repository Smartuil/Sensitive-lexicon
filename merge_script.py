#!/usr/bin/env python3
import os
import glob

def merge_txt_files():
    # 配置选项
    config = {
        'output_file': 'format.txt',
        'excluded_dirs': ['.git', '.github', '__pycache__'],
        'excluded_files': ['format.txt', 'merge_script.py'],
        'separator': ',',
        'encoding': 'utf-8'
    }
    
    all_content = []
    
    # 递归查找所有txt文件
    txt_files = glob.glob("**/*.txt", recursive=True)
    print(f"找到的所有TXT文件: {txt_files}")  # 添加这行
    
    # 过滤文件
    filtered_files = []
    for file_path in txt_files:
        # 检查目录是否在排除列表中
        dir_excluded = any(excluded in file_path for excluded in config['excluded_dirs'])
        # 检查文件是否在排除列表中
        file_excluded = any(file_path.endswith(excluded) for excluded in config['excluded_files'])
        
        if not dir_excluded and not file_excluded:
            filtered_files.append(file_path)
    
    if not filtered_files:
        print("没有找到要合并的txt文件")
        return
    
    print(f"找到 {len(filtered_files)} 个文件进行合并:")
    for f in sorted(filtered_files):
        print(f"  - {f}")
    
    # 按文件名排序处理（可选）
    filtered_files.sort()
    
    # 读取所有文件内容
    for file_path in filtered_files:
        try:
            with open(file_path, 'r', encoding=config['encoding']) as f:
                for line_num, line in enumerate(f, 1):
                    cleaned_line = line.strip()
                    if cleaned_line:
                        all_content.append(cleaned_line)
                        
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {e}")
    
    # 写入合并后的文件
    if all_content:
        # 检查输出文件是否已存在
        output_exists = os.path.exists(config['output_file'])
        if output_exists:
            print(f"输出文件已存在: {config['output_file']}")
            with open(config['output_file'], 'r', encoding=config['encoding']) as f:
                old_content = f.read()
            new_content = config['separator'].join(all_content)
            print(f"旧内容长度: {len(old_content)}")
            print(f"新内容长度: {len(new_content)}")
            print(f"内容是否相同: {old_content == new_content}")
        
        with open(config['output_file'], 'w', encoding=config['encoding']) as f:
            f.write(config['separator'].join(all_content))
        
        print(f"\n合并完成！")
        print(f"输出文件: {config['output_file']}")
        print(f"总行数: {len(all_content)}")
        print(f"文件大小: {os.path.getsize(config['output_file'])} 字节")
    else:
        print("没有找到有效内容")

if __name__ == "__main__":
    merge_txt_files()
