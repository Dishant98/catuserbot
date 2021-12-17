#By @deepaiims
from userbot import catub
from ..core.managers import edit_delete
from ..helpers.utils import reply_id

plugin_category = "useless"

@catub.cat_cmd(
    pattern="agst ?(.*)",
    command=("agst", plugin_category),
    info={
        "header": " To make animated google sticker",
        "usage": [
            "{tr}agst <your text>",
        ],
    },
)
async def app(deep):
    
    if deep.fwd_from:
        return
    bot = "@GooglaxBot "
    text = deep.pattern_match.group(1)
    reply_to_id = await reply_id(deep)
    if not text:
        return await edit_delete(deep, "`Give me some text rip life, Lmao`")
    else:
    	    await deep.delete()
    	    run = await deep.client.inline_query(bot, text)
    	    result = await run[0].click("me")
    	    await result.delete()
    	    await deep.client.send_message(deep.chat_id, result, reply_to=reply_to_id)
