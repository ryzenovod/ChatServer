import time
from datetime import datetime

time_17_00 = datetime.fromisoformat("2021-08-03 17:00:00").timestamp()
time_17_30 = datetime.fromisoformat("2021-08-03 17:00:00").timestamp()
test_message1 = {
    "text": "Привет",
    "name": "Епифан",
    "time": time_17_00,
    }

test_message2 = {
    "text": "Здарова",
    "name": "Михаил",
    "time": time_17_00,
    }
# key + value, ключ + значение

# Database - база данных с сообщениями чата
# Список сообщений
db = [
 test_message1,
 test_message2
    ]

def chat(name, text):
    message = {
        "name": name,
        "text": text,
        "time": time.time()
        }
    db.append(message)
    #добавляем новое соообщение в список
chat("Маша", "Как дела?")
chat("Петя", "Йо, я веган")

    #распечатать все сообщения
def print_messages(messages):
    for message in messages:
        name = message["name"]
        text = message["text"]
        message_time = message["time"]
        time_pretty = datetime.fromtimestamp(message_time)

        print (f"[{name}] / {time_pretty}")
        print(text)
        print()

          #print_messages(db)

          #собирать все сообщения после определенного времени
def get_messages(after_timestamp):
 result = [] #все сообщения после афтертаймстемп
 for message in db:
   if message["time"] > after_timestamp:
      result.append(message)

 return result
  
print_messages(get_messages(time_17_30))