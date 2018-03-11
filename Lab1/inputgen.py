from random import randint

output = [randint(1, 120) for i in range(600)]

fileInput = open("input.txt", "w")
for i in range(len(output) - 1):
	fileInput.write(str(output[i]) + ",")
fileInput.write(str(output[len(output) - 1]))
fileInput.close()
