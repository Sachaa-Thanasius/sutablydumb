import tomllib

import discord
from discord.ext import commands


class SutaBlyDumbBot(commands.Bot):
    async def setup_hook(self) -> None:
        await self.load_extension("jishaku")


def main() -> None:
    with open("config.toml", mode="rb") as fp:
        config = tomllib.load(fp)

    intents = discord.Intents.all()
    bot = SutaBlyDumbBot(",", intents=intents)
    bot.run(config["token"])


if __name__ == "__main__":
    raise SystemExit(main())
