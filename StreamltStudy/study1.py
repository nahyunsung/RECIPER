import streamlit as st
import cv2

def app():

    camera = cv2.VideoCapture(0)
    camera.set(3,640)
    camera.set(4,480)
    #model_path = r"ai\keras_model.h5"
    #model = tensorflow.keras.models.load_model(model_path)
    #labels_path = r"ai\labels.txt"

    while(camera.isOpened()):
        _, image = camera.read()

        size = (224, 224)
        image_resized = cv2.resize(image, size, interpolation=cv2.INTER_AREA)

        image_normalized = (image_resized.astype(np.float32) / 127.0) - 1
        image_reshaped = image_normalized.reshape((1, 224, 224, 3))

        #prediction = model.predict(image_reshaped)
        #result = np.argmax(prediction)
        
        with open(labels_path, 'rt', encoding="UTF8") as f:
            readLines = f.readlines()
        
        print(readLines[result])
        
        cv2.imshow("camera out", image)
        #if cv2.waitKey(100) == ord('q'):
        #    break
    
    cv2.destroyAllWindows()
