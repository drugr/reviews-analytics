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
for line in data:
	sum_len += len(line)
print('留言的平均長度為', sum_len / len(data))

new = []
for line in data:
	if len(line) < 100:
		new.append(line)
print('共有', len(new), '筆留言長度小於100個字') #the算三個字
print(new[0])
print(new[1])

good = []
for line in data:
	if 'good' in line:
		good.append(line)
print('一共有', len(good), '筆留言提到good')
#print(good)

good = [d for d in data if 'good' in d]
#第一個d是運算，第57堂課

bad = ['bad' in d for d in data]
print(bad)
#意思同下列
bad = []
for d in data:
	bad.append('bad' in d)