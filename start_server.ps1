# AI Image Tools - PowerShell HTTP Server
Write-Host "🚀 正在启动 AI Image Tools 网站..." -ForegroundColor Green
Write-Host ""

# 检查端口是否被占用
$port = 8000
$connection = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue

if ($connection) {
    Write-Host "❌ 端口 $port 已被占用，请关闭占用该端口的程序后重试" -ForegroundColor Red
    Read-Host "按任意键退出"
    exit
}

Write-Host "📱 服务器启动中..." -ForegroundColor Yellow
Write-Host "📁 项目目录: $PWD" -ForegroundColor Cyan
Write-Host "🌐 访问地址: http://localhost:$port" -ForegroundColor Cyan
Write-Host "⏹️  按 Ctrl+C 停止服务器" -ForegroundColor Yellow
Write-Host ""

try {
    # 启动HTTP服务器
    $listener = New-Object System.Net.HttpListener
    $listener.Prefixes.Add("http://localhost:$port/")
    $listener.Start()
    
    Write-Host "✅ 服务器已启动！" -ForegroundColor Green
    Write-Host "🌐 请在浏览器中访问: http://localhost:$port" -ForegroundColor Cyan
    
    # 自动打开浏览器
    Start-Process "http://localhost:$port"
    
    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response
        
        $localPath = $request.Url.LocalPath
        $filePath = Join-Path $PWD $localPath.TrimStart('/')
        
        if ($localPath -eq "/") {
            $filePath = Join-Path $PWD "index.html"
        }
        
        if (Test-Path $filePath -PathType Leaf) {
            $content = Get-Content $filePath -Raw -Encoding UTF8
            $buffer = [System.Text.Encoding]::UTF8.GetBytes($content)
            $response.ContentLength64 = $buffer.Length
            $response.OutputStream.Write($buffer, 0, $buffer.Length)
            
            # 设置正确的Content-Type
            $extension = [System.IO.Path]::GetExtension($filePath)
            switch ($extension) {
                ".html" { $response.ContentType = "text/html" }
                ".css" { $response.ContentType = "text/css" }
                ".js" { $response.ContentType = "application/javascript" }
                ".json" { $response.ContentType = "application/json" }
                ".png" { $response.ContentType = "image/png" }
                ".jpg" { $response.ContentType = "image/jpeg" }
                ".jpeg" { $response.ContentType = "image/jpeg" }
                ".gif" { $response.ContentType = "image/gif" }
                default { $response.ContentType = "text/plain" }
            }
        } else {
            $response.StatusCode = 404
            $notFoundContent = "404 - 文件未找到: $localPath"
            $buffer = [System.Text.Encoding]::UTF8.GetBytes($notFoundContent)
            $response.ContentLength64 = $buffer.Length
            $response.OutputStream.Write($buffer, 0, $buffer.Length)
        }
        
        $response.Close()
        
        # 显示访问日志
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Write-Host "[$timestamp] $($request.HttpMethod) $localPath" -ForegroundColor Gray
    }
} catch {
    Write-Host "❌ 启动服务器时出错: $($_.Exception.Message)" -ForegroundColor Red
} finally {
    if ($listener) {
        $listener.Stop()
        Write-Host "🛑 服务器已停止" -ForegroundColor Yellow
    }
}

Read-Host "按任意键退出"
