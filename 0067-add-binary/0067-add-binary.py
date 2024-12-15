class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        tempA = len(a) - 1
        tempB = len(b) - 1
        value = ""
        ten_digit=0

        while tempA >= 0 or tempB >= 0:
            firstvalue = int(a[tempA]) if tempA >= 0 else 0
            
            secondvalue = int(b[tempB]) if tempB >= 0 else 0
            one_digit = (ten_digit + firstvalue + secondvalue) %2
            ten_digit = (ten_digit + firstvalue + secondvalue)//2
            value = str(one_digit) + value 
            tempA = tempA - 1
            tempB = tempB - 1

        if ten_digit > 0:
            value = str(ten_digit) + value

        return value
                 
