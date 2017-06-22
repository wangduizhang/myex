#_*_coding:utf-8


#p1
s1 = 'tiebjhqoiiipb' 
sum = 0
for i in s1:
    if i in 'aeio'and i != '':
        sum += 1
print sum


#p2
 # Paste your code into this box 
s2 = 'jaobooobobobobobobbobobobobboboo'
num = 0
for i in range(len(s2)-2):
    if s2[i:i+3] == 'bob':
        num += 1
print num


#p3  
lenw = 0
star = 0
star2 = 0
end = 1
word = ''
s3 = 'njwygrcwohqldpzgqpqyyz'
while True:
    if end == len(s3):
        print word
        break
    elif s3[star2] <= s3[end]:
        star2 += 1
        end += 1
        if end == len(s3):
            lenw = end + 1 - star
            word = s3[star:end]
    elif s3[star2] > s3[end]:
        if lenw < (end - star):
            lenw = end + 1 - star
            word = s3[star:end]
        star = end 
        star2 = end
        end += 1






