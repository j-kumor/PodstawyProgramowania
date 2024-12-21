import re


def email_sender(email_content):
    sender_match = re.search('From: .*<(.*)>', email_content)
    return sender_match.group(1)


def email_recipient(email_content):
    recipient_match = re.search('To: .*<(.*)>', email_content)
    return recipient_match.group(1)


def email_subject(email_content):
    subject_match = re.search('Subject: (.*)', email_content)
    return subject_match.group(1)


def email_body(email_content):
    body_match = re.search(r"\n\n(.*)", email_content, re.DOTALL)
    return body_match.group(1).strip()

