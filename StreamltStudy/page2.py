import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
from PIL import Image
import cv2

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")

def app():
    st.write('Camera')
    webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
