def solve(arr,toMove):
  i=0
  j=len(arr)-1
  while i<j:
    while i<j and arr[j]==toMove:
      j-=1
    if arr[i]==toMove:
      arr[i],arr[j]=arr[j],arr[i]
    i+=1
  return arr

if __name__ == "__main__":
    arr=[2,1,2,2,2,3,4,2]
    print(solve(arr,2))