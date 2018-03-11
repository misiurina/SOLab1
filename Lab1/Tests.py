from random import sample

def getInput():
	try:
		file = open("input.txt", "r")
		inp = list(map(int, file.read().split(",")))
		file.close()
		return inp
	except FileNotFoundError:
		print("File was not found")

processes = getInput()

def measureFCFS(p):
	delay = 0
	for i in range(len(p) - 1):
		for j in range(i):
			delay += p[j]
	return int(delay / len(p))

def msort(x): #mergesort
	result = []
	if len(x) < 2:
		return x
	mid = int(len(x)/2)
	y = msort(x[:mid])
	z = msort(x[mid:])
	while (len(y) > 0) or (len(z) > 0):
		if len(y) > 0 and len(z) > 0:
			if y[0] > z[0]:
				result.append(z[0])
				z.pop(0)
			else:
				result.append(y[0])
				y.pop(0)
		elif len(z) > 0:
			for i in z:
				result.append(i)
				z.pop(0)
		else:
			for i in y:
				result.append(i)
				y.pop(0)
	return result


def measureSJF(p):
	"""Running SJF. Have no idea, why does it return different values"""
	return measureFCFS(msort(p))

def measureWSJF(p):
	pr0 = [p[i] for i in range(len(p)) if p[i] % 5 == 0]
	pr1 = [p[i] for i in range(len(p)) if p[i] % 3 == 0 and not p[i] % 5 == 0]
	pr2 = [p[i] for i in range(len(p)) if p[i] % 2 == 0 and not p[i] % 5 == 0 and not p[i] % 3 == 0]
	pr3 = [p[i] for i in range(len(p)) if not p[i] % 5 == 0 and not p[i] % 3 == 0 and not p[i] % 2 == 0]
	byPr = pr0 + pr1 + pr2 + pr3
	#print(byPr)
	#print(len(byPr))
	return measureFCFS(byPr)

def measureRR(p):
	#print(len(p))
	quantum = msort(p)[int(len(p) * 0.2)]
	for i in range(len(p)):
		if p[i] > quantum:
			p.append(p[i] - quantum)
			p[i] = quantum
	#print(p)
	#print(len(p))
	return measureFCFS(p)

#print(measureFCFS(processes))
#print(measureSJF(processes))
#print(measureWSJF(processes))
#print(measureRR(processes))

resFCFS = []
resSJF = []
resWSJF = []
resRR = []

FCFS = open("results/FCFS.txt", "a")
SJF = open("results/SJF.txt", "a")
WSJF = open("results/WSJF.txt", "a")
RR = open("results/RR.txt", "a")

for i in range(100):
	procs = sample(processes, len(processes))
	#FCFS
	res = measureFCFS(procs)
	resFCFS.append(res)
	FCFS.write("," + str(res))
	print(res)
	#SJF
	res = measureSJF(procs)
	resSJF.append(res)
	SJF.write("," + str(res))
	print(res)
	#WSJF
	res = measureWSJF(procs)
	resWSJF.append(res)
	WSJF.write("," + str(res))
	print(res)
	#RR
	res = measureRR(procs)
	resRR.append(res)
	RR.write("," + str(res))
	print(res)

FCFS.close()
SJF.close()
WSJF.close()
RR.close()

summary = open("results/summary.txt", "w")
summary.write("minFCFS: " + str(min(resFCFS)) + "\n" + "maxFCFS: " + str(max(resFCFS)) + "\n\nminSJF: " + str(min(resSJF)) + "\n" + "maxSJF: " + str(max(resSJF)) + "\n\nminWSJF: " + str(min(resWSJF)) + "\n" + "maxWSJF: " + str(max(resWSJF)) + "\n\nminRR: " + str(min(resRR)) + "\n" + "maxRR: " + str(max(resRR)))
summary.close()
