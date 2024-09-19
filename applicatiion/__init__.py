from flask import Flask
# from flask_script import Manager
# from application.utils.config import load_config
# manager = Manager()
 
def init_app(config_path):
    """全局初始化"""
    # 创建app应用对象
    app = Flask(__name__)
    # 项目根目录
    # app.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 加载配置
    # Config = load_config(config_path)
    # app.config.from_object(Config)
 
    # 初始化终端脚本工具
    # manager.app = app
 
    # return manager