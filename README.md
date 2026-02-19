# SuperMD5 - MD5 生成程序

计算文件的 MD5 哈希值，并生成与原文件名对应的 `.md5` 文本文件。

## 功能特点

- 支持 **Windows** 和 **macOS**
- 拖放文件到程序即可计算
- 无参数运行时弹出文件选择对话框
- 大文件分块读取，内存占用低
- 生成 `原文件名.md5` 文本文件，内容为 32 位小写 MD5 值

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 直接运行

```bash
python md5_generator.py
# 或指定文件
python md5_generator.py 文件1.pdf 文件2.png
```

### 打包为可执行文件

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包（使用 spec 配置）
pyinstaller build.spec

# 或直接命令行打包
pyinstaller --onefile --name SuperMD5 md5_generator.py
```

打包完成后：
- **Windows**: 可执行文件在 `dist/SuperMD5.exe`，将文件拖放到 exe 上即可
- **macOS**: 可执行文件在 `dist/SuperMD5`，将文件拖放到该程序上即可

### macOS 拖放说明

macOS 上拖放文件到终端程序时，需将程序放入 Applications 或使用以下方式：

1. 右键点击 `SuperMD5` → 打开
2. 或将文件拖到终端窗口，输入空格后再输入 `SuperMD5` 的路径

也可以直接运行程序，通过弹出的文件选择对话框选择文件。

## 输出示例

对 `document.pdf` 运行后，会生成 `document.pdf.md5`，内容示例：

```
d41d8cd98f00b204e9800998ecf8427e
```
