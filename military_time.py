from datetime import datetime
input_time=input()
militiary_time = {}
if input_time[-2:].lower() == 'pm':
    hr,min = input_time.split(':')
    if int(hr)==12:
        hr=0
    elif int(hr) in range(1,12):
        hr = 12+int(hr)
    print("{}:{}".format(hr,min))
else:
    print(input_time)