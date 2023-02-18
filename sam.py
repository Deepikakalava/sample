import streamlit as st
import cv2
from streamlit_webrtc import webrtc_streamer
from webrtc_opencv import WebRtcOpencvTransformer


class VideoTransformer(WebRtcOpencvTransformer):
    def transform(self, frame):
        # Draw a circle on the video frame
        img = cv2.circle(frame.to_ndarray(format="bgr24"), (50, 50), 30, (255, 0, 0), 5)
        return img


def main():
    webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

if __name__ == "__main__":
    main()
