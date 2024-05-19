import os
from glob import glob,escape
from PIL import Image
import pillow_heif
from flask_socketio import SocketIO, emit

class Transformer:
    
    def __init__(self,input_folder,output_folder):
        self.input_folder=input_folder 
        self.output_folder=output_folder
    def from_heic_to_png(self):
        files=glob(escape(self.input_folder)+"/*.heic")
        step=0 
        for file in files:
            step+=1;
            heif_file = pillow_heif.read_heif(file)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )
            # self.progress_tracker(num_files=len(files),step=step)
            print(file) 
            file_name=file.split('/')[1][:-5]
            print(file_name) 
            image.save(f"{self.output_folder}/{file_name}.png", format("png"))

    # def progress_tracker(self,num_files=1,step=0):
    #     progress=step/num_files 
    #     .emit('progress', {'progress': progress})
    #     if step==num_files: 
    #         emit('progress', {'progress': 100, 'status': 'done'})
