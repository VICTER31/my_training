def send_email(message, recipient,*,sender = "university.helpg@mail.com"):
    if not '@' in recipient:
        return (f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if not '@' in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if '.com' in recipient:
        None
    elif '.ru' in recipient:
        None
    elif '.net' in recipient:
        None
    else:
        return (f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if '.com' in sender:
        None
    elif '.ru' in sender:
        None
    elif '.net' in sender:
        None
    else:
        return (f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if recipient == sender:
        return ("Нельзя отправить письмо самому себе!")
    if sender == 'university.helpg@mail.com':
        return ( f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        return (f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напомина=ю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
