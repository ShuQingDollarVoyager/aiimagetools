@echo off
echo 🚀 正在准备发布到GitHub...
echo.

REM 检查Git是否安装
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git未安装，请先安装Git
    echo 下载地址: https://git-scm.com/downloads
    pause
    exit /b 1
)

echo ✅ Git已安装
echo.

REM 添加所有文件
echo 📁 添加文件到Git...
git add .

REM 提交更改
echo 💾 提交更改...
git commit -m "更新AI Image Tools网站"

REM 推送到GitHub
echo 🚀 推送到GitHub...
git push origin main

echo.
echo ✅ 发布完成！
echo 🌐 网站地址: https://ShuQingDollarVoyager.github.io/aiimagetools
echo.
echo 📝 注意：
echo - 首次发布需要先在GitHub上创建仓库
echo - 需要启用GitHub Pages功能
echo - 部署可能需要几分钟时间
echo.

pause
