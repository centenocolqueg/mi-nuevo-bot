import os
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🟢 CENTRAL DE AUDITORÍA OPERATIVA ACTIVE"

if __name__ == "__main__":
    # Arranca tu archivo bot.py original en segundo plano
    subprocess.Popen(["python", "bot.py"])
    
    # Arranca el servidor web en el puerto que Render exige obligatoriamente
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
