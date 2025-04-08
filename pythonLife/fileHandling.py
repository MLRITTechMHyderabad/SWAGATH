f = open('fileHandling1.txt', mode='r')
print(f.read())
f.close()

f = open("fileHandling1.txt", mode ='w')
f.write("Hey swagath")
f.close() #removes the old text

f = open("fileHandling.txt", mode='a')
f.write("magic show")
f.close()

f = open("fileHandling.txt", mode = 'r+')
print(f.read())
f.write("ufff")
f.close()

f = open("fileHandling.txt", mode = 'w+')
f.write("HOW ARE YOU") #truncates
print(f.read())
f.close()


