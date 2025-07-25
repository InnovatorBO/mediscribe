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
    """Load character mappings from pickle file"""
    try:
        with open(char_map_path, "rb") as f:
            mappings = pickle.load(f)
        char_to_num = mappings["char_to_num"]
        num_to_char = mappings["num_to_char"]
        return char_to_num, num_to_char
    except FileNotFoundError:
        raise Exception(f"Character mappings file not found at {char_map_path}")
    except Exception as e:
        raise Exception(f"Error loading character mappings: {str(e)}")

def preprocess_image(image_path):
    """Preprocess image for OCR model"""
    try:
        img = Image.open(image_path).convert("L")  # Convert to grayscale
        img = img.resize((IMG_WIDTH, IMG_HEIGHT), Image.BILINEAR)
        img = np.array(img).astype(np.float32) / 255.0  # Normalize
        img = np.expand_dims(img, axis=-1)  # Add channel dimension
        return img
    except Exception as e:
        raise Exception(f"Error preprocessing image: {str(e)}")

def predict_image(image_path):
    """
    Predict medicine name from image using OCR model
    Returns: tuple of (medicine_name, confidence)
    """
    try:
        # Load model
        if not os.path.exists(MODEL_PATH):
            raise Exception(f"Model file not found at {MODEL_PATH}")
        
        model = load_model(MODEL_PATH, compile=False)
        
        # Load character mappings
        _, num_to_char = load_char_mappings()
        
        # Preprocess image
        img = preprocess_image(image_path)
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        
        # Make prediction
        preds = model.predict(img, verbose=0)
        pred = preds[0]
        
        # Decode CTC output
        input_len = np.ones((1,)) * pred.shape[0]
        decoded, _ = K.ctc_decode(
            np.expand_dims(pred, axis=0), 
            input_length=input_len, 
            greedy=True
        )
        
        # Convert to readable text
        out = K.get_value(decoded[0])[0]
        medicine_name = ''.join([num_to_char.get(i, '') for i in out if i != -1])
        
        # Calculate confidence
        confidence = float(np.mean(np.max(pred, axis=-1)))
        
        # Clean up medicine name
        medicine_name = medicine_name.strip()
        if not medicine_name:
            medicine_name = "Unable to detect medicine name"
            confidence = 0.0
        
        return medicine_name, confidence
        
    except Exception as e:
        raise Exception(f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Standalone Medical OCR Prediction")
    parser.add_argument("--image", type=str, required=True, help="Path to image for prediction")
    args = parser.parse_args()
    
    try:
        name, conf = predict_image(args.image)
        print(f"Predicted Medicine Name: {name}")
        print(f"Confidence: {conf:.4f}")
    except Exception as e:
        print(f"Error: {e}")