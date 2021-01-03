import requests
import psutil
from config import bot_token, chat_id, App


def SendTelegram(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def CheckApp(processName):
    for process in psutil.process_iter():
        try:
            if processName.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if CheckApp(App):
    pass
else:
    SendTelegram('Not running App')
