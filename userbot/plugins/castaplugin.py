from . import ALIVE_NAME, catub, edit_or_reply

plugin_category="extra"

A = (
"╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱\n"
"╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱\n"
"╱┃┗━━┓┃╰━╯┃┃┗━━┓╱\n"
"╱┗━━━┛╰━━━╯┗━━━┛╱\n"
)

B = (
"░█▀▀█ ▀█▀ ░█▀▀█\n"
"░█▄▄▀ ░█    ░█▄▄█\n"
"░█ ░█   ▄█▄ ░█\n"
)

@catub.cat_cmd(
    pattern="lol$",
    command=("lol", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}lol",
    },
)
async def bluedevillol(lol):
    "fun art command"
    await edit_or_reply(lol, A)

@catub.cat_cmd(
    pattern="rip$",
    command=("rip", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}rip",
    },
)
async def bluedevilrip(rip):
    "fun art command"
    await edit_or_reply(rip, B)
