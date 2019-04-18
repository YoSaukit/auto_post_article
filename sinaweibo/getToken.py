import webbrowser  # 打开浏览器
from pymouse import PyMouse  # 模拟鼠标
from pykeyboard import PyKeyboard   # 模拟键盘
import time
import win32clipboard, win32con   # 剪切板

# 在浏览器中打开网址
url=r'https://api.weibo.com/oauth2/authorize?display=default&client_id=88888888&redirect_uri=https%3A//api.weibo.com/oauth2/default.html&response_type=code'
webbrowser.open_new_tab(url)
time.sleep(10)

# 实例化鼠标键盘
m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()  # 屏幕分辨率

m.position()  # 鼠标位置，可以通过这个函数获取网址的像素点位置

# 复制网址的方法是，右键网址，然后F键，可以在浏览器中手动操作一下
# 移动到网址栏
time.sleep(1)
m.click(int(x_dim*0.5), int(y_dim*0.045), button=2, n=1)  # 移动到指定位置，然后右键单击
time.sleep(1)

k.press_key('F')  # 按下F键
time.sleep(1)
k.release_key('F')  # 释放F键
time.sleep(1)

# 关闭浏览器
m.click(int(x_dim * 0.985), int(y_dim * 0.015), button=1, n=1)

#  alt+tab组合键
# k.press_key(k.alt_key)
# k.tap_key(k.tab_key)
# k.release_key(k.alt_key)

# 获取剪切板内容
win32clipboard.OpenClipboard()
time.sleep(1)
new_url = win32clipboard.GetClipboardData(win32con.CF_TEXT)
time.sleep(1)
win32clipboard.CloseClipboard()
new_url = new_url.decode('gbk')

# 获取code
code = new_url.split('code=')[-1]