# discord_bot_hololive
Automatically send latest Youtube video to discord channel


4 things to be added by yourself:
  1. line 8, private_key
      create a api key from google cloud api, 
      you can read "Before you start step 1" from https://developers.google.com/youtube/v3/getting-started 
      
  2. line 25 and line 53, checking_channel_id
      create a checking discord channel and get its channel id,  please mute this channel, as it will send a message every minute
      you can read https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-
  
  3. line 87, message_channel_id
      create a message discord channel and get its channel id, this is channel where the bot will send the latest Youtube video
      you can read https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-
      
   4. line 113, private_token
       create a discord bot token from discord developer portal
       you can read https://www.writebots.com/discord-bot-token/


*** You need to host this bot 24/7
*** You need to include a "hololive_file.txt" file in the same folder, and update the txt by adding new video url


This bot is desgined to send latest hololive ホロライブ - VTuber Group Youtube video,
you can change to send other youtube channel videos by changing id or channelId on line 28, 46, and 69 to the youtube channel id
