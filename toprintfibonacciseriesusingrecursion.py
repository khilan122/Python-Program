def fibonacci(n):
	if n<=1:
		return n
	else:
		return(fibonacci(n-1) + fibonacci(n-2))

n = int(input('Enter a number, N, N>=2 : '))

fibo_series = []

for i in range(0,n):
	fibo_series.append(fibonacci(i))
	
print(fibo_series)