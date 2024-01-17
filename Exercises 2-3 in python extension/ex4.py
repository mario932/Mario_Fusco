import numpy as np
import matplotlib.pyplot as plt

def recaman(n):
    mylist = [0]
    a0 = 0
    
    for i in range(1, n):
       # print(i,a0-i)
        if ((a0 -i > 0) and not (a0-i in mylist)): 
          #  print(i)
            mylist.append(a0:=a0-i)
        else:
            mylist.append(a0:=a0+i)
    return mylist

mylist= (recaman(150))

if __name__ == '__main__':
    print("Script is running directly")
    (recaman(150))

for i in range(1, len(mylist)):
    h = (mylist[i] + mylist[i-1])/2
    r = abs((mylist[i] - mylist[i-1]))/2
    x = np.linspace(mylist[i], mylist[i-1], 100)
    y = (-1)**i * np.sqrt(r**2 - (x-h)**2)
    plt.plot(x, y)
plt.savefig('Recaman.png')
plt.show()

