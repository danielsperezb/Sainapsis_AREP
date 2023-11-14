# Importing necessary libraries
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool
import os
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone

# Pinecone and OpenAI Embedding initialization
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT"))
embeddings = OpenAIEmbeddings()

# Define a tool function for greeting
@tool("SayHello", return_direct=True)
def say_hello(name: str) -> str:
    """Answer when someone says hello"""
    return f"Hello {name}! My name is Sainapsis"

# Define a tool function for searching documents
@tool("Search", return_direct=True)
def search(query: str, pinecone_index: str) -> list:
    """Consult the documents and generate a response"""
    docsearch = Pinecone.from_existing_index(pinecone_index, embeddings)
    docs = docsearch.similarity_search(query)
    return docs

# Main function
def main():
    # Initialize ChatOpenAI with temperature setting
    llm = ChatOpenAI(temperature=0)

    # List of tool functions
    tools = [
        say_hello,
        search
    ]

    # Initialize agent with tools, ChatOpenAI instance, and agent type
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )

    # Run the agent with an initial input
    print(agent.run("Hello! My name is Juan"))

    # Pinecone index creation
    pinecone_index = "sainapsis"
    pinecone.create_index(pinecone_index, dimension=1536, metric="cosine")

    # Folder containing engineering-related documents
    document_folder = os.path.join(os.path.expanduser("~"), "Documentos")

    # List of engineering field file names
    engineering_files = [
        "economia.txt",
        "ingenieria-civil.txt",
        "ingenieria-sistemas.txt",
        "ingenieria-electrica.txt",
        "ingenieria-industrial.txt"
    ]

    # Indexing engineering documents into Pinecone
    for file_name in engineering_files:
        file_path = os.path.join(document_folder, file_name)
        with open(file_path, "r") as text_file:
            # Indexing each document into Pinecone
            data = Pinecone.from_texts(texts=text_file.readlines(), embedding=embeddings, index_name=pinecone_index)

    # User input for a query
    query = input("Por favor digite su consulta (FAQs de ECI): ")

    # Using the agent to run the search tool and printing the results
    print(agent.run(search(query, pinecone_index)))

# Entry point
if __name__ == "__main__":
    main()
