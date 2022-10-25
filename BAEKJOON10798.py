"""
word = []
word_length = []

for i in range(5):
    word.append(input())
    word_length.append(len(word))

for i in range(5):
    for j in range(max(word_length)):
        print(word[i][j])
"""
word = []
word_length = []
for i in range(5):
    word.append(list(input()))
    word_length.append(len(word[i]))

rst = ''
for i in range(max(word_length)):
    for j in range(5):
        #즉, i번째 열의 원소들을 행으로 가져올때 문자열의 길이가 i + 1 이어야 그 원소가 존재함
        if i < word_length[j]:
            rst = rst + word[j][i]

print(rst)

"""

"""