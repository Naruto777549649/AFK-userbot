from pyrogram import Client, filters

@Client.on_message(filters.command("ban") & filters.me)
async def ban_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user's message to ban.")
    
    user_id = message.reply_to_message.from_user.id
    await client.kick_chat_member(message.chat.id, user_id)
    await message.reply_text(f"🚫 User {user_id} banned.")

@Client.on_message(filters.command("unban") & filters.me)
async def unban_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user's message to unban.")

    user_id = message.reply_to_message.from_user.id
    await client.unban_chat_member(message.chat.id, user_id)
    await message.reply_text(f"✅ User {user_id} unbanned.")
