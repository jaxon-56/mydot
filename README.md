# MyDot Python API

یک کتابخانه غیررسمی برای کار با API پلتفرم **MyDot** که با استفاده از `requests` توسعه داده شده است. این کتابخانه بیشتر Endpointهای نسخه وب MyDot را پوشش می‌دهد و استفاده از آن را تنها با چند خط کد امکان‌پذیر می‌کند.

## امکانات

* 🔐 Login / Authentication
* 👤 دریافت و ویرایش پروفایل
* 📸 آپلود و تغییر Avatar
* 🖼️ آپلود و تغییر Header
* 📝 مشاهده پروفایل کاربران
* 👥 دریافت Followers و Following
* ❤️ مشاهده فعالیت‌های Like
* 📰 دریافت Home Timeline
* ✨ دریافت Suggested Timeline
* 🔥 دریافت Trending Hashtags
* 🔔 دریافت Notifications
* 💬 دریافت Conversation List
* 📨 مدیریت پیام‌ها
* 📄 دریافت پست‌های کاربران
* 🔍 جستجوی کاربران و محتوا
* ⚡ مدیریت Session و Cookie به‌صورت خودکار

## نصب

```bash
pip install requests
```

## شروع سریع

```python
from mydot import MyDotAPI

api = MyDotAPI()
api.login("username", "password")

print(api.profile())
```

## نمونه متدها

### ورود

```python
api.login(username, password)
```

### پروفایل

```python
api.profile()
api.user_profile(username)
api.edit_profile(
    display_name="AmirAbas",
    bio="Python Developer",
    website="https://example.com",
    location="Iran"
)
```

### تایم‌لاین

```python
api.timeline()
api.suggested_timeline()
```

### ترندها

```python
api.trending_hashtags()
```

### اعلان‌ها

```python
api.notifications()
```

### گفتگوها

```python
api.conversations()
api.messages(conversation_id)
```

### دنبال‌کنندگان

```python
api.followers("username")
api.following("username")
```

### فعالیت‌ها

```python
api.user_activity(user_id, action_type="like")
```

### آپلود آواتار

```python
api.upload_avatar("avatar.png")
```

### آپلود هدر

```python
api.upload_header("header.jpg")
```

## نیازمندی‌ها

* Python 3.9+
* requests

