from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import os
from datetime import datetime

app = Flask(__name__, 
            static_folder='.', 
            static_url_path='',
            template_folder='.')

# 配置
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['JSON_AS_ASCII'] = False  # 支持中文

# 数据文件路径
TOOLS_FILE = 'data/tools.json'
SUBSCRIBERS_FILE = 'data/subscribers.json'

# 确保数据目录存在
os.makedirs('data', exist_ok=True)

# 加载工具数据
def load_tools():
    try:
        with open(TOOLS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# 保存工具数据
def save_tools(tools):
    with open(TOOLS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)

# 路由
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/tools.html')
def tools_page():
    return send_from_directory('.', 'tools.html')

@app.route('/tools')
def tools_redirect():
    return send_from_directory('.', 'tools.html')

@app.route('/tools/<tool_slug>')
def tool_detail(tool_slug):
    # 这里你可以根据slug动态生成页面
    # 现在先返回模板页面
    return send_from_directory('.', 'tool-detail.html')

@app.route('/search')
def search_page():
    """搜索结果页面 - 重定向到tools页面并带上搜索参数"""
    query = request.args.get('q', '')
    return send_from_directory('.', 'tools.html')

@app.route('/categories.html')
def categories_page():
    return send_from_directory('.', 'categories.html')

@app.route('/categories')
def categories_redirect():
    return send_from_directory('.', 'categories.html')

@app.route('/comparisons.html')
def comparisons_page():
    return send_from_directory('.', 'comparisons.html')

@app.route('/comparisons')
def comparisons_redirect():
    return send_from_directory('.', 'comparisons.html')

@app.route('/blog.html')
def blog_page():
    return send_from_directory('.', 'blog.html')

@app.route('/blog')
def blog_redirect():
    return send_from_directory('.', 'blog.html')

@app.route('/about.html')
def about_page():
    return send_from_directory('.', 'about.html')

@app.route('/about')
def about_redirect():
    return send_from_directory('.', 'about.html')

@app.route('/contact.html')
def contact_page():
    return send_from_directory('.', 'contact.html')

@app.route('/contact')
def contact_redirect():
    return send_from_directory('.', 'contact.html')

@app.route('/privacy.html')
def privacy_page():
    return send_from_directory('.', 'privacy.html')

@app.route('/privacy')
def privacy_redirect():
    return send_from_directory('.', 'privacy.html')

@app.route('/terms.html')
def terms_page():
    return send_from_directory('.', 'terms.html')

@app.route('/terms')
def terms_redirect():
    return send_from_directory('.', 'terms.html')

@app.route('/submit.html')
def submit_page():
    return send_from_directory('.', 'submit.html')

@app.route('/submit')
def submit_redirect():
    return send_from_directory('.', 'submit.html')

# API路由
@app.route('/api/tools', methods=['GET'])
def get_tools():
    """获取所有工具"""
    tools = load_tools()
    
    # 过滤参数
    category = request.args.get('category')
    pricing = request.args.get('pricing')
    search = request.args.get('search', '').lower()
    sort_by = request.args.get('sort', 'featured')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 12))
    
    # 过滤
    filtered_tools = tools
    
    if category:
        filtered_tools = [t for t in filtered_tools if t.get('category') == category]
    
    if pricing:
        filtered_tools = [t for t in filtered_tools if t.get('pricing') == pricing]
    
    if search:
        filtered_tools = [t for t in filtered_tools 
                         if search in t.get('name', '').lower() 
                         or search in t.get('description', '').lower()]
    
    # 排序
    if sort_by == 'rating':
        filtered_tools.sort(key=lambda x: x.get('rating', 0), reverse=True)
    elif sort_by == 'reviews':
        filtered_tools.sort(key=lambda x: x.get('reviews', 0), reverse=True)
    elif sort_by == 'newest':
        filtered_tools.sort(key=lambda x: x.get('id', 0), reverse=True)
    elif sort_by == 'price-low':
        # Sort by pricing type: free < freemium < paid
        price_order = {'free': 0, 'freemium': 1, 'paid': 2}
        filtered_tools.sort(key=lambda x: price_order.get(x.get('pricing', ''), 3))
    elif sort_by == 'price-high':
        price_order = {'free': 0, 'freemium': 1, 'paid': 2}
        filtered_tools.sort(key=lambda x: price_order.get(x.get('pricing', ''), -1), reverse=True)
    else:  # featured
        filtered_tools.sort(key=lambda x: (x.get('featured', False), x.get('popular', False)), reverse=True)
    
    # 分页
    start = (page - 1) * limit
    end = start + limit
    paginated_tools = filtered_tools[start:end]
    
    return jsonify({
        'tools': paginated_tools,
        'total': len(filtered_tools),
        'page': page,
        'pages': (len(filtered_tools) + limit - 1) // limit
    })

