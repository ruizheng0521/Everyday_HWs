import timeit
def fibo(temp,n):
  if n in temp:
    print(temp[n])
    return (temp[n])
  else:
    temp[n] = fibo(temp,n-1) + fibo(temp,n-2)

    return temp[n]


temp={1:1,2:1}
start = timeit.default_timer()

print(fibo(temp,200))
stop = timeit.default_timer()

print('Time: ', stop - start) 
