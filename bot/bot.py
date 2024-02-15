import discord
import handler
# all the initialization stuff

# on_ready

# on_message
    # handler()

token = 'MTIwNjYxNTgwNTQ2MzM3MTc4Ng.GkWuLg.MMRL8p9czCmIybi8s6szBrSL4zJUr5m_93d_qo' # subject to change
intents = discord.Intents.default()
intents.message_content = True

async def send_message(message, user_message: str):
    try:
        response = handler.QueryHandler.ans_query(user_message)

        await message.channel.send(response)
    
    except Exception as e:
        print(e)

def run_discord_bot():
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # useful for debugging
        print('message:', user_message)
        print('channel:', channel)
        print('user:', username)
        print("\n")

        await send_message(message, user_message)

    client.run(token)

run_discord_bot()
