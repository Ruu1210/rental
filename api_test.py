from flask import Flask, jsonify, abort, request
app = Flask(__name__)
books = [
    {
        'id': 1,
        'title': u'论语',
        'auther': u'孔子',
        'price': 18
    },
    {
        'id': 2,
        'title': u'道德经',
        'auther': u'老子',
        'price': 15
    }
]


@app.route('/rental/api/books', methods=['GET'])
def get_tasks():
    return jsonify({'books': books})



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

