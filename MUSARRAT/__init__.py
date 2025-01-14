from MUSARRAT.core.bot import ISTKHAR
from MUSARRAT.core.dir import dirr
from MUSARRAT.core.git import git
from MUSARRAT.core.userbot import Userbot
from MUSARRAT.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ISTKHAR()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
