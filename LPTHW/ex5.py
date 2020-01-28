my_name = 'Umar-Farouq A. Yusuf'
my_age = 21 # not a lie
my_height = 75 # inches
my_weight = 170 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %r pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("He's %d inches tall" % my_height)
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))