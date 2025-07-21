from flask import Flask
import os
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()



def create_app():
    app = Flask(__name__)
    CORS(app)
    # 配置应用
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['API_KEY'] = os.getenv('API_KEY')
    app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')
    # 确保上传文件夹存在
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    return app