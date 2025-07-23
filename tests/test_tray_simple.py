"""
简单的托盘图标测试
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    import pystray
    from PIL import Image, ImageDraw
    print("pystray 和 PIL 导入成功")
except ImportError as e:
    print(f"导入失败: {e}")
    sys.exit(1)

def test_tray_icon():
    """测试托盘图标基本功能"""
    print("=== 测试托盘图标基本功能 ===")
    
    # 创建图标
    image = Image.new('RGB', (64, 64), color='red')
    draw = ImageDraw.Draw(image)
    draw.text((10, 20), "TEST", fill='white')
    
    # 创建菜单
    def show_window(icon, item):
        print("菜单项被点击：显示窗口")
    
    def quit_app(icon, item):
        print("菜单项被点击：退出")
        icon.stop()
    
    menu = pystray.Menu(
        pystray.MenuItem("显示窗口", show_window),
        pystray.MenuItem("退出", quit_app)
    )
    
    # 创建托盘图标
    icon = pystray.Icon("测试图标", image, "测试托盘图标", menu)
    
    # 设置单击事件
    def on_click(icon, event):
        print(f"托盘图标被单击，事件: {event}")
    
    icon.on_click = on_click
    
    print("托盘图标已创建")
    print("请查看系统托盘区域是否有红色图标")
    print("测试方法:")
    print("1. 单击托盘图标")
    print("2. 右键托盘图标，选择菜单项")
    print("3. 观察控制台输出")
    
    # 运行托盘图标
    icon.run()

if __name__ == "__main__":
    test_tray_icon() 