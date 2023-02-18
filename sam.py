import streamlit as st
import streamlit_webrtc as webrtc

def main():
    st.title("Camera feed")
    webrtc_streamer = webrtc.webrtc_streamer(
        key="example",
        video_transformer_factory=None,
        async_transform=False,
        source_video=True,
    )

    if webrtc_streamer is not None:
        video_frame = webrtc_streamer.get_frame()
        st.image(video_frame)

if __name__ == "__main__":
    main()
