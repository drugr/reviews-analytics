#讀取reviews.txt檔
#data = []
#count = 0
#with open('reviews.txt', 'r') as file:
#	for line in file:
#		data.append(line)
#		count += 1
#		if count % 1000 == 0:
#			print(len(data))

#print('檔案讀取完了，總共有', len(data), '筆資料')


data = []
#count = 0
with open('reviews.txt', 'r') as file:
	for line in file:
		data.append(line)
total = len(data)
print(total)
count = 0
data1 = []
summ = 0
while count != total:
	length = 0
	length = len(data[count])
	summ += length
	aver = summ / total
	count += 1
	if count == total:
		break
print('平均長度為', aver)

