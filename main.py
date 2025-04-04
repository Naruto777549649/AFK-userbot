from pyrogram import Client
from config import API_ID, API_HASH, SESSION_STRING

app = Client("userbot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

# Import Features
import afk
import antitag
import commands

print("🚀 Userbot is Running!")
app.run()
