import streamlit as st
import streamlit_webrtc as webrtc
import av
import numpy as np


class VideoTransformer:
    def __init__(self):
        self.to_draw = None

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        # Draw a circle on the video frame
        img = cv2.circle(img, (50, 50), 30, (255, 0, 0), 5)
        self.to_draw = img
        return frame

    def get_drawable_frame(self):
        return self.to_draw


def main():
    webrtc_ctx = webrtc.webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

    if webrtc_ctx.video_transformer:
        video_transformer = webrtc_ctx.video_transformer
    else:
        video_transformer = VideoTransformer()

    while True:
        if webrtc_ctx.video_transformer:
            video_frame = webrtc_ctx.video_transformer.get_frame()
        else:
            # Get the next video frame
            video_frame = webrtc_ctx.get_next_frame()

            # Update the video transformer with the new frame
            video_transformer.transform(video_frame)

            # Get the transformed frame
            video_frame = video_transformer.get_drawable_frame()

        # Display the video frame in the Streamlit app
        st.image(video_frame, channels="BGR", use_column_width=True)


if __name__ == "__main__":
    main()
