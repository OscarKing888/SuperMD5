#!/bin/bash
# 打包脚本 - 在项目目录下运行: ./build.sh

pip install -r requirements.txt
pyinstaller build.spec

echo ""
echo "打包完成! 可执行文件位于: dist/SuperMD5"
