from llama_cpp import Llama
import os

# Path to your GGUF LLaMA model file
MODEL_PATH = r"C:\Users\tharu\Plant_Disease_Detection_Treatment_Advisor\Plant-Disease-Detection-Treatment-Advisor\backend\llm\model\llama-2-7b-chat.Q4_K_M.gguf"

# Load the model (customize n_ctx, n_threads based on your system)
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=512,
    n_threads=8,
    use_mlock=True  # Prevents the model from being swapped out of RAM
)

def chat_with_llama(user_prompt):
    # Wrap the prompt in LLaMA 2 chat format
    system_prompt = (
        "[INST] <<SYS>>\n"
        "You are a helpful plant disease assistant. Answer clearly and concisely.\n"
        "<</SYS>>\n\n"
    )
    
    instruction = f"{user_prompt} [/INST]"

    # Combine system prompt and instruction to form the full prompt
    full_prompt = system_prompt + instruction

    # Call the LLaMA model with the full prompt
    response = llm(
        prompt=full_prompt,
        max_tokens=250,
        temperature=0.7,
        stop=["</s>"]
    )

    # Return the response text after stripping extra whitespace
    return response["choices"][0]["text"].strip()
