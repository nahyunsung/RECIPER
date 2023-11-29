import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

def detect_objects(image, model):
    image_resized = tf.image.resize(image, (224, 224))
    image_normalized = (tf.cast(image_resized, tf.float32) / 127.0) - 1.0
    image_reshaped = tf.reshape(image_normalized, (1, 224, 224, 3))

    # Make predictions
    prediction = model.predict(image_reshaped)
    result = np.argmax(prediction)

    return result

def app():
    st.write('Camera')
    
    img_file_buffer  = st.camera_input("Take a picture")
    
    model_path = r"keras_model.h5"
    model = tf.keras.models.load_model(model_path, compile=False)
    labels_path = r"labels.txt"
    
    if img_file_buffer  is not None:
        # PIL Image로 변환
        pil_image = Image.open(img_file_buffer)

        # PIL Image를 NumPy 배열로 변환
        img_array = np.array(pil_image)

        # NumPy 배열을 TensorFlow 텐서로 변환
        img_tensor = tf.convert_to_tensor(img_array)

        prediction_result = detect_objects(img_tensor , model)

        with open(labels_path, 'rt', encoding="UTF8") as f:
            readLines = f.readlines()
        
        
        
        st.write(readLines[prediction_result][0])
