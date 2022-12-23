class DSeparation:
	def __init__(self) -> None:
		self.source = 0
		self.destination = 0
		self.visited: list = []
		self.numberOfEvents: int = 0
		self.numberOfEdges: int = 0
		self.neighborsOfNode: list = []
		self.numberOfObserved: int = 0
		self.isNodeObserved: list = []
		self.childrenOfNode: list = []

	def getInput(self) -> None:
		self.numberOfEvents, self.numberOfEdges, self.numberOfObserved = [int(x) for x in input().strip().split()]
		for i in range(self.numberOfEvents):
			self.neighborsOfNode.append([])
			self.isNodeObserved.append(False)
			self.childrenOfNode.append([])
		for i in range(self.numberOfEdges):
			a, b = [int(x)-1 for x in input().strip().split()]
			self.neighborsOfNode[a].append(b)
			self.neighborsOfNode[b].append(a)
			self.childrenOfNode[a].append(b)
		for i in range(self.numberOfObserved):
			self.isNodeObserved[int(input().strip()) - 1] = True
		self.source, self.destination = [int(x)-1 for x in input().strip().split()]

	def isNodeOrDescendantsObserved(self, node: int) -> bool:
		if self.isNodeObserved[node]:
			return True
		for child in self.childrenOfNode[node]:
			if self.isNodeOrDescendantsObserved(child):
				return True
		return False

	def neighbors(self, node: int)-> list:
		return [t for t in self.neighborsOfNode[node] if t not in self.visited]

	def findActivePath(self, node: int) -> bool:
		self.visited.append(node)
		if len(self.visited) > 2:		#check activeness of last triple:
			if not(self.isNodeObserved[self.visited[-2]]) and ((self.visited[-1] in self.childrenOfNode[self.visited[-2]]) or (self.visited[-3] in self.childrenOfNode[self.visited[-2]])):
				pass
			elif self.visited[-2] in self.childrenOfNode[self.visited[-1]] and self.visited[-2] in self.childrenOfNode[self.visited[-3]]: #check v-structure
				if not(self.isNodeOrDescendantsObserved(self.visited[-2])):
					self.visited.pop()
					return False
			else:						#last three visited node are not active triple
				self.visited.pop()
				return False
		if node == self.destination:
			return True
		for nextNode in self.neighbors(node):
			if self.findActivePath(nextNode):
				return True
		self.visited.pop()
		return False

	def run(self) -> None:
		if self.findActivePath(self.source):
			print(*[i + 1 for i in self.visited], sep=", ",)
		else:
			print("independent")

def main():
	s = DSeparation()
	s.getInput()
	s.run()

if __name__ == "__main__":
	main()