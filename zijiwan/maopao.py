# coding :utf-8
nums = [9,8,7,6,5,3,4,1,2]
s = [9,8,7,6,5,3,4,1,2]
s.sort()
print(s)
# for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
#     for j in range(len(nums) - i - 1):  # ｊ为列表下标
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print(nums)