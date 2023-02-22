class Solution:
    def intToRoman(self, num: int) -> str:
        intToRomanDict = {
            0: "",
            1: "i", 
            2: "ii",
            3: "iii", 
            4: "iv", 
            5: "v", 
            6: "vi",
            7: "vii",
            8: "viii",
            9: "ix",
        }

        output = ""
        units_dig = num%10
        output = intToRomanDict[units_dig] + output
        num = (num - units_dig)//10

        tens_dig = num%10

        if tens_dig <= 3:
            for i in range(tens_dig):
                output = "x" + output
        elif tens_dig == 4: 
            output = "xl" + output
        elif tens_dig == 5: 
            output = "l" + output
        elif tens_dig == 9: 
            output = "xc" + output
        elif tens_dig > 5 : 
            for i in range(tens_dig - 5):
                output = "x" + output
            output = "l" + output 
        
        num = (num - tens_dig)//10   

        huns_dig = num%10

        if huns_dig <= 3:
            for i in range(huns_dig):
                output = "c" + output
        elif huns_dig == 4: 
            output = "cd" + output
        elif huns_dig == 5: 
            output = "d" + output
        elif huns_dig == 9: 
            output = "cm" + output
        elif huns_dig > 5: 
            for i in range(huns_dig - 5):
                output = "c" + output
            output = "d" + output 
        
        num = (num - huns_dig)//10  

        output = "M" * num + output

        return output.upper()
