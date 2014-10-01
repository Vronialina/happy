#!/usr/bin/python

A = [0.3, 1.8, -2.2]
B = [-2.5, 3.8, 0.4]

if (len(A) == len(B)):
  s = 0					#Skalarprodukt
  i = 0
  for i in range(len(A)):
    s = A[i] * B[i] + s
    i += 1
  print "Skalarprodukt = ", s
  
  if (len(A) == 3):			#Vektorprodukt
    a = A[1]*B[2] - A[2]*B[1]
    b = A[2]*B[0] - A[0]*B[2]
    c = A[0]*B[0] - A[1]*B[0]

    V = [a, b, c]
    print "Vektorprodukt = ", V
  else:
    print "Vektorprodukt: Vektoren haben die falsche Laenge."

else:
  print "Fehler! Vektoren muessen gleich lang sein!"
