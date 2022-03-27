import json
from datetime import datetime

def all_days(url):
    with open(url, "r", encoding='utf-8') as file:
        data = file.readlines()
        i = 3
        days = {}
        i = 0
        for line in data:
            line_json = json.loads(line)
            datetime = line_json['date']
            date = datetime[0:10]     
            if date not in days.keys():
                days[date] = 1
            else:
                days[date] += 1
        sortedDays = sorted(days.items(), key=lambda x: x[1], reverse=True)
            
        return(sortedDays[0:10])
