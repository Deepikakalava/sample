import streamlit as st
import streamlit_webrtc as webrtc
from av import VideoFrame
import numpy as np

class VideoTransformer(webrtc.VideoTransformerBase):
    def __init__(self):
        self.video_transformer = None

    def transform(self, frame: VideoFrame) -> np.ndarray:
        img = frame.to_ndarray(format="bgr24")
        return img

def main():
    st.title("Camera feed")

    # Create a video transformer that accesses the camera stream
    video_transformer = VideoTransformer()

    # Configure the WebRTC connection
    rtc_configuration = {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}

    # Create a webrtc streamer with the custom video transformer
    webrtc_streamer = webrtc.webrtc_streamer(
        key="example",
        video_processor_factory=video_transformer,
        rtc_configuration=rtc_configuration,
        async_processing=False,
    )

    # Display the camera feed in the app
    if webrtc_streamer is not None:
        video_frame = video_transformer.get_frame()
        st.image(video_frame)

if __name__ == "__main__":
    main()
