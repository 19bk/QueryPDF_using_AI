# PDF Query Chatbot with LangChain and Streamlit

## Overview
This project is a sophisticated chatbot application powered by LangChain and Streamlit, designed to answer questions based on the content of uploaded PDF documents. By leveraging the power of advanced embeddings and the LangChain framework, the chatbot provides accurate, context-aware responses, making it a valuable tool for extracting insights from PDFs interactively.

## Features
- **PDF Upload**: Users can upload multiple PDFs to the application.
- **Text Extraction**: Extracts and processes text from the uploaded PDFs.
- **Interactive Chatbot**: Users can interact with the chatbot to ask questions related to the PDF content.
- **LangChain Integration**: Utilizes LangChain for advanced, data-aware, and context-rich conversations.
- **Embeddings**: Employs OpenAI embeddings for text representation and similarity computations.

## Technologies Used
- **Streamlit**: For creating an interactive and user-friendly web application.
- **LangChain**: A framework that enables the development of data-aware conversational AI.
- **OpenAI Embeddings**: Used for converting text into numerical vectors for efficient processing and similarity computations.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.

## How It Works
1. **Uploading PDFs**: Users upload PDF documents to the application. The text content is then extracted and processed.
2. **Text Chunking**: The extracted text is divided into manageable chunks using LangChain’s CharacterTextSplitter.
3. **Vector Store Creation**: Text chunks are converted into embeddings using OpenAI Embeddings and stored in a FAISS vector store for efficient retrieval.
4. **Conversational AI**: LangChain integrates a language model, vector store, and memory buffer to create a conversation chain capable of generating context-aware responses.
5. **User Interaction**: Users can ask questions, and the chatbot retrieves relevant information from the PDF content to generate appropriate responses.

## Installation and Running
Ensure you have Docker installed. Clone the repository and navigate to the project directory. Build and run the Docker container using the following commands:

```sh
docker build -t pdf-query-chatbot .
docker run -p 8501:8501 pdf-query-chatbot
```

Open a web browser and navigate to [http://localhost:8501](http://localhost:8501) to interact with the application.

## Screenshots
![Screenshot of the application](static/pdfelphant.png)

## Conclusion
This PDF Query Chatbot demonstrates the integration of Streamlit with the LangChain framework, showcasing an advanced implementation of conversational AI that is data-aware and context-sensitive. The application stands as an example of how AI, machine learning embeddings, and modern frameworks can come together to deliver interactive and dynamic user experiences.

## License
This project is open source and available under the MIT License.
```

### Note:
- Make sure to replace `"static/pdfelphant.png"` with the actual relative path to the screenshot in your project directory if it's different.
- Ensure that the image file is included when you push your code to the remote repository, so it's accessible when viewing the README on platforms like GitHub.