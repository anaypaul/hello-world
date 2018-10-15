from sort import mergesort
def sayHello():
	print("Hello, World!")
	print("file edit on web")

def main():
	sayHello()
	arr = list(map(int, input().split()))
	print(arr)
	mergesort(arr,0,len(arr)-1)
	print(arr)


if __name__ == '__main__':
	main()
