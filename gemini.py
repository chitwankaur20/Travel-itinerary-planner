import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_itinerary(source, destination, start_date, end_date, no_of_day):
    prompt = f"""
    Create a personalized travel itinerary for a {no_of_day}-day trip from {source} to {destination},
    starting on {start_date} and ending on {end_date}.
    The plan should include daily activities, hotel and transport suggestions, and optimize for a budget in INR.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating itinerary: {str(e)}"