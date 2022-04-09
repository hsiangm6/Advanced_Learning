'''
#Definition for a binary tree node
class treeNode:
   def _init_(self, val=0, right=None, left=None):
      self.val=val
      self.right=right
      self.left=left


def doInvertTree(root):   
    """
   temp=root.left
   root.left=root.right
   root.right=temp"""
   if root==None:        #停止遞迴的設定:如果root是底的話則停止轉換
      return None       
    
   (root.left, root.right)=(root.right, root.left)   #此行是tuple assignment，是python的語法   #python裡可以這樣寫取代以上3行
   doInvertTree(root.left)                           #此行是最底層小樹的位置轉換   #在函式裡面呼叫同名函式就是"遞迴"
   doInvertTree(root.right)                          #此行是最底層小樹的位置轉換
   return root                                       #!!!記得回傳root

#這段的前2行是Leetcode本身給的程式碼，如果加上這段第3行，程式的真正運行便是def doInvertTree(root):
class solution:                                       #程式會從solution.invertTree開始運行而不是上面的函式
   def invertTree(self,root):     #這裡的invertTree的全名叫solution.invertTree   #題目給:root為treeNode
      return doInvertTree(root)                     #這裡的doInvertTree是往上一個的空函式
'''
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
    #print("self.val",self.val)
    

    
def invertTree(node):
  if node is None:
    return None

  node.left, node.right = node.right, node.left

  invertTree(node.left)
  invertTree(node.right)
  #print(node)

  return node

sample_tree = TreeNode(1)
sample_tree.left = TreeNode(2)
sample_tree.right = TreeNode(3)
sample_tree.left.left = TreeNode(4)
sample_tree.left.right = TreeNode(5)
sample_tree.right.left = TreeNode(6)
sample_tree.right.right = TreeNode(7)

def printTree(node):
  print(node.val, end="")
  if node.left:
    printTree(node.left)
  if node.right:
    printTree(node.right)

#print our initial structure
printTree(sample_tree)

#add a line break
print()

#create our inverted tree and print it
inverted_tree = invertTree(sample_tree)
printTree(inverted_tree)

