import streamlit as st
import json
from huggingface_hub import InferenceClient

API_TOKEN = "Your_Hugging_face_key"  # Replace with your actual token

# Use the Hugging Face model
client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta", token=API_TOKEN)

def generate_text(destination, budget, duration, activities):
    prompt = (
    f"Generate a structured {duration}-day travel itinerary for {destination} with a {budget} budget. "
    f"In the itinerary, include:\n"
    f"- Morning, afternoon, and evening activities each day\n"
    f"- Recommended restaurants and cafes\n"
    f"- Transportation options\n"
    f"- Activities: {', '.join(activities)}\n"
    f"Ensure the itinerary is realistic and follows local recommendations."
)

    # prompt = f"Generate a detailed {duration}-day travel itinerary for {destination} with a {budget} budget, including activities like {', '.join(activities)}."

    print("Generated Prompt:", prompt)  # Debugging

    try:
        response = client.post(json={"inputs": prompt})
        print("API Response:", response)  # Debugging

        if not response.strip():  # If response is empty
            return "Error: Empty response from API."

        response_json = json.loads(response)
        return response_json[0]["generated_text"]
    
    except json.JSONDecodeError:
        return f"Error parsing response: Invalid JSON format. Response: {response}"

    except Exception as e:
        return f"Unexpected error: {str(e)}"


# Streamlit UI
st.title("AI Travel Planner")

# User inputs
destination = st.text_input("Enter your destination:")
budget = st.selectbox("Select your budget:", ["Low", "Moderate", "High"])
duration = st.slider("Select duration (days):", 1, 10, 3)
activities = st.multiselect("Select activities:", ["Museums", "Local Food", "Nightlife", "Nature", "Shopping", "Adventure", "Beaches"])

if st.button("Generate Itinerary"):
    if destination and activities:
        itinerary = generate_text(destination, budget, duration, activities)
        st.write("### Your Travel Itinerary:")
        st.write(itinerary)
    else:
        st.write("Please enter all required details.")
