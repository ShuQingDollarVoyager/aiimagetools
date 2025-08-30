# 🚀 GitHub 发布指南

## 📋 准备工作

### 1. 确保已安装Git
```bash
git --version
```

### 2. 配置Git用户信息（如果还没配置）
```bash
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的邮箱"
```

## 🔗 连接到GitHub

### 方法1：使用HTTPS（推荐）
```bash
# 添加远程仓库
git remote add origin https://github.com/你的用户名/aiimagetools.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

### 方法2：使用SSH
```bash
# 添加远程仓库
git remote add origin git@github.com:你的用户名/aiimagetools.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

## 🌐 启用GitHub Pages

1. **进入GitHub仓库页面**
2. **点击 Settings 标签**
3. **滚动到 Pages 部分**
4. **在 Source 下选择：**
   - Branch: `gh-pages`
   - Folder: `/ (root)`
5. **点击 Save**

## 📝 详细步骤

### 步骤1：在GitHub上创建新仓库
1. 访问 https://github.com
2. 点击右上角的 "+" 号，选择 "New repository"
3. 仓库名称：`aiimagetools`
4. 描述：`AI Image Tools Hub - 展示AI图像工具的现代化网站`
5. 选择 "Public"
6. **不要**勾选 "Add a README file"（我们已经有了）
7. 点击 "Create repository"

### 步骤2：推送代码到GitHub
```bash
# 确保在项目目录中
cd D:\Projects\aiimagetools

# 添加远程仓库（替换为你的GitHub用户名）
git remote add origin https://github.com/你的用户名/aiimagetools.git

# 重命名分支为main（GitHub推荐）
git branch -M main

# 推送到GitHub
git push -u origin main
```

### 步骤3：验证推送成功
1. 刷新GitHub仓库页面
2. 应该能看到所有文件都已上传

### 步骤4：启用GitHub Pages
1. 在仓库页面点击 "Settings"
2. 左侧菜单找到 "Pages"
3. Source 选择 "Deploy from a branch"
4. Branch 选择 "gh-pages"
5. 点击 "Save"

### 步骤5：等待自动部署
- GitHub Actions会自动构建和部署网站
- 通常需要2-5分钟
- 可以在 "Actions" 标签页查看部署进度

## 🔧 常见问题

### 问题1：推送时要求登录
**解决方案：**
- 使用GitHub CLI：`gh auth login`
- 或使用个人访问令牌

### 问题2：GitHub Pages不显示
**解决方案：**
1. 检查Actions是否成功运行
2. 确认gh-pages分支已创建
3. 等待几分钟让DNS生效

### 问题3：图片不显示
**解决方案：**
1. 检查图片路径是否正确
2. 确保图片文件已上传到GitHub
3. 使用相对路径而不是绝对路径

## 📱 访问网站

部署成功后，可以通过以下地址访问：
```
https://你的用户名.github.io/aiimagetools
```

## 🔄 更新网站

每次修改代码后：
```bash
git add .
git commit -m "更新说明"
git push
```

GitHub Actions会自动重新部署网站。

## 🎉 完成！

恭喜！您的AI Image Tools网站现在已经成功发布到GitHub Pages了！

---

**提示：** 如果遇到任何问题，请检查GitHub Actions的日志信息。
