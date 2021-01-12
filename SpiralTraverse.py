def solve(arr):
  result=[]
  startRow,endRow=0,len(arr)-1
  startCol,endCol=0,len(arr[0])-1
  
  while startRow<=endRow and startCol<=endCol:
    for col in range(startRow,endCol+1):
      result.append(arr[startRow][col])

    for row in range(startRow+1,endRow+1):
      result.append(arr[row][endCol])

    for col in reversed(startCol,endCol):
      result.append(arr[endRow][col])

    for row in reversed(startRow+1,endRow):
      result.append(arr[row][startCol])
    
    startRow+=1
    startCol+=1
    endRow-=1
    endCol-=1

  return result

    