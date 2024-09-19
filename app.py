from flask import Flask
 
# 创建Flask应用实例
app = Flask(__name__)
 
# 定义路由及其响应函数
@app.route('/')
def index():
    return 'Hello, Flask!'
 
if __name__ == '__main__':
    # 运行Flask应用
    app.run(debug=True)