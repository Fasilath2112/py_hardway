# It uses formatted strings (f-strings) to dynamically insert variable values into output strings, making the information readable and contextually meaningful. 
my_name='Zed A. Shaw'
my_age=35
my_height=74
my_weight=180
my_eyes='Blue'
my_teeth='White'
my_hair='Brown'

print(f"Let's talk about {my_name}")
print(f"He's {my_height} inches tall")
print("Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair")
print(f"His teeth are usually {my_teeth} depending on the coffee")

#this line is tricky, try to get it exactly right
total= my_age + my_height + my_weight
print(f"if i add {my_age}, {my_height} and {my_weight} i get {total}")