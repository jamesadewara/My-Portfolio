import os
import shutil
from pathlib import Path

from django.core.mail import EmailMessage, send_mail
from django.conf import settings

def emailSender(name,sender_email, receiver_email, message, subject):
    send_mail(subject, message, sender_email, receiver_email, fail_silently=False)

def getMediaDir():
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    MEDIA_DIR = os.path.join(BASE_DIR, "media")
    return MEDIA_DIR