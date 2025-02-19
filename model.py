import tensorflow as tf
import numpy as np

MODEL_PATH = "model/video_quality_model.h5"

def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

def predict_quality(frame):
    frame_resized = tf.image.resize(frame, (224, 224)) / 255.0
    frame_resized = np.expand_dims(frame_resized, axis=0)
    score = model.predict(frame_resized)[0][0]
    return float(score)
