import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

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
    # 注册蓝图

    from .routes.text_routes import text_bp
    # from .routes.image_routes import image_bp
    # from .routes.video_routes import video_bp
    # from .routes.audio_routes import audio_bp

    app.register_blueprint(text_bp, url_prefix='/api/text')
    # app.register_blueprint(image_bp, url_prefix='/api/image')
    # app.register_blueprint(video_bp, url_prefix='/api/video')
    # app.register_blueprint(audio_bp, url_prefix='/api/audio')

    return app