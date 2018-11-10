from celery import task
from django.conf import settings

from django.core.mail import send_mail
from django.template import loader
from django.core.cache import caches
# 获得缓存
cache = caches['confirm']

@task
def send_verify_mail(url,user_id,reciver):
    title = "红浪漫"
    content = ''
    # 加载页面
    template = loader.get_template('user/email.html')
    # 渲染html
    html = template.render({"url":url})
    # 找到发件人
    email_from = settings.DEFAULT_FROM_EMAIL
    # 发送邮件
    send_mail(title,content,email_from,[reciver],html_message=html)
    cache.set(url.split("/")[-1],user_id,settings.VERIFY_CODE_MAX_AGE)

