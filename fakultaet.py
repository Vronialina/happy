#Definition Funktion
def fak(n):	
  x = 1
  fakult = 1
  while (x <= n):
    fakult = fakult * x
    x += 1
  return(fakult)
   
#Aufruf von Funktion:
a = input()
y = fak(a)
print y