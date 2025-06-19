class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7657218453"
    sudo_users = "7135097212"
    GROUP_ID = -1002746226173
    TOKEN = "7808483233:AAFDNr1xW2fv112Hik7dM2Bh_wrVdDVktUM"
    mongo_url = "mongodb+srv://hinfi933:4kikA8i7RDzVsB1B@cluster0.xjntjrp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://files.catbox.moe/xrdug4.jpg", "https://envs.sh/6O.jpg"]
    SUPPORT_CHAT = "SANDVILLAGE"
    UPDATE_CHAT = "Akatsuki_airelin"
    BOT_USERNAME = "Grabbersvbot"
    CHARA_CHANNEL_ID = "-1002496865311"
    api_id = 10658015
    api_hash = "a0087bca748f86698c53d291c9e5b3af"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
