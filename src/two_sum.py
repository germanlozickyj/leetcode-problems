
def twoSum(nums, target):
    queue = [0]

    while(queue):
        current_target = queue.pop()    
        for x in range(len(nums)):
            if x == current_target: continue

            if nums[current_target] + nums[x] == target:
                return [
                    current_target, x
                ]
        
        if current_target == len(nums):
            return []
        else:
            queue.append(current_target + 1)

print(twoSum([2,7,11,15], 9))
print('')
print(twoSum([3,2,4], 6))
print('')
print(twoSum([3,3], 6))
