from flask import Flask, render_template, request
# from flask_restful import reqparse
import werkzeug
from werkzeug.utils import secure_filename
from PIL import Image

from image_captioning_prediction import predict
from papagoApi import get_translate

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/photo_to_song', methods=['POST'])
def post():
    # 사진 저장
    files = request.files
    file = files.get('photo_real')
    file.save('image/' + file.filename)
    photo_name = request.form['photo'].split("\\")[-1]
    print(request.form)
    make_sentence_from_photo = predict(photo_name)
    make_sentence_from_photo_final = make_sentence_from_photo.split("<")[0]
    print(make_sentence_from_photo_final)
    kor_sentence = get_translate(make_sentence_from_photo_final)
    print('번역' + kor_sentence)
    result = ''
    return result


#         root_path()
#         # Reference Image
#         refer_img = request.form['refer_img']
#         refer_img_path = '/images/nst_get/' + str(refer_img)
#
#         # User Image (target image)
#         user_img = request.files['user_img']
#         user_img.save('./flask_deep/static/images/' + str(user_img.filename))
#         user_img_path = '/images/' + str(user_img.filename)
#
#         # Neural Style Transfer
#         transfer_img = neural_style_transfer.main(refer_img_path, user_img_path)
#         transfer_img_path = '/images/' + str(transfer_img.split('/')[-1])
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
