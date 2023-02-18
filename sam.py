import streamlit as st
import streamlit_webrtc as webrtc
import av
import numpy as np


class VideoTransformer(webrtc.VideoProcessor):
    def __init__(self):
        self.to_draw = None

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")
        # Draw a circle on the video frame
        img = cv2.circle(img, (50, 50), 30, (255, 0, 0), 5)
        self.to_draw = img
        return av.VideoFrame.from_ndarray(img, format="bgr24")

    def get_drawable_frame(self):
        return self.to_draw


def main():
    webrtc_ctx = webrtc.webrtc_streamer(key="example", video_processor_factory=VideoTransformer)

    if webrtc_ctx.video_processor:
        video_transformer = webrtc_ctx.video_processor
    else:
        video_transformer = VideoTransformer()

    while True:
        video_frame = video_transformer.get_drawable_frame()

        # Display the video frame in the Streamlit app
        st.image(video_frame, channels="BGR", use_column_width=True)


if __name__ == "__main__":
    main()
