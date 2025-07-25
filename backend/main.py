import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
from PIL import Image
import pickle

# --- CONFIGURATION ---
MODEL_PATH = os.path.join("models", "ocr_model_prediction.keras")
CHAR_MAP_PATH = os.path.join("models", "char_mappings.pkl")
IMG_HEIGHT = 128
IMG_WIDTH = 384

def load_char_mappings(char_map_path=CHAR_MAP_PATH):
    with open(char_map_path, "rb") as f:
        mappings = pickle.load(f)
    char_to_num = mappings["char_to_num"]
    num_to_char = mappings["num_to_char"]
    return char_to_num, num_to_char

def preprocess_image(image_path):
    img = Image.open(image_path).convert("L")
    img = img.resize((IMG_WIDTH, IMG_HEIGHT), Image.BILINEAR)
    img = np.array(img).astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=-1)
    return img

def predict_image(image_path):
    model = load_model(MODEL_PATH, compile=False)
    _, num_to_char = load_char_mappings()
    img = preprocess_image(image_path)
    img = np.expand_dims(img, axis=0)
    preds = model.predict(img)
    pred = preds[0]
    input_len = np.ones((1,)) * pred.shape[0]
    decoded, _ = K.ctc_decode(np.expand_dims(pred, axis=0), input_length=input_len, greedy=True)
    out = K.get_value(decoded[0])[0]
    medicine_name = ''.join([num_to_char.get(i, '') for i in out if i != -1])
    confidence = float(np.mean(np.max(pred, axis=-1)))
    return medicine_name, confidence

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Standalone Medical OCR Prediction")
    parser.add_argument("--image", type=str, required=True, help="Path to image for prediction")
    args = parser.parse_args()
    name, conf = predict_image(args.image)
    print(f"Predicted Medicine Name: {name}")
    print(f"Confidence: {conf:.4f}")
