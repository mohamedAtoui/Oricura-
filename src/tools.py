from langchain.tools.retriever import create_retriever_tool
from load_doc import retriever
retriever_tool = create_retriever_tool(
    retriever,
    "recherche_diagnostic",
    "Rechercher et retourner les informations médicales concernant les symptômes, les diagnostics possibles, et les recommandations de traitement dans la base de données médicale.",
)


tools = [retriever_tool]