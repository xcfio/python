# File Write
fw = open("cool.txt", "w")
fw.write("This is data")
fw.close()

# File Read
fr = open("cool.txt", "r")
print(fr.read())
fr.close()
