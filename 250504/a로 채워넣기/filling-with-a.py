# 문자열을 입력받습니다.
string = input()

# 문자열의 길이를 구합니다.
leng = len(string)

# 문자열의 앞에서 두 번째 원소와 뒤에서 두 번째 원소를 'a'로 대체합니다.
string = string[:1] + 'a' + string[2:]
string = string[:leng - 2] + 'a' + string[leng - 1:]
	
# 대체된 이후의 문자열을 출력합니다
print(string)
