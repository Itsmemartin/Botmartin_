import discord, datetime, random, aiohttp, os
import keep_alive
from discord.utils import get
import pickle
from pytz import timezone
import json
import time
import urllib
from discord import Webhook
from discord import guild
from discord.ext import commands
from discord.ext import tasks

Meme = random.choice([
  'terriblefacebookmemes', 'funny', 'crappyoffbrands', 'trippinthroughtime',
  '4chan', 'Meanjokes', 'suicidebywords', 'puns', 'Wholesomememes',
  'Wholesomememes', 'cursedcomments'
])

ST = time.time()
