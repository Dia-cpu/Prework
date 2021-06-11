names_list = ["Sam","Rebecca","Sally","Cardi B","Michelle","Khadjat"]
longest_name = ""

for name in names_list :
    if len(name) > len(longest_name) :
        longest_name = name   
       
print(longest_name)