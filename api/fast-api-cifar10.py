from fastapi import FastAPI, File, UploadFile, HTTPException
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Solo errores importantes
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from io import BytesIO
from PIL import Image, UnidentifiedImageError

app = FastAPI()

# cargamos el modelo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "proyecto_deep.h5")
modelo_cargado = load_model(MODEL_PATH)

# categorias de imagenes
class_names = [
    "Aviación (airplane)",
    "Automóviles (automobile)",
    "Pájaros (bird)",
    "Gatos (cat)",
    "Ciervos (deer)",
    "Perros (dog)",
    "Ranas (frog)",
    "Caballos (horse)",
    "Barcos (ship)",
    "Camiones (truck)"
]

# funcion que procece la imagen
def preprocess_image(img_bytes):
    img = Image.open(BytesIO(img_bytes)).resize((32, 32))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.0
    return img_array

allowed_types = ["image/jpeg", "image/png", "image/webp"]

# POST del api para poder procesar la imagen
@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=415,
            detail=f"Tipo de archivo '{file.content_type}' no soportado. Solo se permiten archivos de imagen."
        )

    img_bytes = await file.read()

    # Validar que sea una imagen válida
    try:
        img = Image.open(BytesIO(img_bytes))
        img.verify()
    except (UnidentifiedImageError, Exception):
        raise HTTPException(status_code=400, detail="Archivo no es una imagen válida.")

    # Reabrir la imagen (img.verify() la invalida)
    try:
        img = Image.open(BytesIO(img_bytes)).convert('RGB').resize((32, 32))
    except Exception:
        raise HTTPException(status_code=400, detail="No se pudo procesar la imagen.")

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.0

    predictions = modelo_cargado.predict(img_array)[0]
    top_indices = predictions.argsort()[-5:][::-1]

    results = []
    for i in top_indices:
        results.append({
            "class": class_names[i],
            "probability": float(predictions[i])
        })

    return {"predictions": results}