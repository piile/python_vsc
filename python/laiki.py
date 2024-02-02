# import datetime
# #standarts datums ar fiksētiem atribūtiem date (gads, mēnesis, diena)
# datums = datetime.date(2023,12,8)
# print (datums)
# ###################
# import datetime
# laiks = datetime.time(23, 59, 59, 99999)
# #laiks
# #Pareizs laiks:
# print (laiks.hour,
#        laiks.minute,
#        laiks.second,
#        laiks.microsecond)
# ###################
# from datetime import time
# laiks = time.fromisoformat('23:59:59+02:01')
# #Pareizs laiks:
# print(laiks.hour,
#       laiks.minute,
#       laiks.second,
#       laiks.microsecond,
#       laiks.tzinfo, # +2 laika josla, nokluse-None
#       laiks.fold) # 0 vai 1 - vasaras laiks
# ###################
# from datetime import timedelta
# delta_object = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# print(delta_object)
# #Tas pats
# obj = timedelta()
# print(obj)
# ###################
# from datetime import timedelta
# delta_object = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# x = timedelta(hours=3, seconds=110)
# print(x)
# y = timedelta(hours=2, seconds=30)
# print("Rezultāts:")
# print(x + x, x - y, x / y, sep='\n')
# ###################
# from datetime import timedelta
# delta_object = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# x = timedelta(hours=3, seconds=110)
# print(x)
# y = timedelta(hours=2, seconds=30)
# print("Rezultāts:")
# print(x + x, y - x, x / y, sep='\n')
# ###################
# import datetime
# from datetime import timedelta
# dienasSogad = datetime.datetime(2022,1,1)
# sodien = datetime.datetime.now()
# print("Šodienas datums = ", sodien)
# print("Šogad nodzīvotas ", sodien-dienasSogad)
# print("Rīt būs ", sodien+timedelta(days=1))
# print()

# print("Šogad ir ", sodien.year, " gads")
# print("Šogad ir ", sodien.day, " diena")
# print(sodien.strftime("%A"))
# #precīzāk skatīt w3schools.com/python/python_datetime.asp
# ###################
# from datetime import datetime
# from pytz import timezone, common_timezones
# datetime_object = datetime.now(timezone('Europe/Riga'))
# print("Current IST:", datetime_object)

