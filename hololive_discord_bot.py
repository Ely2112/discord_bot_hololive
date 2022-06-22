import asyncio
import discord
from discord.ext import commands
from googleapiclient.discovery import build



youtube = build('youtube', 'v3', developerKey = "private_key")  #private_key can get from google cloud

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!')
client = discord.Client()



@bot.event
async def on_ready():
  
    number_of_time = 0
    day = 0
    minute = 0
    hour = 0
  
    print("bot is ready")
    channel = bot.get_channel("checking_channel_id")      #checking channel is the channel where you can check the bot is working or not (please mute this channel)
    await channel.send("bot is ready")
  
    request = youtube.channels().list(part='statistics',id="UCJFZiqLMntJufDCHc6bQixg")
    response = request.execute()
    initial_number_of_video = response.get("items")[0].get("statistics").get("videoCount")
    initial_number_of_video =  int(initial_number_of_video)

    #initial_number_of_video -= 1           #check send video if different number of videos
    
    print(f"initial number of video: {initial_number_of_video}")
  
    while True:
        if minute == 60:
            minute += -60
            hour += 1
        if hour == 24:
            hour += -24
            day += 1
          
        time_message = f"{day}days and {hour}hours and {minute}mins"
        request = youtube.channels().list(part='statistics',id="UCJFZiqLMntJufDCHc6bQixg")
        response = request.execute()
        current_number_of_video = response.get("items")[0].get("statistics").get("videoCount")
        current_number_of_video =  int(current_number_of_video)
        print(f"current number of video: {current_number_of_video}")
        if initial_number_of_video == current_number_of_video:
            print(f"no new hololive anime {number_of_time+1}")
            channel = bot.get_channel("checking_channel_id")   #checking channel is the channel where you can check the bot is working or not (please mute this channel)
            await channel.send(f"no new hololive アニメ {time_message}")
            number_of_time += 1
            await asyncio.sleep(50)
          
        elif initial_number_of_video < current_number_of_video:
            number_of_time = 0
            day = 0
            minute = 0
            hour = 0
            initial_number_of_video += 1
            await asyncio.sleep(50)
          
            async def search(trial_time):
                request = youtube.search().list(
                    part="snippet",
                    channelId="UCJFZiqLMntJufDCHc6bQixg",
                    maxResults=1000,
                    order="date",
                    )
                response = request.execute()

                for i in range(40):
                    url = response.get("items")[i]("id")("videoId")
                    print(i)
                    print(url)
                    print("\n")
                    hololive_file = open("hololive_file.txt", "r")
                    video_data = hololive_file.read()
                    hololive_file.close()
        
                    if url == None:
                        continue
                    if url not in video_data:
                        channel = bot.get_channel("message_channel_id")       #message channel is the channel where you want to post the lastest video
                        await channel.send(f"https://www.youtube.com/watch?v={url}")
                        hololive_file = open("hololive_file.txt", "a")
                        hololive_file.write(f"https://www.youtube.com/watch?v={url}\n")
                        hololive_file.close()
                        break
                    if i == 39 and trial_time != 10:
                        await asyncio.sleep(10)
                        await search(trial_time+1)

            await search(0)
        print("---")
        print(f"initial number of video: {initial_number_of_video}")
        minute += 1
        await asyncio.sleep(10)



@bot.command() # ping-pong checking
async def ping(ctx):
    if ctx.author == client.user:
        return
    await ctx.send('pong')



bot.run("private_token")  #private_token can get from discord development

