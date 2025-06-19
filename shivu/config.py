class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7657218453"
    sudo_users = "7135097212"
    GROUP_ID = -1002746226173
    TOKEN = "7808483233:AAFDNr1xW2fv112Hik7dM2Bh_wrVdDVktUM"
    mongo_url = "mongodb+srv://hinfi933:4kikA8i7RDzVsB1B@cluster0.xjntjrp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://files.catbox.moe/xrdug4.jpg", "https://envs.sh/6O.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
