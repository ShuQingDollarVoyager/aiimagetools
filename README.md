# AI Image Tools Hub

一个展示AI图像工具的现代化网站，帮助用户发现、比较和选择最适合的AI图像处理工具。

## 🚀 快速开始

### 方法1：使用批处理文件（推荐）
```bash
# 双击运行
start_server.bat
```

### 方法2：使用Python
```bash
# 确保已安装Python
python server.py
```

### 方法3：直接打开HTML文件
```bash
# 在文件管理器中双击
index.html
```

## 📁 项目结构

```
aiimagetools/
├── index.html          # 主页面
├── css/               # 样式文件
├── js/                # JavaScript文件
├── data/              # 数据文件
├── images/            # 图片资源
├── pages/             # 其他页面
├── server.py          # Python服务器脚本
├── start_server.bat   # Windows启动脚本
└── README.md          # 项目说明
```

## 🌟 功能特性

- **响应式设计** - 支持桌面和移动设备
- **搜索功能** - 快速查找AI工具
- **分类浏览** - 按类别筛选工具
- **工具比较** - 对比不同工具的特性
- **现代化UI** - 使用Tailwind CSS构建
- **SEO优化** - 完整的元标签和结构化数据

## 🛠️ 技术栈

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **样式**: Tailwind CSS
- **图标**: Font Awesome
- **服务器**: Python HTTP Server

## 📱 访问地址

### 本地运行
启动服务器后，在浏览器中访问：
```
http://localhost:8000
```

### GitHub Pages（在线访问）
项目部署在GitHub Pages上，可以直接访问：
```
https://[你的用户名].github.io/aiimagetools
```

> 注意：首次部署后可能需要几分钟才能访问

## 🔧 开发说明

### 添加新工具
1. 编辑 `data/tools.json` 文件
2. 添加工具信息（名称、描述、价格等）
3. 在 `images/logos/` 目录中添加工具logo

### 自定义样式
- 主样式在 `css/custom.css`
- 使用Tailwind CSS类进行快速样式调整

### 添加新页面
1. 在 `pages/` 目录中创建新的HTML文件
2. 更新导航链接
3. 确保页面响应式设计

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

---

**注意**: 这是一个静态网站项目，所有数据都存储在JSON文件中。如需动态功能，建议集成后端API。