@app.route('/api/tools/<int:tool_id>', methods=['GET'])
def get_tool(tool_id):
    """获取单个工具详情"""
    tools_data = load_tools()
    tools = tools_data.get('tools', []) if isinstance(tools_data, dict) else tools_data
    tool = next((t for t in tools if t.get('id') == tool_id), None)

    if tool:
        return jsonify(tool)
    else:
        return jsonify({'error': 'Tool not found'}), 404

@app.route('/api/tools/slug/<tool_slug>', methods=['GET'])
def get_tool_by_slug(tool_slug):
    """根据slug获取工具详情"""
    tools_data = load_tools()
    tools = tools_data.get('tools', []) if isinstance(tools_data, dict) else tools_data

    # Convert slug to match tool name (e.g., 'midjourney' -> 'Midjourney')
    for tool in tools:
        name_slug = tool.get('name', '').lower().replace(' ', '-').replace('.', '-')
        if name_slug == tool_slug.lower():
            # Get similar tools from same category
            similar = [t for t in tools if t.get('category') == tool.get('category') and t.get('id') != tool.get('id')][:3]
            return jsonify({**tool, 'similar_tools': similar})

    return jsonify({'error': 'Tool not found'}), 404

@app.route('/api/tools', methods=['POST'])
def add_tool():
    """添加新工具（管理员功能）"""
    data = request.json
    tools = load_tools()
    
    # 生成新ID
    new_id = max([t.get('id', 0) for t in tools] + [0]) + 1
    data['id'] = new_id
    data['created_at'] = datetime.now().isoformat()
    
    tools.append(data)
    save_tools(tools)
    
    return jsonify({'message': 'Tool added successfully', 'id': new_id}), 201

@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    """订阅邮件列表"""
    email = request.json.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    # 加载现有订阅者
    try:
        with open(SUBSCRIBERS_FILE, 'r', encoding='utf-8') as f:
            subscribers = json.load(f)
    except FileNotFoundError:
        subscribers = []
    
    # 检查是否已订阅
    if email in [s.get('email') for s in subscribers]:
        return jsonify({'message': 'Already subscribed'}), 200
    
    # 添加新订阅者
    subscribers.append({
        'email': email,
        'subscribed_at': datetime.now().isoformat()
    })
    
    # 保存
    with open(SUBSCRIBERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(subscribers, f, ensure_ascii=False, indent=2)
    
    return jsonify({'message': 'Successfully subscribed'}), 201

@app.route('/api/search', methods=['GET'])
def search():
    """搜索功能"""
    query = request.args.get('q', '').lower()
    tools = load_tools()
    
    if not query:
        return jsonify({'results': []})
    
    results = []
    for tool in tools:
        score = 0
        
        # 名称匹配（权重最高）
        if query in tool.get('name', '').lower():
            score += 10
        
        # 描述匹配
        if query in tool.get('description', '').lower():
            score += 5
        
        # 标签匹配
        for tag in tool.get('tags', []):
            if query in tag.lower():
                score += 3
        
        # 分类匹配
        if query in tool.get('category', '').lower():
            score += 2
        
        if score > 0:
            results.append({**tool, 'score': score})
    
    # 按匹配度排序
    results.sort(key=lambda x: x['score'], reverse=True)
    
    # 移除score字段
    for r in results:
        r.pop('score', None)
    
    return jsonify({'results': results[:20]})  # 返回前20个结果

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """获取所有分类及统计"""
    tools = load_tools()
    categories = {}
    
    for tool in tools:
        cat = tool.get('category', 'other')
        if cat not in categories:
            categories[cat] = {
                'name': cat,
                'count': 0,
                'tools': []
            }
        categories[cat]['count'] += 1
        categories[cat]['tools'].append(tool.get('name'))
    
    return jsonify(categories)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """获取网站统计数据"""
    tools = load_tools()
    
    try:
        with open(SUBSCRIBERS_FILE, 'r', encoding='utf-8') as f:
            subscribers = json.load(f)
    except FileNotFoundError:
        subscribers = []
    
    stats = {
        'total_tools': len(tools),
        'categories': len(set(t.get('category') for t in tools)),
        'free_tools': len([t for t in tools if t.get('pricing') == 'free']),
        'subscribers': len(subscribers),
        'avg_rating': sum(t.get('rating', 0) for t in tools) / len(tools) if tools else 0,
        'total_reviews': sum(t.get('reviews', 0) for t in tools)
    }
    
    return jsonify(stats)

# 静态文件处理
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

@app.route('/data/<path:path>')
def send_data(path):
    return send_from_directory('data', path)

# 错误处理
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # 开发模式
    app.run(debug=True, host='0.0.0.0', port=5000)
    
    # 生产模式建议使用 gunicorn 或 uwsgi
    # gunicorn -w 4 -b 0.0.0.0:5000 server:app