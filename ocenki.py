# Нахождение средней оценки из 5 введенных
N = 5 
A = [0] * N 
print ("Введите оценки:")
for i in range(N):
	print (i+1, "оценка: ", end="") 
	A[i] = int(input()) 
	s = 0
	for i in range(N):
		s = s + A[i]
		sb = s/5
print ("Средний балл:", sb)
