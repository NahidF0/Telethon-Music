import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "17394955"))
    API_HASH = os.environ.get("API_HASH", "db6d0a4fedf7c518bc0474bb4d898b30")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5713188936:AAGWIqJCfOk-8kKH52moFBBwy7_ipcLpdqM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJwBu4SpcfMtczGFjnWCRIp6f85dRCXBsyly5ArT12TeyB0lbviKvqXPNYHKDgcaNWdhtpUqE3ENoyBJ_gMcSmehEyCcvaRMuu8Z0Ia27wK8eD6y56zwmkQno1xtxVx8X7A-ec2t0n_cXdXW1nOspz006bav9_UVFMjqTASyhiJa3fDMMwy5SVqWWU_4g2Om-CWNWsG71tcuKsm2383NOveKTRPaTQg-aG0-mX2G_CkhLHDgfSs7SWV_Epd7uSHtNJTDJ5Y8VxC-CKTbpsnS5sFABN-LUkZYemSiz8QAR_GQ7-vBvGSGCQbBzEPkrFhhFn_T9QR-TWFoAl6alVUnBmvZbMQ=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "VCSongBot")
    SUPPORT = os.environ.get("SUPPORT", "DevenSupport")
    CHANNEL = os.environ.get("CHANNEL", "DevenUpdate")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID")) # required
