# 고득점 kit > hash > 전화번호 목록(L2)

# 1
def solution(phone_book):
    answer = True
    
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return answer


# 2
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False

    return True


# 3
def solution(phone_book):
    answer = True
    dict = {}

    for phone_number in phone_book:
        dict[phone_number] = 1
    
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in dict and temp != phone_number:
                answer = False
    
    return answer


#####
print(solution(["119", "97674223", "1195524421"])) # false
print(solution(["123","456","789"])) # true
print(solution(["12","123","1235","567","88"])) # false