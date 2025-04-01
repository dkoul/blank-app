import streamlit as st
import time
import random
from PIL import Image
import io
import base64

# Set page configuration
st.set_page_config(
    page_title="ChatGPT Free Ghibli Style Wrapper",
    page_icon="🎭",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        color: #1DB954;
        text-align: center;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #4F4F4F;
        text-align: center;
        margin-bottom: 30px;
    }
    .centered-text {
        text-align: center;
    }
    .result-text {
        font-size: 1.5rem;
        color: #FF4B4B;
        text-align: center;
        margin: 20px 0;
    }
    .stProgress > div > div > div > div {
        background-color: #1DB954;
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.markdown("<h1 class='main-title'>🌟 ChatGPT Free Ghibli Style Wrapper 🌟</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Transform your photos into beautiful Ghibli-style anime art for FREE!</p>", unsafe_allow_html=True)

# Initialize session state
if 'processing_complete' not in st.session_state:
    st.session_state.processing_complete = False
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'prank_revealed' not in st.session_state:
    st.session_state.prank_revealed = False

# Form for user input
with st.form("user_input_form"):
    name = st.text_input("Enter your name:", value=st.session_state.name)
    uploaded_file = st.file_uploader("Upload your image (JPG, PNG):", type=["jpg", "jpeg", "png"])
    submitted = st.form_submit_button("Convert to Ghibli Style!")
    
    if submitted and uploaded_file is not None and name:
        st.session_state.name = name
        
        # Show fake processing steps
        st.markdown("<p class='centered-text'>Starting conversion process...</p>", unsafe_allow_html=True)
        progress_bar = st.progress(0)
        
        # Fake processing steps with funny messages
        processing_steps = [
            "Analyzing image composition...",
            "Detecting facial features...",
            "Applying Miyazaki magic dust...",
            "Summoning Totoro for assistance...",
            "Consulting with the spirits of the forest...",
            "Drawing each pixel by hand...",
            "Brewing Calcifer's fire...",
            "Teaching your image to fly...",
            "Adding whimsy and wonder...",
            "Final Ghibli enchantment..."
        ]
        
        for i, step in enumerate(processing_steps):
            # Display current step
            status_text = st.empty()
            status_text.markdown(f"<p class='centered-text'>{step}</p>", unsafe_allow_html=True)
            
            # Update progress bar
            progress_value = (i + 1) / len(processing_steps)
            progress_bar.progress(progress_value)
            
            # Random delay to simulate processing
            time.sleep(random.uniform(0.5, 1.5))
        
        # Set session state to indicate processing is complete
        st.session_state.processing_complete = True
        st.session_state.prank_revealed = True
        
        # Force rerun to show the prank result
        st.rerun()

# Show prank result after processing
if st.session_state.prank_revealed:
    # Batman slapping Robin meme text
    st.markdown("<p class='result-text'>🤣 Happy Fools Day 🤣</p>", unsafe_allow_html=True)
    
    # Display the Batman slapping Robin meme
    
    # Personalized message
    st.markdown(f"""
    <p class='centered-text' style='font-size: 1.3rem; margin-top: 20px;'>
        Hey {st.session_state.name}, focus on your work instead of following trends! 😂
    </p>
    <p class='centered-text'>
        Read how your data is used to improve chatGPT models
    </p>
    """, unsafe_allow_html=True)
    st.link_button ('ChatGPT privacy policy', 'https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance')
    
    # Reset button
    if st.button("Try Again"):
        st.session_state.processing_complete = False
        st.session_state.prank_revealed = False
        st.rerun()

# Show info only when not in prank reveal mode
if not st.session_state.prank_revealed:
    # Fake testimonials
    st.markdown("### 💬 What people are saying")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        > "OMG this is amazing! My photos look exactly like they were drawn by Miyazaki himself!" 
        > 
        > — Abhishek
        """)
    
    with col2:
        st.markdown("""
        > "I can't believe this is free! My friends thought I hired a professional artist!"
        > 
        > — Nancy
        """)
    
    # Fake features list
    st.markdown("### ✨ Features")
    st.markdown("""
    - Convert any photo to Studio Ghibli style in seconds!
    - 100% FREE with no watermarks!
    - Advanced AI trained on every Ghibli film ever made!
    - Magical results that will amaze your friends!
    """)
