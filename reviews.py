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

print(data[0])


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
# input_word = input('輸入文字查詢留言筆數: ')
# good = [d for d in data if input_word in d]
# print(len(good))
#第一個d是運算，第57堂課

# bad = ['bad' in d for d in data]
# print(bad)
#意思同下列
# bad = []
# for d in data:
# 	bad.append('bad' in d)


wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		print('感謝使用本查詢功能')
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過喔!')














