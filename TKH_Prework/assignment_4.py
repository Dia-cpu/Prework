def long_name(name1,name2,name3,name4,name5,name6): 
    names_list = [name1,name2,name3,name4,name5,name6]
    longest_name = ""

    for name in names_list :
        if len(name) > len(longest_name) :
            longest_name = name   
        
    return longest_name

big_name = long_name("Sam","Rebecca","Sally","Cardi B","Michelle","Khadjat") 
print(big_name)