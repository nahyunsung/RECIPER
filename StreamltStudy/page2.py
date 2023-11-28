import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
from PIL import Image
import cv2
import tensorflow.keras
import numpy as np

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")

def app():
    st.write('Camera')
    #webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
    #main()
    
    img_file_buffer = st.camera_input("Take a picture")
    
    if img_file_buffer is not None:
        # To read image file buffer with OpenCV:
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
        # Check the type of cv2_img:
        # Should output: <class 'numpy.ndarray'>
        st.write(type(cv2_img))
    
        # Check the shape of cv2_img:
        # Should output shape: (height, width, channels)
        st.write(cv2_img.shape)
    
def main():
    camera = cv2.VideoCapture(cv2.CAP_DSHOW+0)
    camera.set(3,640)
    camera.set(4,480)
    model_path = r"keras_model.h5"
    model = tensorflow.keras.models.load_model(model_path, compile=False)
    labelspath = r"labels.txt"
    
    frame_placeholder = st.empty()
    #frame_placeholder.image(frame, channels="RGB")
    
    while(camera.isOpened()):
        image = camera.read()

        size = (224, 224)
        image_resized = cv2.resize(image, size, interpolation=cv2.INTER_AREA)

        image_normalized = (image_resized.astype(np.float32) / 127.0) - 1
        image_reshaped = image_normalized.reshape((1, 224, 224, 3))

        prediction = model.predict(image_reshaped)
        result = np.argmax(prediction)

        with open(labels_path, 'rt', encoding="UTF8") as f:
            readLines = f.readlines()

        st.write(readLines[result])

        frame_placeholder.image(image, channels="RGB")
        if cv2.waitKey(100) == ord('q'):
            break

    cv2.destroyAllWindows()

