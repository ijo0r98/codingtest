# 동적계획법 > n으로 표현

# 다른 사람 풀이 https://moondol-ai.tistory.com/272
def solution(N, number):
  # 인덱스가 N을 몇 번 사용했는지를 나타냄 ex) dp_table[1]: 1번 사용, d_table[4]: 4번 사용
  dp_table = [[]]
  for i in range(1, 9): # N 조건이자 사용 횟수 조건(8보다 크면 -1 리턴)
    case = []
    for j in range(1, i):
        for k in dp_table[j]: # j번 사용한 경우의 수 원소 iteration
          for l in dp_table[i - j]: # i-j번 사용한 경우의 수 원소 iteration
              case.append(k + l) # 더하기
              if k - l >= 0: 
                  case.append(k - l) # 빼기
              case.append(k * l) # 곱하기
              if l != 0 and k != 0:
                  case.append(k // l) # 나누기
    case.append(int(str(N) * i)) # 숫자를 그대로 이어 붙인 케이스 ex) 55, 555
  
    if number in case:
        return i
    dp_table.append(list(set(case)))
  return -1



# 내 풀이
# 조건1) 사용할 수 있는 최대 횟수는 8번
# 조건2) +, -, /, * 만을 이용하며 / 의 경우 나머지는 무시

# n을 1번 이용했을 때, 2번 이용했을 때, 3번 이용했을 때..
# 각 만들어진 숫자 조합에서 찾으려는 수가 있는지 확인
# 없다면 횟수를 늘려서 반복

# 참고 https://www.hamadevelop.me/algorithm-n-expression/
# 특정 숫자만큼 5를 사용한 조합을 만들고 싶다면 해당 숫자를 만들수 있는 덧셈 조합의 경우의 수 끼리 사칙연산을 해 주면 되는 것이다.
