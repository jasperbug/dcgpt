import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from openai import OpenAI

# 載入 .env 文件中的環境變量
load_dotenv()

# 從環境變量中獲取令牌和密鑰
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# 初始化 Discord 客戶端
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# 初始化 OpenAI 客戶端
client = OpenAI(api_key=OPENAI_API_KEY)

def read_prompt_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt_content = file.read()
    return prompt_content

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='gpt')
async def gpt_command(ctx, *, prompt):
    try:
        # 從本地文件讀取 prompt
        prompt_content = read_prompt_from_file('prompt.txt')  # 確保這個文件存在並且在正確位置
        
        # 獲取使用者名稱
        user_name = ctx.author.name
        
        response = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=500, 
            messages=[
                {"role": "system", "content": prompt_content},
                {"role": "user", "content": prompt}
            ]
        )
        
        # 在回覆前加上使用者名稱
        reply = f"{user_name}：{response.choices[0].message.content}"
        
        await ctx.send(reply)
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# 檢查是否成功載入環境變量
if not DISCORD_TOKEN or not OPENAI_API_KEY:
    print("Error: Missing environment variables. Please check your .env file.")
else:
    bot.run(DISCORD_TOKEN)
