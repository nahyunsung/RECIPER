import streamlit as st
import tensorflow as tf
import numpy as np

def detect_objects(image, model):
    image_resized = tf.image.resize(np.array(image), (224, 224))
    image_normalized = (tf.cast(image_resized, tf.float32) / 127.0) - 1.0
    image_reshaped = tf.reshape(image_normalized, (1, 224, 224, 3))

    # Make predictions
    prediction = model.predict(image_reshaped)
    result = np.argmax(prediction)

    return result

def app():
    st.write('Camera')
    
    camera_frame, taken = st.camera_input("Take a picture")
    
    model_path = r"keras_model.h5"
    model = tf.keras.models.load_model(model_path, compile=False)
    labels_path = r"labels.txt"
    
    if taken and camera_frame is not None:
        st.write('Camera')
        # To read image file buffer as a 3D uint8 tensor with TensorFlow:
        bytes_data = img_file_buffer.getvalue()
        img_tensor = tf.image.decode_image(camera_frame, channels=3)

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


