from pyrogram import Client, filters
from config import OWNER_ID

afk_mode = True  # Default AFK mode enabled

@Client.on_message(filters.private & ~filters.me)
async def auto_afk(client, message):
    if afk_mode:
        await message.reply_text("🚀 『𝗚𝗢𝗞𝗨』 is AFK right now. Please don’t disturb.")

@Client.on_message(filters.command("afk") & filters.me)
async def toggle_afk(client, message):
    global afk_mode
    afk_mode = not afk_mode
    await message.reply_text(f"AFK Mode {'Enabled ✅' if afk_mode else 'Disabled ❌'}")
