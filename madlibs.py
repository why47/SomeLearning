#Sambung kata dengan player
# Disclaimer MADLIBS??
# is a game in which you write a story with missing word in it then you can ask another
# player to fill in the blanks

#string concatenation how to out string together
# suppose we want to create a string that says "kata1........."

#kata1 = "saya" # string variabel

#print("subscribe to "+ kata1)
#print("subscribe to {}".format(kata1)) #.format method is powerfull tool can be used to format string in a variety of ways
#print(f"subscribe to {kata1}") # with f
# print("subscribe to {kata1}") # without f {kata 1} is ouput {kata1} not on in there values

kata = input("kata: ")
kata1 = input("kata: ")
kata2 = input("kata: ")
kata3 = input("kata: ")

madlib = (f"computer program is so {kata}! it make me so exited all the time because i love to {kata1}. \
          stay hydrate and {kata2} like you are {kata3}!")

print(madlib)