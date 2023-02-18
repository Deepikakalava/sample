import streamlit as st
import cv2
import numpy as np
from streamlit_webrtc import VideoProcessorBase, webrtc_streamer


class VideoTransformer(VideoProcessorBase):
    def transform(self, frame: np.ndarray) -> np.ndarray:
        # Draw a circle on the video frame
        img = cv2.circle(frame, (50, 50), 30, (255, 0, 0), 5)
        return img


def main():
    webrtc_streamer(key="example", video_processor_factory=VideoTransformer)

if __name__ == "__main__":
    main()
