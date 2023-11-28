import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
from PIL import Image
import cv2
import tensorflow.keras

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")

def app():
    st.write('Camera')
    #webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
    #main()

    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    stop_button_pressed = st.button("Stop")
    while cap.isOpened() and not stop_button_pressed:
        ret, frame = cap.read()
        if not ret:
            st.write("Video Capture Ended")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame,channels="RGB")
        if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
            break
    cap.release()
    cv2.destroyAllWindows()
    
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

