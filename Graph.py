from collections import defaultdict

from State import TERMINAL_STATE

import time


class Graph:

	def __init__(self):

		self.bfs_parent = {}
		self.dfs_parent = {}

		self.expandedBFS = 0
		self.expandedDFS = 0

	def DFS(self, s):
		self.expandedDFS = 0
		self.dfs_parent[s] = None
		visited = {(s.missionaries, s.cannibals, s.dir): True}

		start_time = time.time()
		stack = [s]
		while stack:
			u = stack.pop()
			self.expandedDFS += 1

			if u.isGoalState():
				print("No of Expanded Nodes: " + str(self.expandedDFS))
				print("No of Explored Nodes: " + str(visited.__len__()))
				self.dfs_parent[TERMINAL_STATE] = u
				stack.clear()
				return self.dfs_parent

			t = time.time() - start_time
			# Stops searching after a certain time/node limit 
			if t > u.CONSTANTS.MAX_TIME or self.expandedDFS > u.CONSTANTS.MAX_NODES:
				if t > u.CONSTANTS.MAX_TIME:
					print("%.2fs A fost depasita limita de timp de: %.2fs" % (t, u.CONSTANTS.MAX_TIME))
				else:
					print("EXCEEDED NODE LIMIT of %d" % u.CONSTANTS.MAX_NODES)
				print("No of Expanded Nodes: " + str(self.expandedDFS))
				print("No of Explored Nodes: " + str(visited.__len__()))
				stack.clear()
				return {}

			for v in u.successors():
				if (v.missionaries, v.cannibals, v.dir) not in visited.keys():
					visited[(v.missionaries, v.cannibals, v.dir)] = True
					self.dfs_parent[v] = u
					stack.append(v)
		return {}

	# Prints the path returned by BFS/DFS
	def printPath(self, parentList, tail):
		if tail is None:
			return
		if parentList == {} or parentList is None:  # tail not in parentList.keys():
			return
		if tail == TERMINAL_STATE: tail = parentList[tail]

		stack = []

		while tail is not None:
			stack.append(tail)
			tail = parentList[tail]

		while stack:
			print(stack.pop())
