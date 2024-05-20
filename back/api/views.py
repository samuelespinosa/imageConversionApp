import os
from flask import Flask, request, send_file, render_template_string,jsonify
from scripts.format_change import Transformer
from .config import setup
# from flask_cors import CORS
from flask_socketio import SocketIO,emit

app = Flask(__name__)
input,output=setup(app)
app.config['SECRET_KEY'] = 'secret!'
# CORS(app, resources={
#     r"/*": {
#         "origins": "*",
#         "methods": ["GET", "POST"],
#     }
# })
socketio=SocketIO(app,cors_allowed_origins="*")
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

@socketio.on("connect")
def connected():
    """Event listener when client connects to the server"""
    print(request.sid)
    print("client has connected")
    emit("connect", {"data": f"id: {request.sid} is connected"})

@socketio.on("enter")
def entered():
    print("has entered!!")

@socketio.on('data')
def handle_message(data):
    print("data from the front end: ",str(data))
    emit("data",{'data':data,'id':request.sid},broadcast=True)

@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=True)

if __name__ == '__main__':
    socketio.run(app,debug=True, port=8000)
