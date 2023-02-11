from Things import *

Client = commands.Bot(intents=discord.Intents.all(), command_prefix='!')



#onReady
@Client.event
async def on_ready():
  await Client.change_presence(status=discord.Status.dnd)
  print(f'we have logged in as {Client.user}.')
  synced = await Client.tree.sync()
  print(f'{str(len(synced))} commands synced')



#Latency
@Client.tree.command(name='ping', description='pong')
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message(
  content=f"pong, {round(Client.latency, 1)}")



#All channel names and id
@Client.tree.command(name='channel', description='get all channel names and ids')
async def channel(interaction: discord.Interaction):
  hell = Client.get_channel(1045341148752916580)
  await interaction.response.send_message(content='sending names')
  for server in Client.guilds:
    for channel in server.channels:
      if str(channel.type) == 'text':
         await interaction.channel.send(content= f"{channel}: {channel.id}")



#Uptime
@Client.tree.command(name='uptime', description="how long the bot has been online")
async def uptime(interaction: discord.Interaction):
  ET = time.time()
  d = divmod(ET-ST,86400)
  h = divmod(d[1],3600) 
  m = divmod(h[1],60) 
  s = m[1]
  UpTime = discord.Embed(title="Uptime", description='**%d**d **%d**h **%d**m **%d**s' % (d[0],h[0],m[0],s), color=discord.Color.green())
  await interaction.response.send_message(embed=UpTime)


  
#Memes
@Client.tree.command(name='meme', description="meme")
async def meme(interaction: discord.Interaction):
  embed = discord.Embed(title="", description="")
  async with aiohttp.ClientSession() as cs:
    async with cs.get(f'https://www.reddit.com/r/{Meme}/new.json?sort=top') as r:
      res = await r.json()
      embed.title = f"r/{Meme}"
      embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
      await interaction.response.send_message(embed=embed)


                                   
keep_alive.keep_alive()
Client.run(os.environ['Botmartin'])
