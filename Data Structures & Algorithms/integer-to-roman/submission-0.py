class Solution:
    def intToRoman(self, num: int) -> str:
        currstr = ""
        for i in range(len(str(num))):
            currnum =(num//10**i)%10
            print(currnum)
            if i == 0:
                if currnum ==9:
                    currstr="IX"+currstr
                if currnum < 9 and currnum >5:
                    currstr="V"+(currnum-5)*"I"+currstr
                if currnum <4:
                    currstr = "I"*currnum+currstr
                if currnum ==4:
                    currstr ="IV"+currstr
                if currnum ==5:
                    currstr = "V"+currstr
            if i == 1:
                if currnum ==9:
                    currstr ="XC"+currstr
                if currnum < 9 and currnum >5:
                    currstr="L"+(currnum-5)*"X"+currstr
                if currnum <4:
                    currstr = "X"*currnum+currstr
                if currnum ==4:
                    currstr ="XL"+currstr
                if currnum ==5:
                    currstr = "L"+currstr
            if i == 2:
                if currnum ==9:
                    print("t")
                    currstr ="CM"+currstr
                if currnum < 9 and currnum >5:
                    currstr= "D" + (currnum-5)*"C" +currstr
                if currnum <4:
                    currstr = "C"*currnum +currstr
                if currnum ==4:
                    currstr ="CD"+currstr
                if currnum ==5:
                    currstr = "D"+currstr
            if i ==3:
                currstr = "M"*currnum+currstr
        return currstr
                    
                
