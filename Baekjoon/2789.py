# 틀림
# words = list(map(str, input()))
# univ = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
# for word in words:
#     for sensored in univ:
#         if word == sensored:
#             words.remove(word)     
# print(''.join(words))

words = input() 
sensorship = 'CAMBRIDGE'
answer = ''

for i in range(len(words)):
    if words[i] not in sensorship:
        answer += words[i]
print(answer)