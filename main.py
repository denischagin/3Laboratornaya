def inputs():
      while True:
        x = int(input('Введите натур. число '))
        if x > 0:
            break
        print('Неверное число')
    return x
 

def x2(х):
 return collatz(x//2)

  
def x3_1(x):
  return collatz(x * 3 +1)

  
def  collatz():
