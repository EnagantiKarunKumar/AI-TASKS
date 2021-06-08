nums = []
with open('nums','r')as file:
    for line in file.readlines():
        nums.append(int((line.split(','))[0]))
sum = 0
for ln in nums:
    sum = sum + ln
    average = sum / len(nums)


print(nums)
print("Max number is :" ,max(nums))
print("Min number is :" ,min(nums))
print("Average of the numbers in the file is" ,average )
