#project Euler #4 - largest palindrome digital number
# a palindrome is a number that is the same backwards and forwards, like 101 or 990099


def check_is_palindrome(number):
    try:
        number=str(number)
    except Exception:
        print(f"WARNING!!!{number} is not stringable!")
        return False
    is_palindrome = True
    print(f"number: {number}")
    for index in range(0,int(len(number)/2)):
        if number[index]!=number[-(index+1)]:
            #print(f"zle {index} {number[index]} {number[-(index+1)]}")
            is_palindrome=False
            break
    return is_palindrome    
    
    
    
def create_greatest_number(number):
    numbers=str(number)
    is_modulo=len(numbers)%2
    if is_modulo:
        half_len=int(len(numbers)/2)
        middle_digit = numbers[half_len]
        numbers=numbers[0:half_len]+numbers[half_len+1:]
    digitals=set(numbers)
    digitals=list(digitals)
    sorted_digitals=sorted(digitals)[::-1]
    if is_modulo:
        final_result=''.join(sorted_digitals + [middle_digit] + digitals) 
    else:
        final_result=''.join(sorted_digitals + digitals)
    print(f"longest palindrome for {number}:  {final_result}")

    
print(str("123"))        
test_number=1546451    
print (f"Is palindrome for {test_number}: {check_is_palindrome(test_number)}")
if check_is_palindrome(test_number):
    create_greatest_number(test_number)
else:
    print ("this is not palindrome")

