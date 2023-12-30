import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","6435225"))
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = getenv("BOT_TOKEN","5998139371:AAE9TXyrbJpODDPC95sICPBNtYYJxbR-WVk")
BOT_USERNAME = getenv("BOT_USERNAME" , "Sophia_x_MusicBot")
ASSUSERNAME = getenv("ASSUSERNAME" , "Sophia_Assistans")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://SophiaXmusic:cBTsyRXOozyWgDHR@sophiaxmusic.yasayhz.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9999999999))
LOGGER_ID = int(getenv("LOGGER_ID",-1001840241140))
OWNER_ID = int(getenv("OWNER_ID", "5360305806"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AbhiMod/SophiaXmusic",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AMBOTYT")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+-wkgY_fr_I44MGY1")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", "BQCK52hBKd6MlL8gSfGneOnRDIaGGr5k8xry8sFTeEg5pd_deL9OnCBZJnOhpfev9nPX5mqBtdxJW7Sa_ktYDAc9erUNFEIAxUAqlntM7o4L16MbPwQGj6Nqi6I4x5oyLA0cgZPmsWCF2uQLV49Nnwvucwqto5HE15TPND0juwODQAXTcexyW5a_qIrngXi_PRQt231eIGuJZqbZwOW_8u_RCGMJ2xEAKb70lAf4gdsDq4LPmJxHhvtAHeKFZdZL5iGgdPmPlw3ouu0jNJzGXCXIXPGzT2mg1-sjtU1T2W1v9hR8xDGaGnfUrQW9oo4HNV7mgzxHVMQG9IwyDnwClu_FAAAAAXFsS70A")
STRING2 = getenv("STRING_SESSION2", "BAC5I-KY_H0HIn9FEB1pNUwk5Ul445jzylzCmDfVXyGh5VGrxTGhJce5NR5ly45IubEM5dYs0lqfGewLso_6-Lw--xCRakULPlTKfbVrb3pY4lmtIMgz4YbJcrnS8qTDKY_fe3x6uMGi3lcQ5H6XeLDpqiRuPKBtxSEbdwZZ0lxs6byUlqLwwwhAXBWYB6ipZxYPktn-ZTcxLJXFI6-KZP60ld8JOufHWEGp1LTyWsdM3Xd-AKYEYD274Ny2DtYvMCumtfPpT1BVI4CiOrtFffCgu_6sSF3R-Om2ZazgTZahp8Oo30j-4D-D6509Uzj22_6X6SeDfui5DXe5vLZv0CJUAAAAAVxayD8A")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/e7a8c2b902d3e2fefd4ff.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/e7a8c2b902d3e2fefd4ff.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/e7a8c2b902d3e2fefd4ff.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/48f39202823b358203234.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/e7a8c2b902d3e2fefd4ff.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/e7a8c2b902d3e2fefd4ff.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
