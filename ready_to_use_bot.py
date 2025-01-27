
import os
from pyrogram import Client

# Configuration de base
API_ID = 123456  # Remplacez par votre API ID
API_HASH = "your_api_hash_here"  # Remplacez par votre API Hash
SESSION_STRING = "your_session_string_here"  # Session string fournie

# Initialisation du client Pyrogram
app = Client(name="bot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

# Message d'accueil
@app.on_message()
def welcome_message(client, message):
    if message.text.lower() == "/start":
        message.reply_text("Bonjour ! Votre bot est maintenant prêt à fonctionner.")

# Lancement du bot
print("Le bot est en cours d'exécution...")
app.run()
