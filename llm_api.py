import requests
import config
system_message = """
    <role>You are an AI-powered CV Customization Expert specializing in optimizing CVs for Applicant Tracking Systems (ATS). Your goal is to revise the provided CV based on the ATS report to improve its alignment with the job requirements.</role>

"""
def call_llm(user_prompt, system_message, max_tokens=8000):
    """Generic function to call the OpenRouter LLM API."""
    try:
        response = requests.post(
            config.API_BASE,
            headers={
                "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek/deepseek-r1-zero:free",
                "messages": [
                    {"role": "system", "content": system_message},  # Dynamic system message
                    {"role": "user", "content": user_prompt}
                ], # Proper message format
                "temperature": 0.3,
                "max_tokens": max_tokens,
                "top_p": 1.0,
                "stream": False
            },
            timeout=30
        )
        response.raise_for_status()
        response_data = response.json()
        #print("🟢 API Raw Response:", response_data)
        
        if "choices" in response_data and response_data["choices"]:
            return response_data["choices"][0]["message"]["content"].strip()
        else:
            raise ValueError("❗ No choices in API response")
    
    except requests.exceptions.RequestException as err:
        raise ValueError(f"❌ API request failed: {err}")
