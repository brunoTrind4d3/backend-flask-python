from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/reconhecimento', methods=['POST'])
def recognize():
    data = request.get_json()
    urireceived = data['dataUriReceived']
    uricompare = data['dataUriCompare']
    resultcompare = 0.78
    return jsonify({'similarity': resultcompare})


if __name__ == "__main__":
    app.run()