from flask import Flask , jsonify
# import train_gpt2
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/song', method=['GET'])
def weather():
    print('아아')
    result = 'dk'
    # result = train_gpt2.TransformersTokenizer
  # train_gpt2.DropOutput.after_pred
    return result



def getsong():
    return 'hi'


if __name__=="__main__":
  app.run(host='127.0.0.1', port='5001', debug=True)
