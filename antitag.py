from pyrogram import Client, filters

antitag = True  # Default ON

@Client.on_message(filters.mentioned & ~filters.me)
async def tag_response(client, message):
    if antitag:
        await message.reply_text("🚫 Don't tag me unnecessarily!")

@Client.on_message(filters.command("antitag") & filters.me)
async def enable_antitag(client, message):
    global antitag
    antitag = True
    await message.reply_text("✅ Anti-Tag mode enabled.")

@Client.on_message(filters.command("antitag off") & filters.me)
async def disable_antitag(client, message):
    global antitag
    antitag = False
    await message.reply_text("❌ Anti-Tag mode disabled.")
