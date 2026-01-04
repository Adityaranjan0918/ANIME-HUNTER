class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7299916364"
    sudo_users = "8502796270"
    GROUP_ID = "-1002162362171"
    TOKEN = "8556952711:AAFDnPk4Qy-C5vultYjGacH95lJhlkoUNAE"
    mongo_url = "mongodb+srv://hinfi933:4kikA8i7RDzVsB1B@cluster0.xjntjrp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://files.catbox.moe/xrdug4.jpg", "https://envs.sh/6O.jpg"]
    SUPPORT_CHAT = "IND_CODER_SUPPORT"
    UPDATE_CHAT = "THE_IND_CODERS"
    BOT_USERNAME = "IND_AnimeHunterBot"
    CHARA_CHANNEL_ID = "-1002191895626"
    api_id = "24970704"
    api_hash = "503a6a88cdbca1a6cfec91728c2d7d2b"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
