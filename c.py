import os

APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
DB_URI = os.environ.get("DB_URI")

from f import *
start_message = """<b>
Hey There, {}
๐ I Can Convert Link To ShortLink
๐ฌ Send Me Any Message With Links
๐ I Will Shorten All Links In It 
๐ Convert to <a href="https://shorturllink.in/member/tools/bookmarklet">ShortUrlLink</a> & <a href="https://playdisk.xyz/member/tools/bookmarklet">PlayDisk</a>

ยฉ๏ธPowered By @A2z_tech
</b>"""

start_button = [[Button.url("Join Channel โฅ๏ธ", "t.me/A2z_tech"), Button.inline("About Bot ๐ค", "abt")],
                [Button.inline("Connect To Shortner ๐", 'api')]]

api_message = """
<b>Which Shortner Do u Want to Connect To:</b>
"""
api_button = [[Button.url("Shorturllink.in", "https://shorturllink.in/member/tools/bookmarklet")],
              [Button.url("Playdisk.xyz", "https://playdisk.xyz/member/tools/bookmarklet")]]

about_text = """<b>



๐ค Name :  Shorurllink Link Convertor

๐  Language : Python3
๐ Library     : Telethon
๐ง๐ปโ๐ป Developer : @Ziko_0000

ยฉ๏ธPowered By @A2z_tech
</b>"""
