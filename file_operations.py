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