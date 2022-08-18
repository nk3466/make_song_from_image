# import time
#
# from flask import Flask, render_template, request
# # from flask_restful import reqparse
# import werkzeug
# from werkzeug.utils import secure_filename
# from PIL import Image
#
# from gpt2 import inference
# from image_captioning_prediction import predict
# from papagoApi import get_translate
#
# app = Flask(__name__, template_folder='templates', static_folder='static')
#
#
# @app.route('/result', methods=['GET'])
# def index():
#     return render_template('result.html')