import re
 
with open("example.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print(urls)
            
with open("sample2.txt", "r") as myfile:
    contents = myfile.read()
    
reg_ex =r"[a-z0-9\.\-+]+@[a-z0-9\.\-+]+\.[a-z]+"
print(re.findall(reg_ex, contents))    
                
reg_ex=(r"\(\d{3}\)\s\d{3}-\d{4}")
print(re.findall(reg_ex, contents))

street_reg = re.compile(r'ST\s[0-9]{5}')
print(street_reg)

# streets = re.findall(street_reg, myfile)
               