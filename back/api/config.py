import os

def setup(app):
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../scripts/images_input')
    SEND_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../scripts/images_output')
    os.makedirs(UPLOAD_FOLDER,exist_ok=True)
    os.makedirs(UPLOAD_FOLDER,exist_ok=True)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SEND_FOLDER'] = SEND_FOLDER 
    app.config['SECRET_KEY'] = 'secret123'
    return (UPLOAD_FOLDER,SEND_FOLDER)
