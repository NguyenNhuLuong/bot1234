import discord
from discord.ext import commands

# KHỞI TẠO BOT
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)


# KHI BOT KHỞI ĐỘNG
@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công dưới tên: {bot.user}")


# CHÀO MỪNG THÀNH VIÊN MỚI
@bot.event
async def on_member_join(member):
    try:
        # ID kênh chào mừng — nhớ thay bằng kênh thật của bạn
        WELCOME_CHANNEL_ID = 1439331672112759027  
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if channel is None:
            return

        # TẠO EMBED CHÀO MỪNG𝐍𝐢𝐠𝐡𝐭 𝐅𝐮𝐫𝐲
        embed = discord.Embed(
            title="🐉 𝐍𝐢𝐠𝐡𝐭 𝐅𝐮𝐫𝐲 - Chào mừng cư dân mới!",
            description=(
                f"Xin chào {member.mention} 👋\n"
                "Chào mừng bạn đã đáp xuống **Night Fury**!\n\n"
                "Chúc bạn có khoảng thời gian tuyệt vời tại Gia Tộc 🐲"
            ),
            color=discord.Color.dark_purple()
        )

        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(text="BOT By ! Em KID Đâyy • Night Fury")

        await channel.send(embed=embed)

    except Exception as e:
        print(f"Lỗi chào mừng: {e}")


# CHẠY BOT
bot.run("MTQzMzY2MjQwMzYxODU0MTU5MQ.GGYPvv.JkP1ctTjDJGyV28Rl7ev1pvREVqpnRpc5UYPo0")
