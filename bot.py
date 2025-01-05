from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import pymysql
import paramiko

# اطلاعات سرور V2ray
V2RAY_SERVER = 'IP_SERVER'
SSH_PORT = 22
SSH_USER = 'root'
SSH_PASSWORD = 'your_password'

# اتصال به پایگاه داده
db = pymysql.connect(host="localhost", user="db_user", password="db_password", database="v2ray_bot")
cursor = db.cursor()

def start(update: Update, context: CallbackContext):
    update.message.reply_text("به ربات خرید اکانت V2rayNG خوش آمدید!\nبرای مشاهده پلن‌ها /plans را وارد کنید.")

def plans(update: Update, context: CallbackContext):
    plans_text = "💳 پلن‌های موجود:\n1. پلن یک‌ماهه - ۵۰ گیگ\n2. پلن سه‌ماهه - ۱۵۰ گیگ\n3. پلن شش‌ماهه - ۳۰۰ گیگ"
    update.message.reply_text(plans_text)

def order(update: Update, context: CallbackContext):
    user_message = update.message.text.split()
    if len(user_message) < 2:
        update.message.reply_text("لطفاً شماره پلن مورد نظر خود را ارسال کنید.\nمثال: /order 1")
        return
    
    plan_id = user_message[1]
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(V2RAY_SERVER, SSH_PORT, SSH_USER, SSH_PASSWORD)

    # صدور اکانت
    command = f'python3 /path/to/v2ray_script.py --plan {plan_id}'
    stdin, stdout, stderr = ssh_client.exec_command(command)
    result = stdout.read().decode()
    ssh_client.close()

    if "success" in result:
        update.message.reply_text(f"اکانت شما با موفقیت صادر شد:\n{result}")
    else:
        update.message.reply_text("مشکلی در صدور اکانت رخ داده است. لطفاً با پشتیبانی تماس بگیرید.")

def main():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("plans", plans))
    dp.add_handler(CommandHandler("order", order))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
