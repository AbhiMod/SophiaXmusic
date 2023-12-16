import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","6435225"))
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = getenv("BOT_TOKEN","5998139371:AAEpo8FJl8kRubKdgF2GzYBeJu6m_4JRsNk")
BOT_USERNAME = getenv("BOT_USERNAME" , "Sophia_x_MusicBot")
ASSUSERNAME = getenv("ASSUSERNAME" , "Sophia_Assistans")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ambot:ambot@ambot.onafiyb.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9999999999))
LOGGER_ID = int(getenv("LOGGER_ID",-1001840241140))
OWNER_ID = int(getenv("OWNER_ID", 6204761408))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AbhiMod/SophiaXmusic",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AMBOTYT")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AM_YTSUPPORT")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", "BQAKpqfh4wTwuB5SIUYCTfrsf--bLsLRme3UCj-n-Le3Qa9W22DzEaOjn-1j1enb1rNfwhPmK_eXZrENDXgEE12u20kl9DVcmnc_ciCUEQpj4pka3X8kK9PED4Jf66Sa641tx3ybD1LuOFvFNRRsPmX-bAqXoF3G-vyEI6FjQN8ouHFZOfOggK1g0iND5jABWD2vP6ATvw5xLDgKgvG2lphljd-J3dZLu5MDRI11HelkgiuO0XZ5lGN1IEyUR8NvUGb1Vb0RyS75vXWI6T1j13Rap1uGZpqCZ74FtpxFe3JjohJ2FALt1MD4ZMGhe_8JWTJ6PkYhgWbQWzordH_6DaaGAAAAAXFsS70A")
STRING2 = getenv("STRING_SESSION2", None)
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
