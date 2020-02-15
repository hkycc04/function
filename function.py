#function 函式/功能

def wash(dry=False, water=8):
	print('加水', water, '分滿')
	print('加洗衣精')
	print('旋轉')
	if dry:
		print('烘衣服')

wash(water=10)   #function功能執行


def say_hi():
	print('hi!')

# say_hi()

def add(x, y):
	return x + y

result = add(3, 4)
print(result)


def average(numbers):
	avg = sum(numbers) / len(numbers)
	return avg 

a = average([1, 2, 3])
print(a)

