@echo off
REM 打包脚本 - 在项目目录下双击运行或在 cmd 中执行

pip install -r requirements.txt
pyinstaller build.spec

echo.
echo 打包完成! 可执行文件位于: dist\SuperMD5.exe
pause
