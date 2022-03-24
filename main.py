from datetime import datetime, timedelta

if __name__ == '__main__':

    day = 1

    log_time = datetime.today() + timedelta(days=day)
    log_time = log_time.strftime('%Y.%m.%d')
    print(log_time)
