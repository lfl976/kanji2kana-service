from sudachipy import tokenizer
from sudachipy import dictionary
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import katakana_to_hiragana_convert

# 创建分词器
tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C


# 定义分词函数
def tokenize_to_json(text):
    """
    对给定文本进行分词,并将分词结果以 JSON 格式返回
    包含单词surface、发音read、词性pos等信息
    """
    nodes = tokenizer_obj.tokenize(text, mode)
    tokens = []
    for node in nodes:
        print(node.surface(), node.reading_form(), node.part_of_speech())
        token = {
            'surface': node.surface(),
            'kana': katakana_to_hiragana_convert(node.reading_form()),
        }
        tokens.append(token)
    return tokens


application = Flask(__name__)
CORS(application)


@application.route('/')
def hello_world():  # put application's code here
    return 'Hello World2!'


@application.route('/katakana_to_hiragana/<text>')
def katakana_to_hiragana(text):
    return katakana_to_hiragana_convert(text)


@application.route('/tokenize', methods=['GET'])
def tokenize():
    text = request.args.get('text')
    if not text:
        return jsonify({'error': 'Missing text parameter'}), 400
    print(text)
    try:
        tokens = tokenize_to_json(text)
        print(tokens)
        return jsonify(tokens)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    application.debug = True
    application.run()
