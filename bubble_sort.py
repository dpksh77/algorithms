#bubble sort program


class bubble_sort:


	def __init__(self):

		self.arr=[2,6,4,3]

		print(type(self.arr))

	def sort_list(self):

		length=len(self.arr)
		print(length)

		for i in range(1,length):
			for j in range(1,length):

				if self.arr[j] < self.arr[j-1]:

					self.arr[j], self.arr[j-1] = self.arr[j-1], self.arr[j]

		return self.arr			

output=bubble_sort()
arr2=[6,7,4,9]
print(output.sort_list())
