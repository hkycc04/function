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

def add(x=1, y=1):
	print(x + y)

add(y=5)