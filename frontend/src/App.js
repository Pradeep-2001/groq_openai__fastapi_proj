import { useState } from 'react';
import axios from 'axios';
import './App.css';

const MODEL_NAMES_GROQ = ['llama-3.3-70b-versatile'];

const App = () => {
  const [systemPrompt, setSystemPrompt] = useState('');
  const [provider] = useState('Groq'); // Hardcoded since only Groq is supported
  const [selectedModel, setSelectedModel] = useState(MODEL_NAMES_GROQ[0]);
  const [allowWebSearch, setAllowWebSearch] = useState(false);
  const [userQuery, setUserQuery] = useState('');
  const [response, setResponse] = useState(null);
  console.log(response,"response")
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const API_URL = 'http://localhost:9999/chat';

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!userQuery.trim()) {
      setError('Please enter a query');
      return;
    }

    setIsLoading(true);
    setError(null);
    setResponse(null);

    const payload = {
      model_name: selectedModel,
      model_provider: provider,
      system_prompt: systemPrompt,
      messages: [userQuery],
      allow_search: allowWebSearch,
    };

    try {
      const res = await axios.post(API_URL, payload);
      console.log(res,"res")
        setResponse(res.data);
    } catch (err) {
      setError('Failed to fetch response from the server');
    } finally {
      setIsLoading(false);
    }
  };

  return (
      <div className="app-container">
    <h1 className="app-title">AI Chatbot</h1>
    <p className="app-subtitle">Create and interact with AI agents</p>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="systemPrompt" className="block text-sm font-medium text-gray-700">
            Define your AI Agent
          </label>
          <textarea
            id="systemPrompt"
            value={systemPrompt}
            onChange={(e) => setSystemPrompt(e.target.value)}
            className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-blue-500 focus:border-blue-500"
            rows={4}
            placeholder="Enter system prompt"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Select Provider</label>
          <div className="mt-1 flex space-x-4">
            <label className="inline-flex items-center">
              <input
                type="radio"
                value="Groq"
                checked={provider === 'Groq'}
                onChange={() => {}} // Disabled since only Groq is supported
                className="form-radio h-4 w-4 text-blue-600"
                disabled
              />
              <span className="ml-2">Groq</span>
            </label>
          </div>
        </div>

        <div>
          <label htmlFor="modelSelect" className="block text-sm font-medium text-gray-700">
            Select Groq Model
          </label>
          <select
            id="modelSelect"
            value={selectedModel}
            onChange={(e) => setSelectedModel(e.target.value)}
            className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-blue-500 focus:border-blue-500"
          >
            {MODEL_NAMES_GROQ.map((model) => (
              <option key={model} value={model}>
                {model}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label className="inline-flex items-center">
            <input
              type="checkbox"
              checked={allowWebSearch}
              onChange={(e) => setAllowWebSearch(e.target.checked)}
              className="form-checkbox h-4 w-4 text-blue-600"
            />
            <span className="ml-2">Allow web search</span>
          </label>
        </div>

        <div>
          <label htmlFor="userQuery" className="block text-sm font-medium text-gray-700">
            Enter your query
          </label>
          <textarea
            id="userQuery"
            value={userQuery}
            onChange={(e) => setUserQuery(e.target.value)}
           rows={4}
            placeholder="Enter your query"
          />
        </div>

        <button
          type="submit"
          disabled={isLoading}
          
        >
          {isLoading ? 'Processing...' : 'Ask Agent'}
        </button>
      </form>

      {error && (
        <div className="error-box">
          {error}
        </div>
      )}

      {response && (
         <div className="response-box">
        <h2 className="response-title">Agent Response</h2>
        <div className="response-content">
            <p>{response}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default App;
