import pandas as pd
import numpy as np
import datetime

data = datetime.datetime(2021, 7, 8, 23, 59, 32)

print(data)
print(data + datetime.timedelta(days=5))
print(data.weekday())

# Funções

# datetime.datetime(): Define um novo objeto datetime passando os dados de ano, mês, dia, hora, minutos, segundos, microsegundos e fuso
# datetime.timedelta(): Permite somar um intervalo de tempo a uma data
# datetime.datetime.now(): Obtém o dia e hora neste momento (utiliza o fuso horário do computador se nada for passado)
# datetime.datetime.strptime(): Formata uma string em um datetime

# Metados de Datatime

# data.year/month/day/hour/minute/second/microsecond: Obtém informação sobre a data 
# data.weekday(): Dia da semana da data (sendo 0 = segunda-feira)
# data.strftime(): Formata a data numa string

# print(datetime.datetime.now())
# print(data.year)
# print(data.day)
# print(data.month)
# print(data.strftime("%d/%m/%Y %H:%M:%S"))
# dataFormt = datetime.datetime.strptime("11/02/2014 11:43:20", "%d/%m/%Y %H:%M:%S")
# print(dataFormt)

print()
ser = pd.Series(["2021-01-01", "2021-01-02", "2021-01-03", "2021-01-04", "2021-01-05"], dtype="datetime64[ns]")
print(ser)

print("Dia da semana", ser.dt.dayofweek)
print("Dia do ano", ser.dt.dayofyear)
print("numero do dia do mes", ser.dt.daysinmonth)
print("Numero da semana do ano", ser.dt.isocalendar().week)
print("converte o deteTime para texto", ser.dt.strftime("%d %b %Y"))

print()
ser = pd.Series(["2021/01/01", "2021/01/02", "2021/01/03", "2021/01/04", "2021/01/05"])
print(pd.to_datetime(ser))

print()
ser = pd.Series(["01/01/2021", "02/01/2021", "03/01/2021", "04/01/2021", "05/01/2021"])
ser = pd.to_datetime(ser, format="%d/%m/%Y")

print(ser + pd.DateOffset(days=5))
print(ser + pd.DateOffset(months=5))

print(pd.date_range("2021-01-01", "2021-01-05"))
print(pd.Series(pd.date_range("2021-01-01", "2021-01-05")))
print(pd.Series(pd.date_range("2021-01-01", "2021-01-05", freq="12h")))
print(pd.Series(pd.date_range("2021-01-01", "2021-01-05", periods=3)))

ser1 = pd.Series(pd.date_range("2021-01-01", "2021-01-05"))
ser2 = pd.Series(pd.date_range("2021-02-01", "2021-02-05"))
print(ser1 - ser2)

delta = ser1 - ser2

print(delta.dt.days)