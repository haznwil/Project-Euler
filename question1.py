###Python Code for Project Euler Question #1

##Use 3 and 5 as inputs

def sums(n):

  if 1000 % n == 0:
    multiple_n = 1000 - n
  else:
    mod_n = 1000 % n
    multiple_n = 1000 - mod_n

  
  sum_n = (multiple_n/n)*((n + multiple_n)/2)
  return(sum_n)
    
c = int(input("What is your first natural number?" ))
d = int(input("What is your second natural number?" ))
e = c*d

c_sum = sums(c)
d_sum = sums(d)
e_sum = sums(e)
 
print(c_sum + d_sum - e_sum)
