import disnake, os
from disnake.ext import commands
from disnake import Status, Activity, ActivityType

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True

bot = commands.InteractionBot(intents=intents)

@bot.event
async def on_ready():
    print(f"Бот {bot.user} был успешно запущен")
    await bot.change_presence(status=Status.dnd, activity=Activity(
        name="Клоз", type=ActivityType.watching))

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        cog_name = filename[:-3]
        bot.load_extension(f"cogs.{cog_name}")

print("Коги загружены!")

bot.run("MTIwODEyNTA1NDA4NTUwMDk1OQ.G2f_fb.pVdAhTXvtG-s51-K_kFj28ngsTx1DaDVo06OSc")