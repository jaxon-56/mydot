# MyDot Python API

یک کتابخانه‌ی غیررسمی و سبک برای کار با API پلتفرم **MyDot** که با استفاده از `requests` نوشته شده است.

این پروژه تقریباً تمام Endpointهای عمومی و خصوصی کشف‌شده از نسخه وب MyDot را در قالب متدهای ساده پایتون در اختیار شما قرار می‌دهد و می‌تواند برای ساخت ربات، ابزارهای مدیریت حساب، اتوماسیون و توسعه برنامه‌های شخص ثالث مورد استفاده قرار گیرد.

---

## امکانات

### احراز هویت

* ورود با نام کاربری یا ایمیل و رمزعبور
* مدیریت خودکار Session
* ذخیره و استفاده از Access Token
* خروج از حساب

---

### پروفایل

* دریافت اطلاعات حساب فعلی
* دریافت اطلاعات هر کاربر با Username
* ویرایش پروفایل
* تغییر نام نمایشی
* تغییر بیو
* تغییر وبسایت
* تغییر موقعیت
* تغییر تاریخ تولد
* تغییر جنسیت
* تغییر تصویر پروفایل
* تغییر تصویر هدر

---

### آپلود فایل

* دریافت لینک Upload از سرور
* آپلود مستقیم فایل روی CDN
* تایید آپلود آواتار
* تایید آپلود هدر
* پشتیبانی از تصاویر

---

### تایم‌لاین

* دریافت Home Timeline
* دریافت Suggested Timeline
* دریافت Explore
* دریافت Trending Hashtags
* دریافت پست‌های کاربر
* دریافت پست‌های لایک‌شده
* دریافت فعالیت‌های کاربر

---

### پست‌ها (Dots)

* مشاهده اطلاعات پست
* لایک
* آنلایک
* ریپست
* حذف ریپست
* ذخیره
* حذف از ذخیره‌ها
* ارسال پست
* حذف پست
* ارسال پاسخ
* مشاهده پاسخ‌ها

---

### جستجو

* جستجوی کاربران
* جستجوی هشتگ
* جستجوی پست‌ها

---

### دنبال‌کنندگان

* دریافت Followers
* دریافت Following
* Follow
* Unfollow

---

### اعلان‌ها

* دریافت لیست Notifications

---

### گفتگوها

* دریافت Conversation List
* دریافت اطلاعات Conversation
* دریافت پیام‌ها
* ارسال پیام
* مشاهده آخرین پیام

---

### کاربران

* مشاهده اطلاعات هر کاربر
* مشاهده Badge
* مشاهده تعداد دنبال‌کنندگان
* مشاهده تعداد دنبال‌شوندگان
* مشاهده وضعیت Verify
* مشاهده وضعیت Staff

---

## نصب

```bash
pip install requests
```

یا پروژه را Clone کنید:

```bash
git clone https://github.com/USERNAME/mydot-python.git
```

---

## استفاده

```python
from mydot import MyDotAPI

api = MyDotAPI()

api.login(
    "username",
    "password"
)

profile = api.profile()

print(profile)
```

---

## مثال‌ها

دریافت پروفایل

```python
print(api.profile())
```

ویرایش نام

```python
api.edit_profile(
    display_name="AmirAbas"
)
```

دریافت Trending

```python
print(api.trending_hashtags())
```

دریافت اعلان‌ها

```python
print(api.notifications())
```

دریافت گفتگوها

```python
print(api.conversations())
```

دریافت Followers

```python
print(api.followers("username"))
```

دریافت Following

```python
print(api.following("username"))
```

آپلود آواتار

```python
api.upload_avatar("avatar.jpg")
```

آپلود هدر

```python
api.upload_header("header.jpg")
```

---

## ساختار پروژه

```
mydot/
│
├── mydot.py
├── examples.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## وابستگی‌ها

* Python 3.9+
* requests

---

## وضعیت پروژه

این کتابخانه به صورت **غیررسمی (Unofficial)** توسعه داده شده و وابستگی سازمانی به MyDot ندارد.

Endpointها از نسخه وب استخراج شده‌اند و ممکن است در آینده توسط MyDot تغییر کنند.

---

## مشارکت

Pull Request و Issueها با کمال میل پذیرفته می‌شوند.

در صورت کشف Endpoint جدید یا رفع باگ، می‌توانید مشارکت کنید.

---

## سلب مسئولیت

این پروژه صرفاً برای اهداف آموزشی و توسعه نرم‌افزار ایجاد شده است. مسئولیت استفاده از آن بر عهده کاربر است.

---

## مجوز

MIT License
