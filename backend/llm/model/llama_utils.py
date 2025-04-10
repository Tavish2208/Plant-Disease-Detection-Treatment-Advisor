from llama_cpp import Llama
import os

# Path to your GGUF LLaMA model file
MODEL_PATH =MODEL_PATH = r"D:\Plant-Disease-Detection-Treatment-Advisor\backend\llm\model\llama-2-7b-chat.Q4_K_M.gguf"

# Load the model (you can customize n_ctx, n_threads based on your system)
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=512,
    n_threads=8,
    use_mlock=True  # Prevents the model from being swapped out of RAM
)

def chat_with_llama(prompt):
    response = llm(
        prompt=prompt,
        max_tokens=256,
        temperature=0.7,
        stop=["</s>", "User:", "Assistant:"]
    )
    return response["choices"][0]["text"].strip()