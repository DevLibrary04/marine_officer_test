import torch
from transformers import pipeline, AutoProcessor, AutoModelForImageTextToText
from langchain_huggingface import HuggingFacePipeline

def setup_llm(device):
    
    model_id = "google/gemma-3n_E2B-it"
    
    processor = AutoProcessor.from_pretrained(model_id)
    
    model = AutoModelForImageTextToText.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True
    )
    
    pipe = pipeline(
        "image-text-to-text",
        model=model,
        tokenizer=processor.tokenizer,
        image_processor=processor.image_precessor,
        max_new_tokens=1024,
        temperature=0.2,
        device=device
        
        )
    
    return HuggingFacePipeline(pipeline=pipe)