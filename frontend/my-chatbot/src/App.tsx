import React, { useState } from 'react';
import { useChatStore } from './store';

const App: React.FC = () => {
  const [input, setInput] = useState<string>('');
  const messages = useChatStore((state) => state.messages);
  const addMessage = useChatStore((state) => state.addMessage);

  const sendMessage = async () => {
    if (!input.trim()) return;

    try {
      const response = await fetch('http://localhost:8000/api/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: input }),
      });

      if (!response.ok) {
        throw new Error('Failed to send message');
      }

      const data = await response.json();
      addMessage(data);
      setInput('');
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-2xl font-bold mb-4">Chat Bot</h1>
      <div className="w-full max-w-md bg-white shadow-md rounded-lg p-4 mb-4">
        <div className="flex flex-col space-y-2">
          {messages.map((msg, index) => (
            <p key={index} className="p-2 bg-blue-100 rounded">{msg}</p>
          ))}
        </div>
      </div>
      <div className="flex w-full max-w-md">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-grow p-2 border border-gray-300 rounded-l"
          placeholder="Type your message"
        />
        <button
          onClick={sendMessage}
          className="bg-blue-500 text-white px-4 py-2 rounded-r hover:bg-blue-600"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default App;