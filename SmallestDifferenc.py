def solve(arr1,arr2):
  arr1.sort()
  arr2.sort()
  currSum=float("inf")
  finalSum=float("inf")
  ans=[]
  i=0
  j=0
  while i<len(arr1) and j<len(arr2):
    first=arr1[i]
    second=arr2[j]
    if first>second:
      currSum=first-second
      j+=1
    elif second > first:
      currSum=second-first
      i+=1
    else:
      return [first,second]
    if finalSum>currSum:
      finalSum=currSum
      ans=[first,second]
      
    
  return ans

if __name__ == "__main__":
    arr1=[-1,3,5,10,20,28]
    arr2=[15,17,26,135,135]
    print(solve(arr1,arr2))