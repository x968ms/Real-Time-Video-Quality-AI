import cv2
import numpy as np
import ffmpeg
from model import load_model, predict_quality

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return {"error": "Failed to open video"}

    quality_scores = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        score = predict_quality(frame)
        quality_scores.append(score)

    cap.release()
    avg_quality = sum(quality_scores) / len(quality_scores)
    return {"average_quality_score": avg_quality}
