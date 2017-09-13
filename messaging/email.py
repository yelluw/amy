from smtplib import SMTPException

from django.core.mail import send_mail


def send_email(to, subject, message):
    """
    Sends am email to a single recipient
    using django's send_mail() functionality.

    returns True on success, False on failure
    """
    try:
        sent = send_mail(
            subject,
            message,
            'yelluwbusinessnewsletter@yelluw.com',
            [to],
            fail_silently=False,
        )

        # django's send_mail function
        # returns 1 when message is sent
        # 0 when message not sent
        if sent == 1:
            return True

    except SMTPException as e:
        pass

    return False


def send_multiple_emails(to_list, subject, message):
    """
    Sends a email to a list of
    recipients using django's
    send_mass_mail() functionality
    """
    pass
