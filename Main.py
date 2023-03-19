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



#Join Vc (Does Nothing After Joining...Yet)
@Client.tree.command(name="join", description="Join Vc")
async def join(interaction: discord.Interaction):
  channel = interaction.user.voice and interaction.user.voice.channel
  if not channel:
    await interaction.response.send_message("Join Vc bruh...")
    return
  await interaction.response.send_message("Joining...")
  await channel.connect()


  
#Leave Vc 
@Client.tree.command(name="leave", description="Leave Vc")
async def leave(interaction: discord.Interaction):
  if interaction.guild.voice_client:
    await interaction.guild.voice_client.disconnect()
    await interaction.response.send_message("Leaving...")
  else:
    await interaction.response.send_message(
      "I am not currently connected to a voice channel.")

    
    
#Adds sass to your message
@Client.tree.command(name="clap", description="Claps")
async def clap(interaction: discord.Interaction, msg: str):
    split_string = msg.split(" ")
    result = []
    for word in split_string:
        result.extend(list(word))
    output = ' :clap: '.join(result)
    await interaction.response.send_message(output)
    
    
    
#Roast
@Client.tree.command(name="roast", description="Roast")
async def roast(interaction: discord.Interaction, who: str):
    with open('txt_files/adj.txt', 'r') as f:
        W1 = f.readlines()
    with open('txt_files/noun.txt', 'r') as g:
        W2 = g.readlines()
        
  f = random.choice(W1).strip().lower()
  g = random.choice(W2).strip().lower()
  
  await interaction.response.send_message(f"{who} is a {f} {g}")
    
    
    
    
    
    
keep_alive.keep_alive()
Client.run(os.environ['Token'])
