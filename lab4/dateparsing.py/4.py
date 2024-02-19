from datetime import datetime as d
def Dif_Time(dt1,dt2):
    delta_time = dt2 - dt1
    return abs (delta_time.days * 24 * 3600 + delta_time.seconds) # "+delta_time.seconds -> Это количество секунд, оставшихся после вычета целых дней из разницы между датами."

date_str1 = input()
date_str2 = input()

data1 = d.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
data2 = d.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

print(Dif_Time(data2,data1))