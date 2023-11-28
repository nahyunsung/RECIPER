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
    #webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
    
    cap = cv2.VideoCapture(0)
    
    
    # Set the title for the Streamlit app
    st.title("Video Capture with OpenCV")
    
    frame_placeholder = st.empty()
    
    # Add a "Stop" button and store its state in a variable
    stop_button_pressed = st.button("Stop")
    
    while cap.isOpened() and not stop_button_pressed:
        ret, frame = cap.read()
    
        if not ret:
            st.write("The video capture has ended.")
            break
    
        # You can process the frame here if needed
        # e.g., apply filters, transformations, or object detection
    
        # Convert the frame from BGR to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
        # Display the frame using Streamlit's st.image
        frame_placeholder.image(frame, channels="RGB")
    
        # Break the loop if the 'q' key is pressed or the user clicks the "Stop" button
        if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed: 
            break
    
    cap.release()
    cv2.destroyAllWindows()
