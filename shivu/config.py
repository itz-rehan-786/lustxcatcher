class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7775259302"
    sudo_users = ["7775259302"]
    GROUP_ID = "-1002279809564"
    TOKEN = "8076075071:AAF-2RVBTv2uHXX0bAEvoaKRQgcj2PpEc70"
    mongo_url = "mongodb+srv://waifuuu0786:fakedot@cluster0.uctgneu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/7e5398823512d307128a3.jpg", "https://telegra.ph/file/c45dcb207d81e97cb4f6a.jpg", "https://telegra.ph/file/0bc6d65878e8300fbf0f8.jpg", "https://telegra.ph/file/0afb45203ff162ee7227b.jpg"]
    SUPPORT_CHAT = "ur_hell_paradise"
    UPDATE_CHAT = "sungupdate"
    BOT_USERNAME = "sung_gamebot"
    CHARA_CHANNEL_ID = "-1002279809564"
    api_id = "27744639"
    api_hash = "a5e9da62bcd7cc761de2490c52c89ccf"

    

    

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
