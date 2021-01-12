# Using hashtable
def TarSumT(arr, n):
    nums = {}
    for num in arr:
        if n-num in nums:
            return [n-num, num]
        else:
            nums[num] = True
    return []

#more optimised approach
def TarSumP(arr, n):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left]+arr[right] == n:
            return [arr[left], arr[right]]
        elif arr[left] + arr[right] < n:
            left += 1
        elif arr[left] + arr[right] > n:
            right -= 1
        
    return []

if __name__=='__main__':
    arr = [-1, 2, 36, 7, 11, 3]
    print(TarSumT(arr, 10))
    print(TarSumP(arr, 10))
