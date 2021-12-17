from itertools import islice
from itertools import repeat
import math
n = int(input())
arr = list(map(int, input().rstrip().split()))
i = 3
rem = len(arr) % 3
quo = int(len(arr) / 3)

Inputt = iter(arr)
length_to_split = []
length_to_split.extend(repeat(i, quo))
length_to_split.append(rem)
Output = [list(islice(Inputt, elem))
          for elem in length_to_split]

Output.sort()
#lengthy = len(Output)
#print(lengthy)
#print(Output[0][1])


for j in range(len(Output)):
  Output[j].sort()
  k = 0
  x = [i[0] for i in Output]



  

print(sum(x))


 




#print(Output)


#print(Output[0][1])




  
  
