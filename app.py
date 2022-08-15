from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/photo_to_song',methods=['POST'])
def post():
	value = dict(request.form)
	print(value)
	return value
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