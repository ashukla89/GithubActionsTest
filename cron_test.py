from datetime import datetime
now = datetime.now()
message = f"The current time is {now.strftime('%H:%M:%S')} in New York City on {now.strftime('%m/%d/%Y')}."
with open(now.strftime("%m-%d-%Y_%H-%M-%S") + '.txt', 'w') as f:
    f.write(message)
