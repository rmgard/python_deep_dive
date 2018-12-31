 ###############################################333
 # try and finally
 ##################################################

def explain_finally(num, denom):
     a = num 
     b = denom
     try:
         a/b
     except ZeroDivisionError:
         print('division by 0')
     finally:
         print('this always executes')

 ###############################################333
 # Now let's add a while
 ##################################################

def add_while_finally(num, denom):
     a = num 
     b = denom
     while a < 4:
         print('---------------')
         a += 1
         b -= 1 

         try:
             a / b
         except ZeroDivisionError:
             print("{0}, {1} - division by 0".format(a, b))
             continue
         finally:
             print("{0}, {1} - always executes".format(a, b))

         print("{0}, {1} - main loop".format(a, b))
     else:
         print('Code executed without a zero division error!')
