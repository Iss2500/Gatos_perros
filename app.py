<<<<<<< HEAD
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = Flask(__name__)
model = load_model("modelo_xception2_cats_vs_dogs.keras")

def preprocess_image(image):
    image = image.resize((180, 180))
    img_array = np.array(image) / 255.0
    return img_array[np.newaxis, ...]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            file = request.files["image"]
            if file and file.filename != "":
                image = Image.open(file).convert("RGB")
                processed = preprocess_image(image)
                prediction = model.predict(processed)[0][0]
                result = "Perro 🐶" if prediction > 0.5 else "Gato 🐱"
            else:
                result = "No se seleccionó ninguna imagen."
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result)

=======
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = Flask(__name__)
model = load_model("modelo_xception2_cats_vs_dogs.keras")

def preprocess_image(image):
    image = image.resize((180, 180))
    img_array = np.array(image) / 255.0
    return img_array[np.newaxis, ...]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            file = request.files["image"]
            if file and file.filename != "":
                image = Image.open(file).convert("RGB")
                processed = preprocess_image(image)
                prediction = model.predict(processed)[0][0]
                result = "Perro 🐶" if prediction > 0.5 else "Gato 🐱"
            else:
                result = "No se seleccionó ninguna imagen."
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

>>>>>>> dbe744e24fecbc9f3e30e22d3420d9eb1cfe15ee
