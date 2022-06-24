from ctypes.wintypes import HCOLORSPACE


dia = int (input('quantidade de dias? '))
horas = int (input('quantidades de horas? '))
minutos = int (input('quantidade de minutos? '))

diassegundo = dia * 86400
horassegundo = horas * 3600
minutossegundo = minutos * 60

total = (diassegundo + horassegundo + minutossegundo)

print('total:', total)
