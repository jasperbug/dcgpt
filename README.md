# DCGPT

Hello, I'm Buuuggyy, a VTuber, currently streaming on Twitch.
[https://www.twitch.tv/buuuggyy](https://www.twitch.tv/buuuggyy)

This simple code can connect GPT to your Discord, Twitch, Line, and Telegram. This version is optimized for Discord.

Here is an overview of the local code:

# A. Deployment Environment

1. Install Python
2. Set up the environment
```bash
pip install -r requirements.txt
```

# B. Create a Discord BOT

1. Visit the Discord Developer Portal: [https://discord.com/developers/applications](https://discord.com/developers/applications)
2. Click "New Application" and name your bot.
3. In the left menu, click "Bot" and then "Add Bot."
4. Under "Token," click "Copy" to copy your bot's token.
![image](https://github.com/jasperbug/dcgpt/assets/70250247/02f55d56-80a7-4679-9105-a5771d2f8de2)

# C. Set up OpenAI

1. Visit the OpenAI website: [https://openai.com](https://openai.com)
2. Register or log into your account.
3. In the dashboard, find and copy your API key.

# D. Create a .env File

1. Create a new file named `.env` in your project folder.
2. Add the following content to the file:
```env
DISCORD_TOKEN=your_discord_token
OPENAI_API_KEY=your_openai_api_key
```
Remember to replace with your actual token and key!

# E. Run the Program

```bash
python dcgpt.py
```

2. If everything is set up correctly, you should see a message saying "[Your Bot Name] has connected to Discord!"

# F. Invite the Bot to Your Discord Server

1. Go back to the Discord Developer Portal.
2. In the left menu, click "OAuth2" > "URL Generator."
3. In "Scopes," select "bot."
4. In "Bot Permissions," select the necessary permissions (at least "Send Messages" and "Read Messages/View Channels").
5. Copy the generated URL and open it in your browser.
6. Choose the server you want to invite the bot to and authorize.
