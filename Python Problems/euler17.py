# If all the numbers from 1 to 1000 (one thousand) inclusive were 
# written out in words, how many letters would be used?

import math

#Length of the first 19 numbers
sub_twenty = [len("one"), len("two"), len("three"), len("four"), len("five"),
len("six"), len("seven"), len("eight"), len("nine"), len("ten"), len("eleven"),
len("twelve"), len("thirteen"), len("fourteen"), len("fifteen"), len("sixteen"),
len("seventeen"),len("eighteen"), len("nineteen")]

#Length of the tens' place
tens = [len("twenty"), len("thirty"), len("forty"), len("fifty"), len("sixty"),
len("seventy"), len("eighty"), len("ninety")]

def sub_100(n):
  if n < 20:
    return sub_twenty[n - 1]
  return tens[math.floor(n / 10) - 2] + sub_twenty[(n % 10) - 1]

def main(n):
  if n < 100:
    return sub_100(n)
  
  length = 0
  thousands = math.floor(n / 1000)
  hundreds = math.floor(n / 100) % 10
  modulo = n % 100
  
  if n > 999:
    length += sub_100(thousands) + len("thousand")
  
  if hundreds != 0:
    length += sub_twenty[hundreds - 1] + len("hundred")
  
  if modulo != 0:
    length += sub_100(modulo) + len("and")
  
  return length
  
def answer(n):
  total = 0
  for i in range (1, n + 1):
    total += main(i)
  return total
  
answer(1000)  

# Solution with a dictionary
s={0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six"/
,7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven"/
,12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen"/
,16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"/
,20:"twenty",30:"thirty",40:"forty",50:"fifty"/
,60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
for i in range(1,1000):
	if(not i in s.keys()):
		if(i<100):
			s[i]=s[i/10*10]+s[i%10]

		else:
			s[i]=s[i/100]+"hundred"
			if(i%100):
				s[i]+="and"+s[i%100]
s[1000]="onethousand"
total=0;
 for i in s.values():
	total+=len(i)
