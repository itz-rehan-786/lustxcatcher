class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5116239739"
    sudo_users = ["5116239739"]
    GROUP_ID = "-1002158051312"
    TOKEN = "7246514260:AAGRYq6AIHGjKm1-Vbt5UEgeYEcMRDpDm58"
    mongo_url = "mongodb+srv://Slavewaifu:bot@cluster0.sx51gw3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/7e5398823512d307128a3.jpg", "https://telegra.ph/file/c45dcb207d81e97cb4f6a.jpg", "https://telegra.ph/file/0bc6d65878e8300fbf0f8.jpg", "https://telegra.ph/file/0afb45203ff162ee7227b.jpg"]
    SUPPORT_CHAT = "bwnsnansn67"
    UPDATE_CHAT = "bwnsnansn67"
    BOT_USERNAME = "Slave_grabber_bot"
    CHARA_CHANNEL_ID = "-1002158051312"
    api_id = "27744639"
    api_hash = "a5e9da62bcd7cc761de2490c52c89ccf"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
