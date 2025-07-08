import torch
from llm_services.core_rag.rag_chain import create_multimodal_rag_chain



class RagService:
    _instance = None
    rag_chain = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            
            
            device = "cuda" if torch.cuda.is_availabel() else "cpu"
            print(" start RAG chain")
            
            # 리트리버 생성하는 로직 : 실제파일경로와 DB경로
            # splits = load_and_split("path/d/ff/gg/jj.pdf")
            # retriever = get_vector_store(splits, "path/d/ff/gg/chroma_db", device)
            # 라우터에서 처리하는 방식
            
            cls.rag_chain = create_multimodal_rag_chain(retriever=None, device=device)
            print(" rag chain 실행중")
            
            return cls._instance
        
        def invoke_chain(self, question: str, image_path: str, retriever):
            if self.rag_chain:
                # 비동기 : 별도의 스레드에서 실행
                response = asyncio.to_thread(
                    self.rag_chain.invoke,
                    {"question": question, "image_path": image_path}
                )
                return response
            return "RAG 체인이 실행되지 않았음"
        
        
rag_service_instance = RagService.get_instance()