# Import required packages
import cv2
import mediapipe as mp
import numpy as np
import streamlit as st

# Load pre-trained hand tracking model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Define app layout and widgets
st.title("Hand Tracking App")
start_button = st.button("Start")
stop_button = st.button("Stop")

# Define hand tracking function
# Define hand tracking function
def track_hands():
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Convert image to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Flip the image horizontally
            frame = cv2.flip(frame, 1)
            # Perform hand tracking on the image
            results = hands.process(frame)
            # Display the image with hand tracking overlay
            annotated_image = frame.copy()
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            st.image(annotated_image, channels="RGB")
            # Check if the Stop button is clicked
            if stop_button:
                cap.release()
                break

    

# Start the app
if start_button:
    track_hands()
