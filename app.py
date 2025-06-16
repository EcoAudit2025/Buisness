import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import json
from urllib.parse import quote
from datetime import datetime
import database as db
from simple_ai_models import eco_ai, material_ai
from simple_chatbot import chatbot
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="EcoAudit",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Base URL for sharing
APP_URL = os.environ.get("REPLIT_DOMAINS", "").split(',')[0] if os.environ.get("REPLIT_DOMAINS") else ""

# Helper function to get actual public URL
def get_public_url():
    """Get the actual public-facing URL of the app"""
    if APP_URL:
        return f"https://{APP_URL}"
    return "URL not available"

# Initialize session state for displaying saved notifications
if 'show_saved' not in st.session_state:
    st.session_state.show_saved = False
if 'saved_message' not in st.session_state:
    st.session_state.saved_message = ""
if 'ai_initialized' not in st.session_state:
    st.session_state.ai_initialized = False

# Initialize AI system on first run
if not st.session_state.ai_initialized:
    with st.spinner("Initializing AI system..."):
        historical_data = db.get_utility_history(limit=100)
        data_for_training = []
        for record in historical_data:
            data_for_training.append({
                'timestamp': record.timestamp,
                'water_gallons': record.water_gallons,
                'electricity_kwh': record.electricity_kwh,
                'gas_cubic_m': record.gas_cubic_m,
                'water_status': record.water_status,
                'electricity_status': record.electricity_status,
                'gas_status': record.gas_status
            })

        success, message = eco_ai.train_models(data_for_training)
        if success:
            st.session_state.ai_initialized = True

# Existing app code continues here...

# Inject Developer Tool into User Profile page logic (simplified version for demonstration)
# Add this block in the section where a user is already logged in
if 'current_user' in st.session_state and st.session_state.current_user is not None:
    st.subheader("🧪 Developer Tools")
    delete_username = st.text_input("Enter username to delete", key="delete_user_input")
    if st.button("Delete User", key="delete_user_button"):
        deleted = db.delete_user(delete_username)
        if deleted:
            st.success(f"User '{delete_username}' deleted.")
        else:
            st.warning("User not found or could not be deleted.")

# (Ensure your database.py has the following function):
#
# def delete_user(username):
#     try:
#         user = session.query(User).filter_by(username=username).first()
#         if user:
#             session.delete(user)
#             session.commit()
#             return True
#         return False
#     except Exception as e:
#         print("Delete error:", e)
#         return False

# Rest of the large application logic follows...
