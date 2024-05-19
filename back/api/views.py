import os
from flask import Flask, request, send_file, render_template_string,jsonify
from scripts.format_change import Transformer
from .config import setup
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST"],
    }
})

socketio=SocketIO(app)
input,output=setup(app)
transformer=Transformer(input,output)

@app.route('/upload', methods=['POST'])

def upload():
    files = request.files.getlist('files')
    for file in files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename.lower())
        file.save(file_path)
    
    transformer.from_heic_to_png()
    # send_file(file_path, as_attachment=True)
    return jsonify({"message": "Files uploaded successfully!"})

# def upload_file():
#     if reques.method == 'POST':
#         if 'files' not in request.files:
#             return 'No file part', 400
#         
#         files = request.files['files']
#         if file.filename == '':
#             return 'No selected file', 400
#         print(files) 
#         # if file:
#         #     return send_file(file_path, as_attachment=True)
#
#     return render_template_string(form_template)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
