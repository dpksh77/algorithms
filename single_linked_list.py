class Node:

	def __init__(self, data=None, next=None):
		print(data)
		#print(next)
		self.data=data
		self.next=next


	def set_data(self,data):
		self.data=data

	def get_data(self):
		return self.data

	def set_next(self,next):
		self.next=next

	def get_next(self):
		return self.next

class SinglyLinkedList:

	def __init__(self):
		#print("deepak")
		self.head=None
		self.size=0

	def add(self,value):
		node=Node(value)
	#	print(node.data_value)
		node.set_next(self.head)
	#	print(self.head)
		self.head=node
	#	print(self.head)
		self.size += 1
#		print(node.data_value)
		#node.get_data()

	def _search_node(self, value,remove=False):
		current = self.head
		previous = None

		while current:
			if current.data == value:
				print("search node "+str(current.data)+" is present on position")
				break

			else:
				previous = current
				current = current.next


		if remove and current:
			if previous is None:
				self.head = current.next
			else:
				previous.set_next(current.next)
			self.size -=1
			print("removed successfully")
		
		if current==None:
			print("search node "+str(value)+" is present not on position")
		
        

	def remove(self, value):
		
		return self._search_node(value,True)
    
	def search(self, value): 
		return self._search_node(value)

	def size1(self):
		print(self.size)
	#	return self.size
   # def search(self, value):
    	#return self._search_node(value)




obj=SinglyLinkedList()
obj.add(10)
obj.add(5)
obj.add(6)
obj._search_node(5)
obj.remove(5)
obj.search(5)
obj.size1()
#obj.search(6)