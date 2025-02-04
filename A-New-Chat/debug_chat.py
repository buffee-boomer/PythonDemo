# from langchain.embeddings import HuggingFaceEmbeddings

import sentence_transformers


from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2", 
    show_progress=True
)

# print(embeddings.cache_folder)