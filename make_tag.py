import nltk
from nltk.stem import PorterStemmer

from papagoApi import get_translate

stop_words = ["i","me","my","myself","we","our","ours","ourselves","you","you\'re","you\'ve",
              "you\'ll","you\'d","your","yours","yourself","yourselves","he","him","his",
              "himself","she","she\'s","her","hers","herself","it","it\'s","its","itself","they",
              "them","their","theirs","themselves","what","which","who","whom","this","that","that\'ll",
              "these","those","am","is","are","was","were","be","been","being","have","has","had","having",
              "do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by",
              "for","with","about","against","between","into","through","during","before","after","above","below","to","from",
              "up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where",
              "why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own",
              "same","so","than","too","very","s","t","can","will","just","don","don\'t","should","should\'ve","now","d","ll",
              "m","o","re","ve","y","ain","aren","aren\'t","couldn","couldn\'t","didn","didn\'t","doesn","doesn\'t","hadn",
              "hadn\'t","hasn","hasn\'t","haven","haven\'t","isn","isn\'t","ma","mightn","mightn\'t","mustn","mustn\'t",
              "needn","needn\'t","shan","shan\'t","shouldn","shouldn\'t","wasn","wasn\'t","weren","weren\'t","won","won\'t",
              "wouldn","wouldn\'t"]


def make_tag(prediction_result):
    global stop_words

    prediction_result = prediction_result.rstrip().split(' ')
    # remove stopwords
    result_keywords = [word for word in prediction_result if word not in stop_words]

    # result_keywords
    pos_tag = nltk.pos_tag(result_keywords)

    stemmer = PorterStemmer()
    for idx, (word, tag) in enumerate(pos_tag):
        if tag == 'VBG':  # word is not noun
            result_keywords[idx] = stemmer.stem(word)

    tags_string = ""
    for x in result_keywords:
        print(x)
    for keyword in result_keywords:
        tags_string += "#" + str(get_translate(keyword)).strip('.') + " "
    print("tag" + tags_string)
    return tags_string
