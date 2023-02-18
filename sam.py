import streamlit as st
import streamlit_webrtc as webrtc
from aiortc import VideoStreamTrack

class VideoTransformer(webrtc.VideoTransformerBase):
    def __init__(self):
        self.frame = None

    def transform(self, frame):
        self.frame = frame
        return frame

def main():
    st.title("Camera feed")

    # Create a video transformer that accesses the camera stream
    video_transformer = VideoTransformer()

    # Configure the WebRTC connection
    rtc_configuration = {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}

    # Create a webrtc streamer with the custom video transformer
    webrtc_streamer = webrtc.webrtc_streamer(
        key="example",
        video_transformer_factory=video_transformer,
        rtc_configuration=rtc_configuration,
        async_transform=False,
    )

    # Display the camera feed in the app
    if webrtc_streamer is not None:
        video_frame = video_transformer.frame
        st.image(video_frame)

if __name__ == "__main__":
    main()
