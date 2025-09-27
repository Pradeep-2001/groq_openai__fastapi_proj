# Agentic Chatbot Project

A FastAPI-based chatbot leveraging Groq and OpenAI APIs for agentic conversational experiences.

## Features

- FastAPI backend for scalable API endpoints
- Integration with Groq and OpenAI for advanced language capabilities
- Modular, extensible architecture

## Requirements

- Python 3.8+
- FastAPI
- Groq API credentials
- OpenAI API credentials

## Installation

```bash
git clone https://github.com/yourusername/Agentic_chatbot_proj.git
cd Agentic_chatbot_proj
pip install -r requirements.txt
```

## Usage

1. Set your Groq and OpenAI API keys as environment variables.
2. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

3. Access the API at `http://localhost:8000`.

## Project Structure

```
Agentic_chatbot_proj/
├── main.py
├── requirements.txt
├── README.md
└── ...
```

## License

MIT License

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI](https://openai.com/)
- [Groq](https://groq.com/)