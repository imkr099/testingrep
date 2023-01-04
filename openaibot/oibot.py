import openai
from decouple import config
import telebot

openai.api_key = config("OPENAI_API_KEY")
bot = telebot.TeleBot(config("TOKEN"))


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    bot.send_message(chat_id=message.from_user.id, text= response['choices'][0]['text'])

bot.polling()