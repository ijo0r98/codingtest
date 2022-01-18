# 4673. 셀프넘버

# def find_self(num):
#     for i in range(1, num):
#         self_num = i
#         while i:
#             self_num += (i%10)
#             i //= 10
#         if self_num == num:
#             return False
#     return True

# for num in range(1, 10001):
#     if find_self(num):
#         print(num)


nums = [False for i in range(1, 10001)]

def get_self_nums(array, limit):
    for i in range(1, limit):
        self_num = i
        while i != 0:
            self_num += (i%10)
            i //= 10
        if self_num < limit:
            array[self_num] = True
    return array
    
nums = get_self_nums(nums, 10000)
for i in range(1, 10000):
    if nums[i] == False:
        print(i)
