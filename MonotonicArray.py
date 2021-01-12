def solve(arr):
  if len(arr)<=2:
    return True
  direction=arr[1]-arr[0]
  for i in range(2,len(arr)):
    if direction==0:
      direction=arr[i]-arr[i-1]
      continue
    if breakFunction(direction,arr[i-1],arr[i]):
      return False
  return True

def breakFunction(direction,prevNum,currNum):
  difference=prevNum - currNum
  if direction > 0:
    return difference < 0
  return difference > 0

def solve2(arr):
  isNonIncreasing=True
  isNonDecreasing=True
  for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
      isNonIncreasing=False
    if arr[i] < arr[i-1]:
      isNonDecreasing=False
  return isNonIncreasing or isNonDecreasing