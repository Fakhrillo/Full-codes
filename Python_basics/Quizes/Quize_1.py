""" 1st one is working fine"""
# def arrayCheck(nums):
#     if 1 in nums and 2 in nums and 3 in nums:
#         return True
#     else:
#         return False
# print(arrayCheck([1, 1, 2, 4, 1]))
"""This better solution of 1st """
# def arrayCheck(nums):
#     for i in range(len(nums)-2):
#         if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
#             return True
#     return False

# print(arrayCheck([1, 1, 2, 3, 1]))

""" 2nd one is good """

# def stringBits(str):    
#     a = ""
#     for i in range(len(str)):
#         if i%2 == 0:
#             a += str[i]
    
#     return a

# print(stringBits("Hello"))


""" 3rd one is also working fine"""
# def end_other(a, b):
#     a = a.lower()
#     b = b.lower()
#     if a.endswith(b) or b.endswith(a):
#         print("True")
#     else:
#         print("False")

# end_other("Hiabc", "abc")


"""Working good but code is poor """
# def doubleChar(str):
#     a = ""
#     for x in str:
#         a = a + x
#         a += x
#     print(a)
# doubleChar("AAbb")


# def count_evens(nums):
#     a = 0
#     for x in nums:
#         if x%2==0:
#             a+=1
#         else:
#             continue
#     print(a)

# count_evens([1, 3, 5])