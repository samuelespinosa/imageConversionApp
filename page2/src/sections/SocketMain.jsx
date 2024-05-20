import SocketCall from "./SocketCall";
import { io } from "socket.io-client";
import { useEffect, useState } from "react";

function SocketMain() {
  const [loading, setLoading] = useState(true);
  const [buttonStatus, setButtonStatus] = useState(false);
  const [messages, setMessages] = useState([]);
  const [socket,setSocket]=useState(null);
  const handleClick = () => {
    setButtonStatus(prevStatus => !prevStatus);
  };

  const handleData = (data) => {
    console.log("in handleData, data is",data);
    setMessages((prevMessages) => [...prevMessages, data.data]);
  };
   
  useEffect(() => {
      if (buttonStatus) {
      const socket = io("http://localhost:8000/", {
        cors: {
          origin: "http://localhost:5173/",

        },
      });
      setSocket(socket);
      function onEnter(data){
        console.log(data); 
        console.log('Connected front');
      }
      socket.on("enter",onEnter);
      setLoading(false);
      return () => {
        socket.off('enter',onEnter);
        socket.disconnect();
      };
    }
  }, [buttonStatus]);
  useEffect(() => {
    if(socket){ 
      socket.on("data", handleData);
      return () => {
        socket.off("data", handleData);
      };
    }
  }, [handleData])
  return (
    <div>
      {!buttonStatus ? (
        <button onClick={handleClick}>Turn Chat On</button>
      ) : (
        <>
          <button onClick={handleClick}>Turn Chat Off</button>
          <div className="line">
            {!loading && <SocketCall messages={messages} socket={socket} />}
          </div>
        </>
      )}
    </div>
  );
}

export default SocketMain;
