from llm_pipeline import setup_llm
from PIL import Image
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

def create_rag_chain(retriever, device):
    
    
    llm_pipeline = setup_llm(device=device)
    
    def model_invoker(inputs):
        
        question=inputs['question']
        image_path=inputs['image_path']
        context_docs=inputs['context']
        
        context_str = "\n\n".join([doc.page_count for doc in context_docs])
        
        prompt_text = f"""
        role
        
        # Context
        {context_str}
        
        # Question
        {question}
        
        
        """
        
        messages = [
            {"role":"user", "content": [{"type":"image"}, {"type":"text", "text":prompt_text}]}
            
        ]
        
        image = Image.open(image_path).convert("RGB")

        return llm_pipeline.invoke({'text':messages, 'images': image})
    
    
    rag_chain = (
        
        RunnablePassthrough.assign(context=(lambda x : x["question"]) | retriever)
        | RunnableLambda(model_invoker)
    )
    
    return rag_chain









