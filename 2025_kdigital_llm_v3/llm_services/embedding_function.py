from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import Chroma
import os



def get_info_from_vectordb(persist_dir, splits, device):
    
    embedding_fn = HuggingFaceEmbeddings(
        model_name = "BAAI/bge-m3",
        model_kwargs={'device':device},
        encode_kwargs={'normalize_embeddings':True}
    )
    
    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        vectorstore = Chroma(
            persist_directory=persist_dir,
            embedding_function=embedding_fn
        )    
        
    else:
        vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=embedding_fn,
            persist_directory=persist_dir
        )
    return vectorstore.as_retriever(search_kwargs={'k':7})


