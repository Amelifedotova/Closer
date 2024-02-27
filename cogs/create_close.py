import disnake, os, time
from disnake.ext import commands

class Eventer (commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name="create-event", description="Создание ивента")
	@commands.has_permissions(administrator=True)
	async def create_close(self, inter: disnake.ApplicationCommandInteraction, event: str = commands.Param(name="ивент"), user_limit: int = commands.Param(name="участники")):
		await inter.response.defer()
		guild = self.bot.get_guild(1179405637092900936)
		category = disnake.utils.get(guild.categories, id=1208828726192767096)

		if guild and inter.guild.id == 1179405637092900936:
			channels = category.channels
			for channel in channels:
				if str(event) in channel.name:
					await inter.edit_original_response(f"Ивент с названием {event} уже существует.")
					return

			else:
				await category.create_voice_channel(name=event, user_limit=user_limit, reason=None)
				await category.create_text_channel(name=f"Чат ивента {event}", reason=None)
				await inter.edit_original_response(f"Ивент с названием `{event}` был успешно создан!")

		else:
			await inter.edit_original_response(f"....")

def setup(bot: commands.Bot):
    bot.add_cog(Eventer(bot))