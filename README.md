

برای خرید اکانت V2rayNG می‌توانید از ربات تلگرام ویژه ما استفاده کنید. این ربات ساده و سریع طراحی شده است تا در کمترین زمان ممکن اکانت مورد نظر خود را تهیه کنید. برای دسترسی به ربات، از لینک زیر استفاده کنید:

🔗 [ربات خرید اکانت V2rayNG](https://t.me/v2makers_bot)

همچنین در صورت نیاز به پشتیبانی، می‌توانید با آیدی پشتیبانی ما در تلگرام تماس بگیرید:  
🆔 [@v2makers_admin](https://t.me/v2makers_admin) 

با ربات ما تجربه‌ای آسان و امن برای خرید اکانت‌های پرسرعت و پایدار خواهید داشت.

این ربات به شما امکان می‌دهد تا به راحتی سرویس مورد نظر خود را انتخاب کنید. مزایای استفاده از ربات خرید اکانت V2rayNG شامل موارد زیر است:  

### **مزایای ربات خرید V2rayNG**  
1. **پرداخت آسان و امن**  
با استفاده از روش‌های پرداخت مطمئن، خرید شما با امنیت کامل انجام می‌شود.  

2. **دسترسی فوری**  
پس از خرید، اطلاعات اکانت به سرعت در اختیار شما قرار می‌گیرد و می‌توانید بلافاصله استفاده کنید.  

3. **تنوع در پلن‌ها**  
پلن‌های متنوعی از لحاظ مدت زمان و حجم مصرفی ارائه شده‌اند که می‌توانید براساس نیاز خود یکی را انتخاب کنید.  

4. **پشتیبانی حرفه‌ای**  
در صورت هرگونه سوال یا مشکل، تیم پشتیبانی ما به صورت ۲۴ ساعته در دسترس است.  

### **چرا V2rayNG؟**  
V2rayNG یکی از بهترین سرویس‌ها برای دسترسی پایدار و پرسرعت به اینترنت است. این سرویس از پروتکل‌های پیشرفته‌ای بهره می‌برد که امنیت و کیفیت اتصال شما را تضمین می‌کند.  

برای شروع، همین حالا وارد ربات شوید:  
🔗 [ورود به ربات خرید](https://t.me/v2makers_bot)

در صورت نیاز به مشاوره یا اطلاعات بیشتر، می‌توانید با تیم پشتیبانی ارتباط بگیرید:  
🆔 [@v2makers_admin](https://t.me/v2makers_admin)  

از سرعت و کیفیت فوق‌العاده سرویس‌های ما لذت ببرید.

برای برنامه‌نویسی یک ربات خرید اکانت V2rayNG، می‌توان از زبان‌هایی مانند Python استفاده کرد که به خوبی با APIهای تلگرام سازگار است. همچنین برای مدیریت و صدور اکانت‌ها، به یک سرور مجهز به نرم‌افزار V2ray نیاز دارید.

### **پیش‌نیازها**
1. **سرور VPS یا سرور اختصاصی**: 
   - سیستم‌عامل: ترجیحاً **Ubuntu 20.04** یا **Ubuntu 22.04**.
   - نصب نرم‌افزار **V2ray** و تنظیمات مربوط به صدور اکانت.
2. **API Bot تلگرام**:
   - ایجاد یک ربات در تلگرام با استفاده از [BotFather](https://t.me/BotFather) و دریافت توکن API.
3. **زبان برنامه‌نویسی**: 
   - Python همراه با کتابخانه‌هایی مانند `python-telegram-bot` برای ارتباط با تلگرام و `paramiko` یا `asyncssh` برای مدیریت سرور از طریق SSH.
4. **پایگاه داده**:
   - برای ذخیره اطلاعات کاربران و سفارش‌ها، از **SQLite**، **MySQL**، یا **PostgreSQL** استفاده کنید.

---

### **کدهای موردنیاز**

#### ۱. نصب پیش‌نیازها
```bash
sudo apt update
sudo apt install python3 python3-pip git
pip3 install python-telegram-bot pymysql paramiko
```

#### ۲. کدنویسی ربات
```python
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
```

---

### **مستندات و روش اجرا**

1. **نصب سرور V2ray**  
   برای نصب V2ray، می‌توانید از اسکریپت‌های آماده زیر استفاده کنید:
   ```bash
   bash <(curl -L -s https://install.direct/go.sh)
   ```

2. **پیکربندی فایل V2ray**  
   فایل پیکربندی `/etc/v2ray/config.json` را با توجه به پلن‌ها و کاربران تنظیم کنید.

3. **راه‌اندازی پایگاه داده**  
   - ایجاد دیتابیس:
     ```sql
     CREATE DATABASE v2ray_bot;
     ```
   - ایجاد جدول برای ذخیره کاربران:
     ```sql
     CREATE TABLE users (
         id INT AUTO_INCREMENT PRIMARY KEY,
         telegram_id BIGINT NOT NULL,
         username VARCHAR(255),
         plan_id INT,
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );
     ```

4. **اجرای ربات**  
   - ذخیره فایل در مسیر `bot.py` و اجرای آن:
     ```bash
     python3 bot.py
     ```

5. **مدیریت سرور**  
   می‌توانید از دستورات SSH برای مدیریت اکانت‌ها استفاده کنید یا اسکریپت‌هایی برای صدور و حذف اکانت بنویسید.

---

### **پیشنهادات سرور**
- VPS با مشخصات زیر مناسب است:
  - **RAM:** حداقل ۲ گیگابایت
  - **CPU:** حداقل ۲ هسته
  - **پهنای باند:** نامحدود یا با ترافیک بالا
  - **سیستم‌عامل:** Ubuntu 20.04 یا بالاتر

---

### **گسترش امکانات**
- افزودن درگاه پرداخت آنلاین برای دریافت هزینه.
- ارسال پیام‌های خودکار پس از صدور اکانت.
- مدیریت زمان‌بندی انقضای اکانت‌ها و ارسال هشدار.
