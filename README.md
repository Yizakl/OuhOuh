# OuhOuh Discord Bot

一个基于 Discord.py 框架构建的 Discord 机器人，包含一些有趣的功能，如“今天的运势”、“大佬统计”等，供用户互动娱乐使用。

## 功能

1. **今日运势**：通过 API 获取用户的运势，支持每日查询一次。
2. **随机运势**：从本地生成的运势列表中随机选择并显示。
3. **大佬统计**：记录用户在聊天中提到“*大佬*”的次数。
4. **大佬排行榜**：显示被称为“大佬”的次数排行榜。
5. **复读功能**：允许用户让机器人重复指定内容若干次。
6. **Ping 测试**：测试机器人与 Discord 服务器的延迟。

## 安装与运行

1. **克隆仓库**：
   ```bash
   git clone https://github.com/Yizakl/OuhOuh.git
   cd OuhOuh
   ```

2. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

3. **设置环境变量**：
   确保你已经创建了 Discord 机器人并获取了其 Token，以及 OpenAI 的 API 密钥。你可以通过以下环境变量进行设置：

   - `DISCORD_TOKEN`：你的 Discord 机器人 Token。
   - `OPENAI_API_KEY`：你的 OpenAI API 密钥。

   如果你使用的是 `.env` 文件，可以添加以下内容：

   ```
   DISCORD_TOKEN=your_discord_token
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **运行机器人**：
   ```bash
   python bot.py
   ```

## 命令说明

### /luck
查看今日运势（从 API 获取）。

### /today
查看随机运势（从本地生成的列表中随机选择）。

### /dl
查看你被标记为“大佬”的次数。

### /dtop
查看“大佬”次数排行榜，显示被标记为“大佬”次数最多的用户。

### /help
显示所有可用命令的帮助信息。

### /ping
测试机器人与 Discord 服务器的响应时间。

### !repeat
让机器人重复指定内容若干次（最多重复 8 次）。

### 示例

1. **查询今日运势**：
   ```
   /luck
   ```
   机器人返回：`今天的运势：大吉`

2. **查看大佬统计**：
   ```
   /dl
   ```
   机器人返回：`你被标记为大佬的次数是：5 次喵！`

3. **查看大佬排行榜**：
   ```
   /dtop
   ```
   机器人返回：显示一个包含用户名和“大佬”次数的排行榜。

## 文件说明

- `bot.py`：主程序文件，包含所有的逻辑和命令实现。
- `dalao_count.json`：记录每个用户被称为“大佬”的次数。
- `fortune_requests.json`：记录每个用户每日查询运势的情况。
  
## 许可证

该项目使用 [MIT 许可证](LICENSE)，你可以自由使用、修改和分发。

## 贡献

如果你愿意为这个项目做出贡献，可以通过提交 Pull Request 或报告问题来参与。

## 问题跟踪

如果你发现问题或有改进建议，可以在 GitHub 上的 Issues 部分创建新问题。

## 联系

- 开发者：Venti
- GitHub 链接：[https://github.com/Yizakl/OuhOuh](https://github.com/Yizakl/OuhOuh)



