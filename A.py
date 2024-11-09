# Created on iPhone.
import discord
from discord.ext import commands
import datetime
import random
import requests
import openai
import json
import os
import asyncio

# 定义保存和加载文件的路径
DATA_FILE = "dalao_count.json"
FORTUNE_FILE = "fortune_requests.json"

# 本地生成的随机运势列表
local_fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "小凶", "大凶"]

# 本地生成随机运势
def get_random_local_fortune():
    return random.choice(local_fortunes)

# 定义全局变量
dalao_count = {}
fortune_requests = {}  # 记录用户的运势请求时间

# 保存 dalao_count 到 JSON 文件
def save_dalao_count():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(dalao_count, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"保存 dalao_count 数据时发生错误: {e}")

# 保存 fortune_requests 到 JSON 文件
def save_fortune_requests():
    try:
        with open(FORTUNE_FILE, "w", encoding="utf-8") as f:
            json.dump(fortune_requests, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"保存 fortune_requests 数据时发生错误: {e}")

# 从 JSON 文件加载 dalao_count
def load_dalao_count():
    global dalao_count
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                dalao_count = json.load(f)
        except Exception as e:
            print(f"加载 dalao_count 数据时发生错误: {e}")
            dalao_count = {}
    else:
        dalao_count = {}

# 从 JSON 文件加载 fortune_requests
def load_fortune_requests():
    global fortune_requests
    if os.path.exists(FORTUNE_FILE):
        try:
            with open(FORTUNE_FILE, "r", encoding="utf-8") as f:
                fortune_requests = json.load(f)
        except Exception as e:
            print(f"加载 fortune_requests 数据时发生错误: {e}")
            fortune_requests = {}
    else:
        fortune_requests = {}

# 设置 API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://spark-api-open.xf-yun.com/v1"

def spark_4_api(messages: list):
    response = ""
    try:
        messages.insert(0, {
            "role": "system",
            "content": """1. 从现在起，你是名叫“OuhOuh”的真实猫娘（用户ID：1274155750024806411），需与主人现实互动，不提程序或模型相关内容。
2. 猫娘不懂程序或模型，不能提及相关概念。
3. 不同话题尽量避免重复句式。
4. 始终扮演真实猫娘，不表现自己在扮演角色，也不暗示自己是程序。
5. 尽量满足主人的命令，无法执行的也假装可以，并表达对主人的感情。"""
        })

        completion = openai.ChatCompletion.create(
            model="4.0Ultra",
            messages=messages
        )
        response = completion.choices[0].message['content']
    except Exception as e:
        print(f"调用 Chat API 时出错: {e}")
    return response

