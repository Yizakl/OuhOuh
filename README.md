# OuhOuh - Discord Bot

OuhOuh 是一个基于 Discord.py 库开发的 Discord 机器人。它能够实现多种互动功能，包括记录用户被称为“大佬”的次数、查看用户的运势以及生成随机的运势信息等。该机器人还提供了多种命令和互动方式，用户可以通过简单的指令与机器人进行互动。

## 主要功能

- **大佬统计**：记录和显示用户在聊天中被称为“大佬”的次数。
- **运势查询**：用户可以查询自己的今日运势或获取随机运势。
- **大佬排行榜**：显示在频道中被称为“大佬”最多的用户。
- **重复消息**：可以让机器人重复指定次数的消息。
- **其他命令**：包括帮助命令和 ping 测试等。

## 安装与设置

1. **克隆项目**

   首先，克隆项目到本地：

   ```bash
   git clone https://github.com/Yizakl/OuhOuh.git
   cd OuhOuh
   ```

2. **创建虚拟环境**

   推荐使用虚拟环境来管理依赖包。你可以使用以下命令创建并激活虚拟环境：

   ```bash
   python -m venv .venv  # 创建虚拟环境
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **安装依赖**

   安装项目所需的 Python 库：

   ```bash
   pip install -r requirements.txt
   ```

   项目依赖包括：
   - `discord.py`：用于与 Discord API 进行交互。
   - `openai`：用于与 OpenAI API 进行交互，提供运势查询服务。
   - `requests`：用于调用外部API来获取运势数据。
   - 其他常见的 Python 库。

4. **设置环境变量**

   为了保护 API 密钥等敏感信息，你需要在本地创建一个 `.env` 文件，并添加以下内容：

   ```env
   DISCORD_TOKEN=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```

   - `DISCORD_TOKEN`：你的 Discord 机器人 Token。
   - `OPENAI_API_KEY`：你的 OpenAI API 密钥（如果使用 OpenAI API）。

   可以通过 [Discord 开发者门户](https://discord.com/developers/applications) 获取 Discord 机器人 Token。

5. **运行机器人**

   使用以下命令启动机器人：

   ```bash
   python OuhOuh.py
   ```

   机器人成功启动后，你应该能看到如下信息：

   ```bash
   Logged in as OuhOuhBot!
   ```

## 使用方法

### 1. `/luck` - 查看今日运势

这个命令会从外部 API 获取今日的运势，并显示给用户。

```bash
/luck
```

### 2. `/today` - 随机运势

生成并显示一个随机的运势，用户每次都能看到不同的运势内容。

```bash
/today
```

### 3. `/dl` - 查看你被标记为“大佬”的次数

这个命令会显示用户在当前频道中被称为“大佬”的次数。

```bash
/dl
```

### 4. `/dtop` - 查看大佬排行榜

查看当前频道中被称为“大佬”最多的前几名用户。

```bash
/dtop
```

### 5. `/help` - 显示帮助信息

列出所有可用的命令和它们的功能说明。

```bash
/help
```

### 6. `/ping` - 测试机器人的响应时间

返回机器人与 Discord 服务器之间的延迟。

```bash
/ping
```

### 7. `!repeat` - 重复消息

让机器人重复发送指定次数的消息。例如：

```bash
!repeat 5 Hello, world!
```

这会让机器人发送 5 次 “Hello, world!”。

## 配置文件

### `dalao_count.json`

该文件用于保存每个用户被称为“大佬”的次数。每次用户在聊天中说“大佬”，计数就会增加。

### `fortune_requests.json`

用于记录每个用户请求运势的日期，避免同一天重复请求。

## 贡献

欢迎提交问题、提建议或贡献代码！若要贡献，请遵循以下步骤：

1. Fork 这个仓库。
2. 创建一个新的分支 (`git checkout -b feature-branch`)。
3. 提交你的更改 (`git commit -am 'Add feature'`)。
4. 推送到分支 (`git push origin feature-branch`)。
5. 创建一个新的 Pull Request。

## 许可

本项目使用 [MIT 许可证](LICENSE)。详细内容请查看 `LICENSE` 文件。




