from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os
import gdown

app = Flask(__name__)

# URL de descarga directa desde Google Drive
url = "https://drive.google.com/uc?id=1C2t3sfb545KBht5meEH_M5fjuaq6Kios"
output = "modelo_xception2_cats_vs_dogs.keras"

# Descargar el modelo si no existe
try:
    if not os.path.exists(output):
        print("Descargando modelo desde Google Drive...")
        gdown.download(url, output, quiet=False)
except Exception as e:
    print(f"Error al descargar el modelo: {e}")

# Cargar el modelo
try:
    model = load_model(output)
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    model = None

# Preprocesamiento de imagen
def preprocess_image(image):
    image = image.resize((180, 180))
    img_array = np.array(image) / 255.0
    return img_array[np.newaxis, ...]

# Ruta principal
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            file = request.files["image"]
            if file and file.filename != "":
                image = Image.open(file).convert("RGB")
                processed = preprocess_image(image)
                if model:
                    prediction = model.predict(processed)[0][0]
                    probabilidad = round(prediction * 100, 2)
                    result = f"Perro 🐶 ({probabilidad}%)" if prediction > 0.5 else f"Gato 🐱 ({100 - probabilidad}%)"
                else:
                    result = "El modelo no se pudo cargar correctamente."
            else:
                result = "No se seleccionó ninguna imagen."
        except Exception as e:
            result = f"Error al procesar la imagen: {str(e)}"
    return render_template("index.html", result=result)

# Configuración para Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
