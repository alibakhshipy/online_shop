from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_email(subject, to, context, template_name):
    """
    ارسال ایمیل با رندر قالب HTML
    """
    # محتوای HTML رو از قالب بساز
    message = render_to_string(template_name, context)

    # ارسال ایمیل
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # فرستنده (تو settings.py باید ست شده باشه)
        [to],                         # گیرنده
        fail_silently=False,
    )