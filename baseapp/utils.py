from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template


EMAIL_ADMIN = settings.DEFAULT_FROM_EMAIL


def get_next_destination(request):
    next = None
    if request.GET.get("next"):
        next = str(request.GET.get("next"))
    return next


def send_welcome_mail(user):
    subject = "Account registered successful"
    context = {
        "user": user,
    }
    message = get_template("auth/welcomemail.html").render(context)
    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=EMAIL_ADMIN,
        to=[user.email],
        reply_to=[EMAIL_ADMIN],
    )
    mail.content_subtype = "html"
    mail.send(fail_silently=True)
