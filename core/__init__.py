import datetime

class SystemInfo():

    def __init__():
        pass

    def get_time():
        now = datetime.datetime.now()
        answer = f'São {now.hour} horas e {now.minute} minutos.'
        return answer

    @staticmethod
    def get_day():
        today = datetime.datetime.now()
        answer = f'Hoje é {today.day} do mês {today.month}'
        return answer