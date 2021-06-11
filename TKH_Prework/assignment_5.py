def word_scramble(*names_list):
    even_list = []
    odd_list = []
    for name in names_list:
        if len(name) % 2 == 0:
            even_list.append(f"{name}")
        else:
             odd_list.append(name)
    
    even_list = [f"b{name[1:]}" for name in even_list]
    odd_list = [f"{name[:-1]}c" for name in odd_list]
    print(even_list,odd_list,"\n")
    return even_list

even_list = word_scramble("bob","jimmy","max b", "bernie", "jordan", "future hendrix")
print(even_list)
even_list = word_scramble("Sam","Rebecca","Sally","Card B","Michelle","Khadjat")
print(even_list)
#I have to admit I got stuck on this one and had to ask online