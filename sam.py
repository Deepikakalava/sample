import streamlit as st
import imageio
import mediapipe as mp

# Create a reader object for the default camera
reader = imageio.get_reader("<video0>")

# Initialize the hand tracking module
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

    # Loop over the frames and display them in Streamlit
    for frame in reader:
        # Convert the frame to RGB format
        frame = frame[:, :, :3]
        results = hands.process(frame)
        annotated_frame = frame.copy()
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    annotated_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
