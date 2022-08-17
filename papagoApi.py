import requests

def get_translate(text):
    client_id = "xg8f9L12EddjGuN4HtEE" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "iR0r_O12hQ" # 개발자센터에서 발급받은 Client Secret 값
    data = {'text': text,
            'source': 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id": client_id,
              "X-Naver-Client-Secret": client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if (rescode == 200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:", rescode)