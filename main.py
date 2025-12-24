from telethon import TelegramClient, events
import asyncio

# আপনার এপিআই তথ্য
api_id = 27318719 
api_hash = '0d964023416a995f4c479240445feae5' 

# যে সোর্সগুলো আপনি দিয়েছেন
source_groups = [
    'TechUniverseotp', 
    'Allnumbersultra_Bot', 
    'black_all_otp', 
    'NxTraDerOfficial'
]

# আপনার নিজের গ্রুপ যেখানে ওটিপি আসবে
target_group = 'otpbotus2' 

client = TelegramClient('colab_session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_groups))
async def handler(event):
    if event.message.text:
        # কোন গ্রুপ থেকে ওটিপি আসছে সেটি চিহ্নিত করা
        sender_chat = await event.get_chat()
        group_name = getattr(sender_chat, 'title', 'Bot/Group')
        
        # আপনার গ্রুপে পাঠানোর মেসেজ ফরম্যাট
        final_message = f"🔔 **নতুন ওটিপি আপডেট!**\n\n🏢 **উৎস:** {group_name}\n💬 **মেসেজ:**\n`{event.message.text}`"
        
        await client.send_message(target_group, final_message)
        print(f"✅ {group_name} থেকে মেসেজ পাঠানো হয়েছে!")

print("🤖 মাল্টি-সোর্স ওটিপি ফরোয়ার্ডার সচল হয়েছে...")

# এটি ২৪ ঘণ্টা সচল রাখার জন্য Render-এ ব্যবহার করুন
client.start()
client.run_until_disconnected()
