# AI Travel Planner

## Overview
The AI Travel Planner is a Streamlit-based web application that generates personalized travel itineraries based on user input. It utilizes the **Hugging Face Zephyr-7B model** to create detailed day-by-day plans, including recommended activities, restaurants, transportation options, and accommodations.

## Features
- Users can input their **destination, budget, trip duration, and preferred activities**.
- The app generates a **structured multi-day itinerary**.
- Utilizes **Hugging Face's Zephyr-7B model** instead of OpenAI.
- Hosted on **Streamlit Cloud** for live access.

## Setup & Installation
To run the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/travel-planner.git
   cd travel-planner
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Deployment
The application is deployed on **Streamlit Cloud**. You can access the live version [here](your-deployment-link).

## Usage
1. Enter your travel details:
   - Destination (e.g., Paris)
   - Budget (Low, Moderate, High)
   - Duration (1-10 days)
   - Activities (Museums, Local Food, Nightlife, etc.)
2. Click **"Generate Itinerary"**.
3. View the detailed day-by-day itinerary generated by the AI.

## Technologies Used
- **Python**
- **Streamlit** (for UI)
- **Hugging Face Hub** (Zephyr-7B model for text generation)

## Acknowledgment
This project is developed as a **Prompt Engineering Assignment**. Unlike typical implementations using OpenAI, we used Hugging Face models for itinerary generation.

## Preview

![Screenshot 2025-01-28 221800](https://github.com/user-attachments/assets/6620dd1a-14e9-447d-bfeb-a5e06b5ff6fb)
