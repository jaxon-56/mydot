# MyDot Python API

یک کتابخانه غیررسمی برای کار با API پلتفرم **MyDot** که با استفاده از `requests` توسعه داده شده است. این پروژه بسیاری از Endpointهای نسخه وب MyDot را در قالب متدهای ساده و خوانا در اختیار توسعه‌دهندگان قرار می‌دهد.

> **قبل از استفاده، حتماً فایل `mydot.py` موجود در این مخزن را دانلود کرده و در کنار پروژه خود قرار دهید.** تمام کلاس‌ها و متدهای کتابخانه داخل این فایل قرار دارند.

## امکانات

* 🔐 ورود به حساب کاربری
* 👤 دریافت اطلاعات پروفایل
* ✏️ ویرایش پروفایل
* 📸 تغییر تصویر پروفایل (Avatar)
* 🖼️ تغییر تصویر هدر (Header)
* 👥 دریافت Followers و Following
* 📝 مشاهده پروفایل سایر کاربران
* ❤️ دریافت فعالیت‌های لایک کاربران
* 📰 دریافت Home Timeline
* ✨ دریافت Suggested Timeline
* 🔥 دریافت Trending Hashtags
* 🔔 دریافت Notifications
* 💬 دریافت لیست گفتگوها و پیام‌ها
* 📄 دریافت پست‌های کاربران
* 🔍 جستجوی کاربران و محتوا
* ⚡ مدیریت خودکار Session و Cookie

## نصب

```bash
pip install requests
```

سپس فایل **`mydot.py`** را از این مخزن دانلود کرده و کنار فایل پروژه خود قرار دهید.

## شروع سریع

```python
from mydot import MyDotAPI

api = MyDotAPI()

api.login("username", "password")

print(api.profile())
```

## متدهای موجود

```python
api.login(username, password)

api.profile()
api.user_profile(username)
api.edit_profile(...)

api.timeline()
api.suggested_timeline()

api.notifications()

api.trending_hashtags()

api.conversations()
api.messages(conversation_id)

api.followers(username)
api.following(username)

api.user_activity(user_id, action_type="like")

api.upload_avatar(path)

api.upload_header(path)
```

## نیازمندی‌ها

* Python 3.9+
* requests

