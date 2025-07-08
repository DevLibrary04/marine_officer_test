import os
import shutil






router = APIRouter(prefix="/rag-chat", tags=["RAGChat"])

UPLOAD_DIR = './temp_storage'
os.makedirs(UPLOAD_DIR, exist_ok=True)