
#EJ5
#PIDE LA NOTA FINAL DE UN ESTUDIANTE DE 0 A 100, SI 
# EL PROMEDIO ES MENOR IGUAL A 50 MOSTRAR REPROBADO CON 
# LA NOTA DE REPROBACION Y SI ES MAYOR IGUAL A 51 MOSTRAR APROBADO CON LA NOTA DE APROBACION
sa = False
while sa == False:
   print ("veremos si su estudiante reprobo querida/o ingeniero")
   print("⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓")
   j = int(input (" ingresa la nota "))
   if j >=0 and j <= 100:
    if j == 100:
      print ("es excelencia")
      sa=True
    if j < 51:
      print(f"REPROBADO con la nota {j}")
      if j == 100:
              print ("es excelencia")
      sa=True
    else:
      print(f"APROBADO con la nota {j}")
      sa= True
   else:
      print ("esa nota no es valida")
