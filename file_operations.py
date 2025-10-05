file = open('sample.txt', 'r')
content = file.read()
print(content)
print(file.read(12))
file.close()
file = open('sample.txt', 'a')
file.write('\nThis is an additional line.')
file = open('sample.txt', 'w')
file.write('hey everyone!\nmy name is rajveer')
file.close()
file = open('sample.txt', 'r')
print(file.readlines())
file.close()
file = open('sample.txt', 'r')
    
for x in file:
    print(x)

file.close()
file = open('update.txt', 'r')
print(file.read())
file1 = open('update.txt', 'w')
x = file.readlines()
print(type(x))
for i in x:
    if i%2 != 0:
        file1.write(x[i-1])
    else:
        pass
file.close()
file1.close()
file1 = open('update.txt', 'r')
print(file1.read())
file1.close()