import time

from flask import Flask, render_template, request, jsonify, make_response
# from flask_restful import reqparse
import werkzeug
from werkzeug.utils import secure_filename
from PIL import Image

from gpt2 import inference
from image_captioning_prediction import predict
from papagoApi import get_translate

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/photo_to_song', methods=['POST'])
def result():
    start = time.time()
    # 파일 저장
    file = request.files['photo_real']
    filename = secure_filename(file.filename)
    file.save('static/image/' + filename)

    # image_captioning
    make_sentence_from_photo = predict('static\\image\\' + filename)
    make_sentence_from_photo_final = make_sentence_from_photo.split("<")[0]
    print(make_sentence_from_photo_final)

    #ko-gpt
    kor_sentence = get_translate(make_sentence_from_photo_final)
    print('번역:' + kor_sentence)
    result = inference(kor_sentence)
    print(time.time() - start)

    data = {'result': result}
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)
