#!/usr/bin/env python3

import sys

number_arg = float(sys.argv[1])

if number_arg > 0:
   print("positive")
   if number_arg =< 50:
      print("Number also equal or smaller than 50")
      if (number_arg % 2) == 0:
         print("it is an even number that is smaller than 50")
   else:
      print("Number is larger than 50")
      if number_arg % 3 == 0:
         print("Number is larger than 50 and divisible by 3")         
elif number_arg == 0:
   print("Zero")
else:
   print("negative")

