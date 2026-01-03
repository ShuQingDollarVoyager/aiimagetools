@echo off
echo 🚀 正在启动 AI Image Tools 网站...
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python未安装或不在PATH中
    echo 请安装Python: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 启动服务器
echo 📱 服务器启动中...
echo 📁 项目目录: %CD%
echo 🌐 访问地址: http://localhost:8000
echo ⏹️  按 Ctrl+C 停止服务器
echo.

python server.py

pause
