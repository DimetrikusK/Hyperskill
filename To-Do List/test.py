from datetime import datetime, timedelta

today = datetime.today() - timedelta(days=20)
tmp = today.strftime('%d')
print(int(tmp))
print(f'{today.strftime("%a")} {int(tmp)} {today.strftime("%b")}')