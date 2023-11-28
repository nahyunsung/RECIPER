import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
from PIL import Image
import cv2
import tensorflow.keras
import tensorflow as tf
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
    
    model_path = r"keras_model.h5"
    model = tf.keras.models.load_model(model_path, compile=False)
    labels_path = r"labels.txt"
    
    if img_file_buffer is not None:
        # To read image file buffer as a 3D uint8 tensor with TensorFlow:
        bytes_data = img_file_buffer.getvalue()
        img_tensor = tf.image.decode_image(bytes_data, channels=3)

        prediction_result = detect_objects(img_tensor, model)

        with open(labels_path, 'rt', encoding="UTF8") as f:
            readLines = f.readlines()
        
        # Check the type of img_tensor:
        # Should output: <class 'tensorflow.python.framework.ops.EagerTensor'>
        st.write(type(img_tensor))
    
        # Check the shape of img_tensor:
        # Should output shape: (height, width, channels)
        st.write(img_tensor.shape)
        
        st.write(readLines[result])

def detect_objects(image, model):
    image_resized = tf.image.resize(np.array(image), (224, 224))
    image_normalized = (tf.cast(image_resized, tf.float32) / 127.0) - 1.0
    image_reshaped = tf.reshape(image_normalized, (1, 224, 224, 3))

    # Make predictions
    prediction = model.predict(image_reshaped)
    result = np.argmax(prediction)

    return result


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

