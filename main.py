from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#load the token from somewhere safe (step 1)
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

# step 2 :Setup bot!!

intents : Intents = Intents.default()  #permissions
intents.message_content = True #NOQA   
 # permissions for content reading and no quality assurance
client: Client = Client(intents=intents) #client of type client which has intent set to our intents

#s3 meg function
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(message was empty because intents were not enabled probably)')
        return
    #walrus operator down
    if is_private := user_message[0] == '?': 
        user_message =  user_message[1:]

    try:
        response : str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# s4, handle startup for the bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} bot is running')

#s5 handle incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author== client.user:
        return   # bot wont reply to itself

    username: str = str(message.author)
    user_message:str =message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#s6 : main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
