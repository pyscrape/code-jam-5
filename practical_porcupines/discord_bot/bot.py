from discord.ext import commands
from practical_porcupines.utils import ConfigBot, check_date
from practical_porcupines.discord_bot.api import get_difference
from practical_porcupines.discord_bot.utils import decode_diff_resp, embed_generator

config_bot = ConfigBot()

bot_client = commands.Bot(command_prefix=config_bot.PREFIX)


@bot_client.event
async def on_ready():
    """
    Runs when client boots
    """

    print(f"{bot_client.user.name} is online w/ id: '{bot_client.user.id}'!")
    print("Testing api: " + await decode_diff_resp(await get_difference("2010", "2019")))


@bot_client.command()
async def gmwl(ctx, date_1, date_2):
    """
    Global Mean water level command

    > Inputs 2 dates
    - date_1: Beginning date
    - date_2: Ending date
    < Shows user gmwl difference
    """

    verified_date_1 = check_date(date_1)
    verified_date_2 = check_date(date_2)

    # IF invalid date
    if not (verified_date_1 or verified_date_2):
        ctx.send(
            embed=embed_generator(
                "Invalid date",
                "One of the dates you sent was invalid, please try again!",
                0xA31523,
            )
        )
        return

    result = await decode_diff_resp(get_difference(verified_date_1, verified_date_2))

    ctx.send(
        embed=embed_generator(
            "Result",
            f"Operation completed sucsessfully, result is {result}mm",
            0x3BA315,
        )
    )
