import os
import asyncio
from flask import Flask
import bot

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "🟢 CENTRAL DE AUDITORÍA OPERATIVA - PROXYS ACTIVOS"

async def run_flask():
    from werkzeug.serving import make_server
    port = int(os.environ.get("PORT", 10000))
    server = make_server("0.0.0.0", port, flask_app, threaded=True)
    print(f"Servidor Web iniciado en el puerto {port}")
    while True:
        server.handle_request()
        await asyncio.sleep(0.5)

async def main():
    telegram_app = bot.configurar_aplicacion()
    if not telegram_app:
        print("Error: No se configuró el token de Telegram.")
        return

    await telegram_app.initialize()
    await telegram_app.updater.start_polling()
    await telegram_app.start()
    print("Bucle de Telegram conectado con éxito.")

    await asyncio.gather(
        run_flask(),
        asyncio.Event().wait()
    )

if __name__ == "__main__":
    asyncio.run(main())
