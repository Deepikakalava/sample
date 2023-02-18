import streamlit as st
import cv2
import mediapipe as mp

# Define hand tracking function
def track_hands():
    cap = cv2.VideoCapture(0)
    with mp.solutions.hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Flip the image horizontally
            frame = cv2.flip(frame, 1)
            # Convert image to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Perform hand tracking on the image
            results = hands.process(frame)
            # Display the image with hand tracking overlay
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp.solutions.drawing_utils.draw_landmarks(
                        frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            st.image(frame, channels="RGB")
            # Check if the Stop button is clicked
            if stop_button:
                cap.release()
                break
