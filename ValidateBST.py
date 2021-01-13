def solve(tree):
  return solveHelper(tree,int("-inf"),int("inf"))

def solveHelper(tree,minval,maxval):
  if tree==None:
    return True
  if tree.value>=maxval or tree.value<minval:
    return False
  return solveHelper(tree.left,minval,tree.value) and solveHelper(tree.right,tree.value,maxval)