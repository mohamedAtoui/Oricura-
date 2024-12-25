from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define path to your existing database
PERSIST_DIRECTORY = os.path.join(os.path.dirname(__file__), 'medical_db')

# Load the existing vectorstore
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
vectorstore = Chroma(
    persist_directory=PERSIST_DIRECTORY,
    embedding_function=embeddings,
    collection_name="medical-rag"
)

# Create retriever from existing vectorstore
retriever = vectorstore.as_retriever()
