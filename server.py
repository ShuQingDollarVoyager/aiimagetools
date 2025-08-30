#!/usr/bin/env python3
"""
简单的HTTP服务器，用于运行AI Image Tools网站
"""

import http.server
import socketserver
import os
import sys

# 设置端口
PORT = 8000

# 切换到项目目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加CORS头，允许跨域请求
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def log_message(self, format, *args):
        # 自定义日志格式
        print(f"[{self.log_date_time_string()}] {format % args}")

def main():
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🚀 AI Image Tools 网站已启动!")
            print(f"📱 访问地址: http://localhost:{PORT}")
            print(f"📁 项目目录: {os.getcwd()}")
            print(f"⏹️  按 Ctrl+C 停止服务器")
            print("-" * 50)
            
            # 启动服务器
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 服务器已停止")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 端口 {PORT} 已被占用，请尝试其他端口")
        else:
            print(f"❌ 启动服务器时出错: {e}")
    except Exception as e:
        print(f"❌ 未知错误: {e}")

if __name__ == "__main__":
    main()
