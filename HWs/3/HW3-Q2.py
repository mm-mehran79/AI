import numpy as np
def main():
	transitionProbabilityTable:list = []
	Mood2ColorProbabilityTable:list = []
	k = int(input().strip())
	n = int(input().strip())
	m = int(input().strip())
	#k, n, m = [int(x) for x in input().strip().split()]
	daysColor = [int(x)-1 for x in input().strip().split()]								#shirt color of day {index}
	probability = np.array([float(x) for x in input().strip().split()])                    #probability of being in mood {index} at first day
	for i in range(n): 
		transitionProbabilityTable.append([float(x) for x in input().strip().split()])
	for i in range(n):
		Mood2ColorProbabilityTable.append([float(x) for x in input().strip().split()])
	transitionProbabilityTable = np.array(transitionProbabilityTable)
	for i in range(k+1):
		probability = probability @ transitionProbabilityTable
	probability = probability @ np.array(Mood2ColorProbabilityTable)
	argMax = np.argmax(probability)
	print(argMax+1, round(probability[argMax], 2), sep=" ")
	
if __name__ == "__main__":
	main()