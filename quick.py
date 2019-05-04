from random import randint
A = []
B = []
C = []
D = []
sirali_dizi = [0,1,2,3,4,5,6,7,8,9]
ters_sirali_dizi = [9,8,7,6,5,4,3,2,1,0]

def random_array_generator(Array,x):
   while x>0:
      Array.append(randint(0,10000))
      x=x-1
random_array_generator(A,10)
random_array_generator(B,100)
random_array_generator(C,1000)
random_array_generator(D,10000)

class sort_algorithm:
   def __init__(self):
      self.counter_quick = 0

   def Quick_sort(self,Array,b,s):
      if b<s:
         self.counter_quick=self.counter_quick+1
         r = self.Partition(Array,b,s)
         self.counter_quick=self.counter_quick+1
         self.Quick_sort(Array,b,r-1)
         self.counter_quick=self.counter_quick+1
         self.Quick_sort(Array,r+1,s)
         self.counter_quick=self.counter_quick+1

   def Partition(self,Array,b,s):
      pivot = Array [s]
      self.counter_quick=self.counter_quick+1
      i = b - 1
      self.counter_quick=self.counter_quick+1
      for j in range (b,s):
         self.counter_quick=self.counter_quick+1
         if(Array[j] <= pivot):
            self.counter_quick=self.counter_quick+1
            i = i+1
            self.counter_quick=self.counter_quick+1
            t = Array[i]
            self.counter_quick=self.counter_quick+1
            Array[i] = Array[j]
            self.counter_quick=self.counter_quick+1
            Array[j] = t
            self.counter_quick=self.counter_quick+1
      t = Array[i+1]
      self.counter_quick=self.counter_quick+1
      Array[i+1] = Array[s]
      self.counter_quick=self.counter_quick+1
      Array[s] = t
      self.counter_quick=self.counter_quick+1
      return i+1
def run_quick_algorithm(Array):
    print (Array)
    x = sort_algorithm()
    x.Quick_sort(Array,0,len(Array)-1)
    print (Array)
    print (x.counter_quick)

def main():
    run_quick_algorithm(B)

main()
      
