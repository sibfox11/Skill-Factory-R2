 import numpy as np
 
 
 
 def calc_sum():
     num1=np.random.randint(low=0,high=101)
     num2=np.random.randint(low=0,high=101)

     #print('Посчитайте : {} + {} ='.format(num1,num2),end='')
     ssum=int(input('Посчитайте : {} + {} ='.format(num1,num2)))
     print('Sum = ',ssum)