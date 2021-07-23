from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝗔𝘀𝘀𝗮𝗹𝗮𝗺𝘂'𝗮𝗹𝗮𝗶𝗸𝘂𝗺 𝗱𝘂𝗹𝘂 𝗯𝗶𝗮𝗿 𝘀𝗼𝗽𝗮𝗻.`")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝗔𝘀𝘀𝗮𝗹𝗮𝗺𝘂'𝗮𝗹𝗮𝗶𝗸𝘂𝗺 𝗱𝘂𝗹𝘂 𝗯𝗶𝗮𝗿 𝘀𝗼𝗽𝗮𝗻.`")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝗪𝗮'𝗮𝗹𝗮𝗶𝗸𝘂𝗺𝘀𝘀𝗮𝗹𝗮𝗺 𝗕𝗿𝗼𝘂.`")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝗪𝗮'𝗮𝗹𝗮𝗶𝗸𝘂𝗺𝘀𝘀𝗮𝗹𝗮𝗺 𝗕𝗿𝗼𝘂`")


CMD_HELP.update({
    "salam":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.P` | `.p`\
\n↳ : Untuk Memberi salam.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.L` `.l`\
\n↳ : Untuk Menjawab Salam."
})
