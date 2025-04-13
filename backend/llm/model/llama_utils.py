from llama_cpp import Llama
import os

# Path to your GGUF LLaMA model file
MODEL_PATH = r"C:\Users\tharu\Plant_Disease_Detection_Treatment_Advisor\Plant-Disease-Detection-Treatment-Advisor\backend\llm\model\llama-2-7b-chat.Q4_K_M.gguf"

# Load the model
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4,
    use_mlock=False
)

def get_current_weather(weather_data):
    try:
        # Debug: Print raw input
        print(f"🧪 Raw weather_data type: {type(weather_data)}")
        print(f"🧪 Raw weather_data preview: {weather_data}")

        # Since the provided data does not have a "current" key, return the data directly
        if isinstance(weather_data, dict):
            return weather_data
        else:
            print("⚠️ Weather data is not a dictionary.")
            return "Weather data unavailable"

    except Exception as e:
        print("⚠️ Failed to get current weather:", e)
        return "Weather data unavailable"

def chat_with_llama(user_prompt, user_location, weather_data):
    try:
        print("🔄 Starting chat_with_llama...")
        print(f"📍 Location: {user_location}")

        # Call get_current_weather and get the current weather data directly
        current_weather_info = get_current_weather(weather_data)
        print(f"🌦 Current Weather Info: {current_weather_info}")
        print(f"📝 User Prompt: {user_prompt}")

        # Build system prompt with current weather data
        system_prompt = (
            "[INST] <<SYS>>\n"
            "You are a helpful plant disease assistant. Answer clearly and concisely.\n"
            f"The user is located in: {user_location}. Provide treatment advice and recommendations suitable for this region.\n"
            f"Current weather data: {current_weather_info}\n"
            "<</SYS>>\n\n"
        )
        instruction = f"{user_prompt} [/INST]"
        full_prompt = system_prompt + instruction

        print("📨 Full prompt sent to model:")
        print(full_prompt)

        # Generate response from the model
        response = llm(
            prompt=full_prompt,
            max_tokens=150,
            temperature=0.5,
            stop=["</s>"]
        )

        print("✅ Full model response:")
        print(response)

        # Check the response and extract text
        if response and "choices" in response and len(response["choices"]) > 0:
            return response["choices"][0].get("text", "").strip()
        else:
            print("⚠️ Unexpected response format:", response)
            return "Error: Unexpected response format."

    except Exception as e:
        print(f"❌ Error in chat_with_llama: {e}")
        return "An error occurred while processing your request."
