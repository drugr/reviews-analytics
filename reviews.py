#讀取reviews.txt檔
data = []
count = 0
with open('reviews.txt', 'r') as file:
	for line in file:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for line1 in data:
	sum_len += len(line1)
print('留言的平均長度為', sum_len / len(data))

