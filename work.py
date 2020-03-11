class Parent(object):
   def fun(self):
      print('Hi')
p = Parent()
p.fun()

class Child(Parent):
    def fun(Parent):
        print('Bye')
c = Child()
c.fun()

def insertionSortRecursive(arr,n):
    # Comment A
    if n<=0:
        return
    insertionSortRecursive(arr,n-1)
    last = arr[n-1]
    j = n-2
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1]=last