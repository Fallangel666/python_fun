#3 number max 
def max_num(num1, num2, num3):
    if num1 > num2:
        return num1
    elif num2 > num3:
        return num2
    else: 
        return num3

def mult_list(*nums):
    results = 0
    for n in nums:
      n * results
      return results

def rev_string(string):
    rev = string [::-1]
    print(rev) 


