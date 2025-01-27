import telebot
import datetime
import time
import os,sys,re
import subprocess
import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
bot_token = '7766543633:AAFnN9tgGWFDyApzplak0tiJTafCxciFydo' 
bot = telebot.TeleBot(bot_token)
processes = []

def TimeStamp():
    now = str(datetime.date.today())
    return now

@bot.message_handler(commands=['spam'])
def spam(message):
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
    bot.reply_to(message, f'➤ Tấn Công SĐT: [ {phone_number} ] Thành Công ✅\n➤ Lặp Lại : {lap} ⏰\n➤ Ngày : {TimeStamp()}\n')
@bot.message_handler(commands=['help'])
def help(message):
    help_text = '''
Danh sách lệnh:
┏━━━━━━━━━━━━━━━━━┓
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
    youtube_url = "https://youtube.com/@secphiphai?si=Tum3SHPTFgsyv6Nl"
    web_url = "https://linktr.ee/tranquan46"
    admin_message = f"Thông tin liên hệ của Admin:\nweb: {web_url}\nyoutube: {youtube_url}"
    bot.reply_to(message, admin_message)
# lo 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Lệnh không hợp lệ. Vui lòng sử dụng lệnh /help để xem danh sách lệnh.')

bot.infinity_polling(timeout=60, long_polling_timeout = 1)