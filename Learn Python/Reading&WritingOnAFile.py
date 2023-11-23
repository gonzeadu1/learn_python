# mode = 'r' is read only
# mode = 'w' is write only (will overwrite files or create new!)
# mode = 'r+' is reading and writing
# mode = 'a' is append only (will add on to files)
# mode = 'w+' is writing and reading (overwrites exsiting files or ceates a new file!)

# with open('my_file.txt', mode='r') as f:
#     print((f.read()))

my_file = open("Feyi.txt", mode='w')
my_file.write("Hello World")
my_file.close()
print(my_file)
