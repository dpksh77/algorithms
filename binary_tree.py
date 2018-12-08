class Node:

	def __init__(self,data):

		self.left=None
		self.right=None
		self.data=data
		print(self.data)

	def insert_data(self, data):

		if self.data:
			#print(self.data)
			print(self.data)
			if data > self.data:
				if self.right is None:
					self.right=Node(data)

				else:

					self.right.insert_data(data)

			
			elif data < self.data:
				if self.left is None:
					self.left=Node(data)
				else:
					self.left.insert_data(data)
		else:
			self.data=data

	#def print_tree():

out=Node(10)
out.insert_data(5)
out.insert_data(3)