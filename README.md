# AI-Powered Search & Aggregation Tool - Backend  
<!-- ^ `#` tag: Main heading -->

This repository contains the backend implementation of an AI-powered search and aggregation tool built with Django Rest Framework (DRF). It integrates with AI agents powered by LangChain to process user queries, retrieves data from multiple sources (Google, YouTube, LinkedIn), and serves structured results to the frontend via RESTful APIs.

## Features  
<!-- ^ `##` tag: Subheading -->
- **Query Processing**: Uses LangChain AI agents to interpret and expand user queries.  
- **Multi-Source Data Retrieval**: Fetches results from Google, YouTube, and LinkedIn using APIs.  
- **Result Ranking**: Processes and ranks retrieved data for relevance using NLP techniques.  
- **RESTful API**: Provides endpoints for the frontend to access processed results.

## Tech Stack  
- **Django Rest Framework**: For building RESTful APIs.  
- **LangChain**: For AI-powered query processing and NLP tasks.  
- **Python**: Core programming language.  
- **Requests**: For making HTTP requests to external APIs.  
- **GROQ**: AI model integration for query enhancement.  
- **Google Custom Search API**: For Google search results.  

## Prerequisites  
- Python (v3.9 or higher)  
- pip (Python package manager)  
- Virtualenv (recommended)  
- GROQ API Key (for LangChain AI agents)  
- Google Project API Key (for Google API access)  
- Google Custom Search Engine (CSE) ID (for Google search)  

## Setup on Localhost  
Follow these steps to set up and run the backend on your local machine after cloning the repository:

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/Rudraparbat/Ai_backend.git
   cd Ai_backend

2. **Create and Activate a Virtual Environment-**:  
   ```bash
   python -m venv venv
   venv\Scripts\activate
   
3. **Install Dependencies:-**:  
   ```bash
   pip install -r requirements.txt

4. **Install Dependencies:-**:  
   ```bash
   pip install -r requirements.txt

#### Configure Environment Variables  
<!-- ^ `####` tag: Sub-subheading -->
- Create a `.env` file in the root directory (`backend/.env`) to store sensitive keys.  
- Open a text editor and add the following:  
  ```plaintext
  GROQ_API_KEY=your-groq-api-key
  GOOGLE_API_KEY=your-google-project-api-key
  GOOGLE_CSE_ID=your-google-cse-id

- **GROQ_API_KEY**: Sign up at the GROQ platform and copy your API key.  
- **GOOGLE_API_KEY**: Obtain from [Google Cloud Console](https://console.cloud.google.com) after enabling the Custom Search API.  
- **GOOGLE_CSE_ID**: Create a Custom Search Engine at [Google CSE](https://programmablesearchengine.google.com), configure it, and copy the ID.

#### Set Up the Database  
<!-- ^ `####` tag: Sub-subheading -->
- Apply Django migrations to create the database (uses SQLite by default).  
  ```bash
  python manage.py migrate

#### Run the Development Server  
<!-- ^ `####` tag: Sub-subheading -->
Start the Django development server to test the backend locally
  ```bash
  python manage.py runserver
  ```
The backend will be available at http://localhost:8000.
Visit http://localhost:8000/api/search/ in a browser or use a tool like Postman to test the API

### Key Challenges, Solutions, and Future Improvements :-
#### Fine-tune the AI model with domain-specific prompts and add caching for frequent queries.
#### Switch to asynchronous requests with asyncio and aiohttp for better scalability.
#### Implement a quota management system and fallback to cached results when limits are hit.
