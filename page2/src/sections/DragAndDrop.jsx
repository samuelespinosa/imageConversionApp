import React, { useState, useCallback } from 'react';
import './DragAndDrop.css';
import axios from 'axios';
import {API_URL} from '../utils/config';
const DragAndDrop = () => {
  const [files, setFiles] = useState([]);
    const handleDragOver = useCallback((event) => {
        event.preventDefault();
        event.stopPropagation();
    }, []);

    const handleDrop = useCallback((event) => {
        event.preventDefault();
        event.stopPropagation();

        const droppedFiles = event.dataTransfer.files;
        setFiles((prevFiles) => [...prevFiles, ...Array.from(droppedFiles)]);
    }, []);

    const handleFileChange = (event) => {
        const selectedFiles = event.target.files;
        console.log('files',files)
        console.log('selectedFiles',selectedFiles)
        setFiles((prevFiles) => [...prevFiles, ...Array.from(selectedFiles)]);
    };
    
    const submitHandler = (event) => {
        event.preventDefault();
        const formData = new FormData();
        files.forEach(file => {
            formData.append('files', file);
        });
        axios.post(`${API_URL}/upload`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
        .then(response => {
            console.log('Files successfully uploaded', response);
        })
        .catch(error => {
            console.error('Error uploading files', error);
        });
    };  
          
    return (
        <div className="container">
            <div
                className="drop-area"
                onDragOver={handleDragOver}
                onDrop={handleDrop}
            >
                <p>Arrastra las imagenes</p>
                
                <form method="post" encType="multipart/form-data">
                <input
                    type="file"
                    id="fileElem"
                    name='files' 
                    multiple
                    accept="image/*"
                    onChange={handleFileChange}
                />
                <label className="button" htmlFor="fileElem">
                   Selecionar archivos 
                </label>
                <input 
                    type="submit" 
                    onClick={submitHandler}
                    className="button" 
                    value="Subir"
                />
              </form>
        </div>
            <div id="gallery">
                {files.map((file, index) => (
                    <img
                        key={index}
                        src={URL.createObjectURL(file)}
                        alt={`Preview ${index}`}
                    />
                ))}
            </div>
        </div>
    );
};

export default DragAndDrop;
