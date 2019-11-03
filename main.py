from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

logging.disable(logging.ERROR)

chatbot = ChatBot('XXX-bot')

trainer_1 = [
    'Xin chào',
    'Tôi có thể giúp gì được bạn',
]

trainer_2 = [
    'Tạm biệt',
    'Hẹn gặp lại',
    'Vâng'
]

# trainer = ListTrainer(chatbot)
# trainer.train(trainer_1)
# trainer.train(trainer_2)

response = chatbot.get_response("tam biet")
print(response)