import telebot
import datetime
import time
import os,sys,re
import subprocess
import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
bot_token = '6393252222:AAEWYuwEUdVj7jN0AnhUzO5TPm9E0cOQPjo' 
bot = telebot.TeleBot(bot_token)
processes = []
ADMIN_ID = '6452283369'
allowed_group_id = -1001999335910
def TimeStamp():
    now = str(datetime.date.today())
    return now

@bot.message_handler(commands=['getkey'])
def startkey(message):
    bot.reply_to(message, text='VUI LÒNG ĐỢI TRONG GIÂY LÁT!')
    key = "HDT-" + str(int(message.from_user.id) * int(datetime.date.today().day) - 12666)
    key = "http://off-vn.x10.mx/index.html?key=" + key
    print(key)
    api_token = '18e951d7-7b48-4f87-8401-c584158244dd'    
    url = requests.get(f'https://web1s.com/api?token={api_token}&url={key}').json()
    url_key = url['shortenedUrl']
    text = f'''
- http://off-vn.x10.mx/n.mp4 LINK LẤY KEY {TimeStamp()} LÀ: {url_key}
- KHI LẤY KEY XONG, DÙNG LỆNH /key <key> ĐỂ TIẾP TỤC
'''
    bot.reply_to(message, text)


@bot.message_handler(commands=['key'])
def key(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP KEY.')
        return

    user_id = message.from_user.id

    key = message.text.split()[1]
    username = message.from_user.username
    expected_key = "HDT-" + str(int(message.from_user.id) * int(datetime.date.today().day) - 12666)
    if key == expected_key:
        bot.reply_to(message, f' http://off-vn.x10.mx/t.mp4 [ KEY HỢP LỆ ] NGƯỜI DÙNG CÓ ID: [ {user_id} ] ĐƯỢC PHÉP ĐƯỢC SỬ DỤNG LỆNH    [ /spam ]')
        fi = open(f'./user/{datetime.date.today().day}/{user_id}.txt',"w")
        fi.write("")
        fi.close()
    else:
        bot.reply_to(message, 'KEY KHÔNG HỢP LỆ.')
  
@bot.message_handler(commands=['spam'])
def spam(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
      bot.reply_to(message, 'Dùng /getkey Để Lấy Key Và Dùng /key Để Nhập Key Hôm Nay!')
      return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI ')
        return
    if len(message.text.split()) == 2:
        bot.reply_to(message, 'Vui Lòng Nhập Đúng Định Dạng | Ví Dụ: /spam 0987654321 500')
        return
    lap = message.text.split()[2]
    if lap.isnumeric():
      if not (int(lap) > 0 and int(lap) <= 100):
        bot.reply_to(message,"Vui Lòng Spam Trong Khoảng 1 - 100 Thôi !!")
        return
    else:
      bot.reply_to(message,"Sai Số Lần Spam !!!")
      return
    phone_number = message.text.split()[1]
    if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone_number):
        bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        return

    if phone_number in ["0376841471"]:
        # Số điện thoại nằm trong danh sách cấm
        bot.reply_to(message,"Spam cái đầu buồi tao huhu")
        return
    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, phone_number, "100"])
    processes.append(process)
    bot.reply_to(message, f'➤ USER ID: [ {user_id} ]\n➤ Tấn Công SĐT: [ {phone_number} ] Thành Công ✅\n➤ Lặp Lại : {lap} ⏰\n➤ Ngày : {TimeStamp()}\n http://off-vn.x10.mx/i.mp4\n')
@bot.message_handler(commands=['help'])
def help(message):
    help_text = '''
Danh sách lệnh:
┏━━━━━━━━━━━━━━━━━┓
┣➤/getkey: Để Lấy Key ✅
┣➤/key: Để Nhập Key ✅
┣➤/spam {SĐT} {Số Lần} ✅
┣➤/help: Danh sách lệnh ✅
┣➤/time Thời Gian HĐ Bot ✅
┣➤/status Lượt Chạy Bot ✅
┣➤/admin Thông Tin Admin ✅
┗━━━━━━━━━━━━━━━━━┛
'''
    bot.reply_to(message, help_text)
    
# status
@bot.message_handler(commands=['status'])
def status(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    process_count = len(processes)
    bot.reply_to(message, f'Số quy trình đang chạy: {process_count}.')

#cpu
# khoir dong lai bot
@bot.message_handler(commands=['time'])
def show_uptime(message):
    current_time = time.time()
    uptime = current_time
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    bot.reply_to(message, f'Bot Đã Hoạt Động Được: {minutes} phút, {seconds} giây')
#check

#admin
@bot.message_handler(commands=['admin'])
def admin_info(message):
    # Thay thế các giá trị sau bằng thông tin liên hệ của bạn
    zalo_box = "https://zalo.me/g/bprmyn080"
    youtube_url = "https://youtube.com/@HDT-TOOL-VN?si=MvEhEk8SIMp2V26s"
    web_url = "https://linkbio.co/sharetool"
    admin_message = f"Thông tin liên hệ của Admin:\n\nBox Zalo: {zalo_box}\nweb: {web_url}\nyoutube: {youtube_url}"
    bot.reply_to(message, admin_message)
# lo 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Lệnh không hợp lệ. Vui lòng sử dụng lệnh /help để xem danh sách lệnh.')

bot.infinity_polling(timeout=60, long_polling_timeout = 1)
