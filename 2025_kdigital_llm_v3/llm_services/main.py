import torch
import argparse

from splitter import load_and_splitter
from embedding_function import get_info_from_vectordb
from rag_chain import create_rag_chain


def main():
    
    
    parser = argparse.ArgumentParser(description="multimodal demo")
    parser.add_argument('--pdf_path', type=str, required=True)
    parser.add_argument('--image_path', type=str, required=True)
    parser.add_argument('--question', type=str, required=True)
    parser.add_argument('--persist_dir', type=str, default='./chroma_db_multi_test_v2')
    args = parser.parse_args()
    
    
    
    
    
    
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    if device == "cuda":
        print(f"gpu: {torch.cuda.get_device_name(0)}")
        
    splits = load_and_splitter(args.pdf_path)
    
    retriever = get_info_from_vectordb(splits, args.persist_dir, device)
    
    rag_chain = create_rag_chain(retriever, device)
    
    result = rag_chain.invoke({"question": args.question, "image_path": args.image_path})

    print(result)
    
if __name__ == "__main__":
    
    main()






