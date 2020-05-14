#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().system(u'pip install pytelegrambotapi')


# In[6]:


get_ipython().system(u'pip install --upgrade pip')


# In[8]:


get_ipython().system(u'pip install requests')


# In[15]:


import requests

url = "https://api.telegram.org/bot1193429890:AAEr8pqQVxH3m-uHuF12pcVSDCXGUnZCnxU/"

#делаем функцию проверки обновлений 

def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


# In[19]:


token = "1193429890:AAEr8pqQVxH3m-uHuF12pcVSDCXGUnZCnxU"
bot = telebot.TeleBot('1193429890:AAEr8pqQVxH3m-uHuF12pcVSDCXGUnZCnxU')


# In[17]:


import telebot


# In[20]:


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Пора поговорить о CV!')
    
bot.polling()


# In[ ]:


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, надеюсь, ты не против общаться неформально. Давай уточним, что именно ты хочешь обсудить?')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Надеюсь, я помог. Пиши ещё)')
        
bot.polling()


# In[ ]:




