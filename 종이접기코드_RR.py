n = int(input('접는 횟수를 입력하세요:'))

def zero_one_replace(string):
    new_str = ''
    for i in range(0,len(string)):
        if string[i] == '0':
            new_str = new_str+'1'
        else:
            new_str =new_str +'0'
    return new_str


code = '0'
reverse = '0'

for i in range(1,n):
    reverse = code[::-1]
    front = zero_one_replace(reverse)
    code = front+'0'+code
    
print("(0,1) code는 %s 입니다"%code)
print("code의 길이는 %d 입니다"%len(code))