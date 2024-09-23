from flask import Flask
 

from flask import Flask, request, jsonify
import threading
import pyautogui
import time

# 创建Flask应用实例
app = Flask(__name__)

is_running = False

def auto_mine():
    global is_running
    while is_running:
        x, y = 100, 200 
        pyautogui.click(x, y)
        time.sleep(5)


# 定义路由及其响应函数
@app.route('/')
def index():
    return 'Hello, Flask!'
 
if __name__ == '__main__':
    # 运行Flask应用
    app.run(debug=True)
    # app.run(port=5000)