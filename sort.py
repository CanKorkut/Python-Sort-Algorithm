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
      self.counter_merge=0
      self.counter_insertion=0
   
   def insertion_sort(self,array):
      keyword = 0;
      for j in range(1,len(array)):
        keyword=array[j]
        i = j-1
        while (i>=0 and array[i]>keyword):
            array[i+1]= array[i]
            i=i-1
        array[i+1]=keyword

   def merge_sort(self,array,p,r):
      if p<r:
         q = (p+r)//2
         self.merge_sort(array,p,q)
         self.merge_sort(array,q+1,r)
         self.merge(array,p,q,r)

   def merge(self,array,p,q,r):
      n1 = q-p+1
      n2 = r-q
      L=[0] * (n1+1)
      R=[0] * (n2+1)
      for i in range(0,n1):
         L[i]=array[p+i]
      for j in range(0,n2):
         R[j]=array[q+j+1]
      L[n1]=99999
      R[n2]=99999
      i=0
      j=0
      for k in range(p,r+1):
         if L[i]<=R[j]:
            array[k] = L[i]
            i=i+1
         else:
            array[k] = R[j]
            j=j+1

def run_sort_alg(array):
   print(array)
   x=sort_algorithm();
   #x.insertion_sort(array)
   x.merge_sort(array,0,len(array)-1)
   print(x.counter_merge)
   #print(x.counter_insertion)
   print (array)

   
def main():
   run_sort_alg(A)
   
if __name__ == "__main__": 
   main()
