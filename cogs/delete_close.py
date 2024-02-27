import disnake, os, time
from disnake.ext import commands

class CloserDelete(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name="delete-close", description="Удаление ивента")
	@commands.has_permissions(administrator=True)
	async def delete_close(self, inter: disnake.ApplicationCommandInteraction, close: str = commands.Param(name="ивент")):
		await inter.response.defer()
		guild = self.bot.get_guild(1179405637092900936)
		category = disnake.utils.get(guild.categories, id=1208471443055058974)

		if guild and inter.guild.id == 1179405637092900936:
			channels = category.channels

			delete_channels = False
			for channel in channels:
				if close.lower() in channel.name.lower() or close.lower() in channel.name.lower().replace("-", " "):
					await channel.delete()
					delete_channels = True

			if delete_channels:
				await inter.edit_original_response(f"Ивент с названием `{close}` был успешно удален!")

			else:
				await inter.edit_original_response(f"Ивента с названием {close} не существует!")

def setup(bot: commands.Bot):
    bot.add_cog(CloserDelete(bot))