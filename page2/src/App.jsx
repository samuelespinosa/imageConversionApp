import { useState } from 'react'
import './App.css'
import DragAndDrop from './sections/DragAndDrop';
import io from 'socket.io-client';
import {API_URL} from './utils/config'
function App() {
  return (
    <>
      <DragAndDrop/>
    </>
  )
}

export default App
