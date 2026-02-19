#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MD5 生成程序 - 计算文件的 MD5 哈希值并生成对应的 .md5 文本文件
支持 Windows 和 macOS，可通过拖放文件到程序上使用
"""

import hashlib
import sys
import os


def calculate_md5(file_path: str, chunk_size: int = 8192) -> str:
    """
    计算文件的 MD5 哈希值
    
    Args:
        file_path: 文件路径
        chunk_size: 每次读取的字节数，用于大文件分块读取
        
    Returns:
        MD5 哈希值字符串（32位小写十六进制）
    """
    md5_hash = hashlib.md5()
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            md5_hash.update(chunk)
    
    return md5_hash.hexdigest()


def process_file(file_path: str) -> bool:
    """
    处理单个文件：计算 MD5 并生成 .md5 文本文件
    
    Args:
        file_path: 文件路径
        
    Returns:
        是否成功处理
    """
    # 规范化路径，处理拖放时可能带引号的情况
    file_path = file_path.strip().strip('"').strip("'")
    
    if not os.path.exists(file_path):
        print(f"错误: 文件不存在 - {file_path}")
        return False
    
    if not os.path.isfile(file_path):
        print(f"跳过: 不是文件 - {file_path}")
        return False
    
    try:
        md5_value = calculate_md5(file_path)
        base_name = os.path.basename(file_path)
        md5_filename = base_name + ".md5"
        md5_filepath = os.path.join(os.path.dirname(file_path), md5_filename)
        
        with open(md5_filepath, 'w', encoding='utf-8') as f:
            f.write(md5_value)
        
        print(f"✓ {base_name} -> {md5_filename} ({md5_value})")
        return True
        
    except PermissionError:
        print(f"错误: 无权限读取文件 - {file_path}")
        return False
    except Exception as e:
        print(f"错误: 处理文件失败 {file_path} - {e}")
        return False


def main():
    """主入口：支持命令行参数（拖放）和交互式文件选择"""
    # 获取传入的文件路径（拖放或命令行参数）
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        # 无参数时，打开文件选择对话框
        try:
            import tkinter as tk
            from tkinter import filedialog
            
            root = tk.Tk()
            root.withdraw()  # 隐藏主窗口
            root.attributes('-topmost', True)  # 置顶
            
            files = filedialog.askopenfilenames(
                title='选择要计算 MD5 的文件',
                filetypes=[('所有文件', '*.*')]
            )
            root.destroy()
            
            if not files:
                print("未选择任何文件。")
                return
            
            # tkinter 返回的可能是 tuple
            files = list(files)
            
        except ImportError:
            print("用法: 将文件拖放到本程序上，或运行: python md5_generator.py <文件1> [文件2] ...")
            print("示例: python md5_generator.py document.pdf image.png")
            return
    
    success_count = 0
    for file_path in files:
        if process_file(file_path):
            success_count += 1
    
    if success_count > 0:
        print(f"\n完成: 成功生成 {success_count} 个 MD5 文件")
    
    # Windows 下从资源管理器拖放运行时，控制台会立即关闭，添加暂停
    if sys.platform == 'win32' and len(sys.argv) > 1:
        try:
            input("\n按回车键退出...")
        except (EOFError, OSError):
            pass  # 无控制台时（如 --noconsole）忽略


if __name__ == '__main__':
    main()
