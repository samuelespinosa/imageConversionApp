import { useEffect, useState } from "react";

export default function SocketCall({ socket, messages }) {
  const [message, setMessage] = useState("");

  const handleText = (e) => {
    const inputMessage = e.target.value;
    setMessage(inputMessage);
  };

  const handleSubmit = () => {
    if (!message) {
      return;
    }
    console.log(message);
    socket.timeout(5000).emit("data", message);
    setMessage("");
  };


  return (
    <div>
      <h2>WebSocket Communication</h2>
      <input type="text" value={message} onChange={handleText} />
      <button onClick={handleSubmit}>Submit</button>
      <ul>
        {messages.map((message, ind) => (
          <li key={ind}>{message}</li>
        ))}
      </ul>
    </div>
  );
}
