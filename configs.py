# (c) 

import os


class Config(object):
    API_ID = os.environ.get("API_ID", "14699743")
    API_HASH = os.environ.get("API_HASH", "0cef89ed2c8025c16d2b4d42a1b8d792")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5115356918:AAFH3T-1f2x4ZdikRQnNoOXXgonLUlwryAQ")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001625277697")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001788952875")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 4))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "5eb945e0fc5266091de2")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "gLV2QdvKaRhqlrJ")
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://SaviorGod:E4DY1YWGqvazdsvL@clustersavi.usbtdks.mongodb.net/?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 5059280908))

    START_TEXT = """
๐๐ข ๐๐๐๐ซ ๐๐ฌ๐๐ซ , ๐ ๐๐ฆ ๐๐ข๐๐๐จ ๐๐๐ซ๐ ๐ ๐๐จ๐ญ!
๐ ๐๐๐ง ๐๐๐ซ๐ ๐ ๐๐ฎ๐ฅ๐ญ๐ข๐ฉ๐ฅ๐ ๐๐ข๐๐๐จ๐ฌ ๐ข๐ง ๐๐ง๐ ๐๐ข๐๐๐จ. ๐๐ข๐๐๐จ ๐๐จ๐ซ๐ฆ๐๐ญ๐ฌ ๐ฌ๐ก๐จ๐ฎ๐ฅ๐ ๐๐ ๐ฌ๐๐ฆ๐.

๐๐๐๐ ๐๐ฒ @Savior_128
"""
    CAPTION = "แตโฑแตแตแต แตแตสณแตแตแต แตสธ @{}\n\n๐ผ๐๐๐ ๐๐ข @๐๐๐๐๐๐_๐ท๐ธ๐พ"
    PROGRESS = """
๐๐๐ซ๐๐๐ง๐ญ๐๐ ๐ : {๐}%
๐๐จ๐ง๐: {๐}
๐๐จ๐ญ๐๐ฅ: {๐}
๐๐ฉ๐๐๐: {๐}/๐ฌ
๐๐๐: {๐}
"""
