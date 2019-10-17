#讀取reviews.txt檔
data = []
count = 0
with open('reviews.txt', 'r') as file:
	for line in file:
		data.append(line)
#		count += 1
#		if count % 1000 == 0:
#			print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for line1 in data:
	sum_len += len(line1)
print('留言的平均長度為', sum_len / len(data))

new = []
for line2 in data:
	if len(line2) < 100:
		new.append(line2)
print('共有', len(new), '筆留言長度小於100個字') #the算三個字
print(new[0])
print(new[1])
