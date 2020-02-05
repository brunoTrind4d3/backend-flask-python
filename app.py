from flask import Flask, request, jsonify
from binascii import a2b_base64
import face_recognition

app = Flask(__name__)


@app.route('/reconhecimento', methods=['POST'])
def recognize():
    data = request.get_json()
    uri_received = data['dataUriReceived']
    uri_compare = data['dataUriCompare']

    binary_data = a2b_base64(uri_received)
    fd = open('imageReceived.png', 'wb')
    fd.write(binary_data)
    fd.close()

    binary_compare = a2b_base64(uri_compare)
    fd = open('imageCompare.png', 'wb')
    fd.write(binary_compare)
    fd.close()

    known_image = face_recognition.load_image_file("imageReceived.png")
    unknown_image = face_recognition.load_image_file("imageCompare.png")

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

    return jsonify({'similarity': results})


if __name__ == "__main__":
    app.run()