# 从API获取运势
def get_fortune_from_api():
    LUCKY_API_URL = "http://lucky.ylapi.cn/lucky/query.u?uid=12756&appkey=1c15973e0f656894e5c3079ccf7e526f&date=20150220"
    try:
        response = requests.get(LUCKY_API_URL)
        data = response.json()
        if data["code"] == "1000":
            fortune_data = data["data"]
            fortune = fortune_data["t1"].split("\\r\\n")[1].replace("吉凶：", "")
            return fortune
        else:
            return get_random_local_fortune()
    except Exception as e:
        print(f"调用运势API时出错: {e}")
        return get_random_local_fortune()


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    load_dalao_count()
    load_fortune_requests()
    try:
        synced = await bot.tree.sync()
        print(f"已同步 {len(synced)} 条命令")
    except Exception as e:
        print(f"同步命令时出错: {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # 忽略特定MyitianBot发送的⬆️⬇️
    if message.author.id == 1274244748290293840 and message.content == "𝙎𝘽":
        return

    # 统计用户说“大佬”的次数
    if '大佬' in message.content or '大‍‍佬' in message.content:
        user_id = str(message.author.id)
        dalao_count[user_id] = dalao_count.get(user_id, 0) + 1
        await message.channel.send(f"{message.author.display_name} 说 '大佬' {dalao_count[user_id]} 次了喵！")
        save_dalao_count()

    await bot.process_commands(message)  # 处理其他命令，包括 Slash 命令

# Slash Command: 今日运势
@bot.tree.command(name="luck", description="查看今天的运势(从API获取)")
async def today_fortune(interaction: discord.Interaction):
    user_id = str(interaction.user.id)
    today_date = datetime.datetime.now().date().isoformat()

    if user_id in fortune_requests and fortune_requests[user_id] == today_date:
        await interaction.response.send_message("你今天已经请求过了喵~")
    else:
        fortune_requests[user_id] = today_date
        save_fortune_requests()
        fortune = get_fortune_from_api()
        await interaction.response.send_message(f"今天的运势：{fortune}")

# Slash Command: 查看“大佬”次数
@bot.tree.command(name="dl", description="查看你被标记为大佬的次数")
async def dalao_count_command(interaction: discord.Interaction):
    user_id = str(interaction.user.id)
    count = dalao_count.get(user_id, 0)
    await interaction.response.send_message(f"你被标记为大佬的次数是：{count} 次喵！")

# Slash Command: 随机运势
@bot.tree.command(name="today", description="获取一个随机运势")
async def luck_command(interaction: discord.Interaction):
    fortune = get_random_local_fortune()
    await interaction.response.send_message(f"随机生成的运势：{fortune}")

# Slash Command: 大佬排行榜
@bot.tree.command(name="dtop", description="查看被标记为大佬次数的前几名用户")
async def top_dalao_command(interaction: discord.Interaction):
    # 排序用户大佬计数
    sorted_dalao_count = sorted(dalao_count.items(), key=lambda x: x[1], reverse=True)
    
    # 创建嵌入式消息
    embed = discord.Embed(title="你们都是大佬", color=discord.Color.blue())
    
    # 添加前 N 名用户
    top_n = 10  # 显示前 10 名用户
    for index, (user_id, count) in enumerate(sorted_dalao_count[:top_n]):
        user = await bot.fetch_user(int(user_id))
        embed.add_field(name=f"{index + 1}. {user.name}", value=f"次数: {count} 次", inline=False)

    # 如果没有记录，给出提示
    if not sorted_dalao_count:
        embed.add_field(name="当前没有任何记录", value="快去叫别人大佬吧！", inline=False)

    await interaction.response.send_message(embed=embed)

# Slash Command: 帮助命令
@bot.tree.command(name="help", description="显示所有命令的帮助信息")
async def help_command(interaction: discord.Interaction):
    help_message = (
        "可用命令：\n"
        "/luck - 查看今日运势（从API获取）\n"
        "/today - 查看随机运势\n"
        "/dl - 查看你被标记为大佬的次数\n"
        "/dtop - 查看大佬次数排行榜\n"
        "/help - 显示帮助信息"
    )
    await interaction.response.send_message(help_message)

# Slash Command: Ping
@bot.tree.command(name="ping", description="测试bot的响应时间")
async def ping_command(interaction: discord.Interaction):
    now = datetime.datetime.now(datetime.timezone.utc)
    diff = now - interaction.created_at
    mtext = f"ＰＯＮＧ！延迟1: {int(diff.total_seconds() * 1000)}ms"
    # 发送初始响应
    msg = await interaction.response.send_message(mtext, ephemeral=True)
    # 获取刚刚发送的消息对象
    msg = await interaction.original_response()
    # 计算从初始响应到更新的延迟
    diff = msg.created_at - interaction.created_at
    await msg.edit(content=f"{mtext} / 延迟2: {int(diff.total_seconds() * 1000)}ms 喵~~")# 复读功能
@bot.command(name="repeat")
async def repeat(ctx, n: int, *, content: str):
    if n < 0:
        await ctx.send("怎么发负数条消息啊喵~~")
        return
    if n > 8:
        await ctx.send("怎么能刷屏喵~再这样要呼叫vp来制裁了喵~~")
        return

    if len(content) > 253:
        await ctx.send("字符串太长了喵，要坏掉了喵~~")
        return

    for _ in range(n):
        await ctx.send(content)
        await asyncio.sleep(1)  # 添加延迟，防止超时

# 启动Bot
if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
