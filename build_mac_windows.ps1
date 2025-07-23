# 英语学习助手 - Windows编译Mac版本
# PowerShell脚本

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "英语学习助手 - Windows编译Mac版本" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查Docker
Write-Host "检查Docker环境..." -ForegroundColor Yellow
try {
    $dockerVersion = docker --version 2>$null
    if ($dockerVersion) {
        Write-Host "✅ Docker已安装: $dockerVersion" -ForegroundColor Green
        $useDocker = $true
    } else {
        throw "Docker未安装"
    }
} catch {
    Write-Host "❌ Docker未安装或未运行" -ForegroundColor Red
    Write-Host "请先安装Docker Desktop: https://www.docker.com/products/docker-desktop/" -ForegroundColor Yellow
    $useDocker = $false
}

Write-Host ""

if ($useDocker) {
    Write-Host "选择编译方式:" -ForegroundColor Yellow
    Write-Host "1. 使用Docker编译（推荐）" -ForegroundColor White
    Write-Host "2. 使用GitHub Actions编译" -ForegroundColor White
    Write-Host "3. 查看虚拟机编译指南" -ForegroundColor White
    Write-Host "4. 退出" -ForegroundColor White
    
    $choice = Read-Host "`n请选择 (1-4)"
    
    switch ($choice) {
        "1" {
            Write-Host "`n开始Docker编译..." -ForegroundColor Green
            
            # 构建Docker镜像
            Write-Host "构建Docker镜像..." -ForegroundColor Yellow
            docker build -t learnenglish-mac-builder .
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host "✅ Docker镜像构建成功" -ForegroundColor Green
                
                # 运行编译
                Write-Host "开始编译Mac版本..." -ForegroundColor Yellow
                docker run --rm -v "${PWD}:/app" learnenglish-mac-builder
                
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "`n🎉 Mac版本编译成功！" -ForegroundColor Green
                    Write-Host "📁 可执行文件位置: dist/英语学习助手" -ForegroundColor White
                    Write-Host "注意: 这个文件需要在Mac系统上运行" -ForegroundColor Yellow
                } else {
                    Write-Host "❌ 编译失败" -ForegroundColor Red
                }
            } else {
                Write-Host "❌ Docker镜像构建失败" -ForegroundColor Red
            }
        }
        "2" {
            Write-Host "`nGitHub Actions编译指南:" -ForegroundColor Green
            Write-Host "1. 将代码推送到GitHub仓库" -ForegroundColor White
            Write-Host "2. 在GitHub上查看Actions标签页" -ForegroundColor White
            Write-Host "3. 手动触发工作流或等待自动触发" -ForegroundColor White
            Write-Host "4. 下载编译好的Mac版本" -ForegroundColor White
            Write-Host ""
            Write-Host "优点: 完全免费，无需本地环境" -ForegroundColor Yellow
            Write-Host "缺点: 需要GitHub账号" -ForegroundColor Yellow
        }
        "3" {
            Write-Host "`n虚拟机编译指南:" -ForegroundColor Green
            Write-Host "详细说明请查看: 虚拟机编译指南.md" -ForegroundColor White
            Write-Host ""
            Write-Host "主要步骤:" -ForegroundColor Yellow
            Write-Host "1. 安装VMware或Parallels Desktop" -ForegroundColor White
            Write-Host "2. 创建macOS虚拟机" -ForegroundColor White
            Write-Host "3. 安装Python和依赖" -ForegroundColor White
            Write-Host "4. 运行编译脚本" -ForegroundColor White
        }
        "4" {
            Write-Host "退出程序" -ForegroundColor Yellow
            exit
        }
        default {
            Write-Host "无效选择，退出程序" -ForegroundColor Red
            exit
        }
    }
} else {
    Write-Host "由于Docker未安装，推荐使用以下方案:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "方案1: 安装Docker Desktop" -ForegroundColor White
    Write-Host "  下载地址: https://www.docker.com/products/docker-desktop/" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "方案2: 使用GitHub Actions" -ForegroundColor White
    Write-Host "  将代码推送到GitHub，使用自动编译" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "方案3: 使用虚拟机" -ForegroundColor White
    Write-Host "  查看详细指南: 虚拟机编译指南.md" -ForegroundColor Cyan
}

Write-Host "`n按任意键退出..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 