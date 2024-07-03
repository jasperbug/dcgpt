# DCGPT
你好,我是你家蟲子vtuber,
目前在twitch開台
https://www.twitch.tv/buuuggyy
這個間單的code可以將gpt串接近你的dc, twitch, line, telegram
目前這份是針對discord進行優化的版本
以下是在本地端運行的程式碼概要

# A. 部署環境
1. 安裝python
2. 部署環境
```
pip install -r requirements.txt
```

# B. 創建Discord BOT
1. 訪問 Discord 開發者:[https://t.co/tP3VMvmqOi](https://discord.com/developers/applications)
2. 點擊 "New Application",為您的機器人取個名字
3. 在左側菜單中點擊 "Bot",然後點擊 "Add Bot"
4. 在 "Token" 下方,點擊 "Copy" 來複製您的機器人令牌 (Token)
![image](https://github.com/jasperbug/dcgpt/assets/70250247/02f55d56-80a7-4679-9105-a5771d2f8de2)


# C. 設置OpenAI
1. 訪問OpenAI網站https://openai.com
2. 註冊或登錄您的帳戶
3. 在儀表板中找到並複製您的 API 密鑰

# D. 創建 .env 文件 
1. 在您的專案文件夾中創建一個名為 `.env` 的新文件
2. 在文件中添加以下內容:    
```    
DISCORD_TOKEN=你的Discord令牌    
OPENAI_API_KEY=你的OpenAI API密鑰    
```    
記得替換為您實際的令牌和密鑰!

# E. 運行程式
```
python dcgpt.py
```

2. 如果一切正常,您應該會看到 "[你的機器人名稱] 已連接到 Discord!" 的消息

# F. 邀請機器人到您的 Discord 伺服器
1. 回到 Discord 開發者
2. 在左側菜單中點擊 "OAuth2" > "URL Generator"
3. 在 "Scopes" 中選擇 "bot"
4. 在 "Bot Permissions" 中選擇需要的權限(至少需要 "Send Messages" 和 "Read Messages/View Channels")
5. 複製生成的 URL 並在瀏覽器中打開
6. 選擇您想邀請機器人加入的伺服器,然後授權
