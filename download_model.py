"""Download the official Qwen GGUF once; subsequent runs work offline."""
from pathlib import Path
from huggingface_hub import hf_hub_download
from chatbot import MODEL_NAME

if __name__ == '__main__':
    target = Path(__file__).resolve().parent / 'models'
    print(hf_hub_download('Qwen/Qwen2.5-1.5B-Instruct-GGUF', MODEL_NAME, local_dir=target))
