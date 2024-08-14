# Concatenate two strings
name_1 = "Naruto"
name_2 = "Uzumaki"
full_name = name_1 + ' ' + name_2
print(full_name)

#NoneType
how_many_cars_you_have = None
print(how_many_cars_you_have)
# None
print(type(how_many_cars_you_have))
# NoneType

# id() - function gives you the memory address where the object is stored.
age = 24
age_1 = "24"
age_2 = 24

print(id(age))      # 140710144183448
print(id(age_1))    # 2214999937632
print(id(age_2))    # 140710144183448

print(type(id(age_1)))
# int