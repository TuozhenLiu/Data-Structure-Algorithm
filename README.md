# Data-Structure-Algorithm

### Binary Search

注意查找区间是右开还是右闭

- [left, right]，`left, right = 0, len(nums)-1`，`while left <= right`，`left = mid+1`，`right = mid-1`
  - 注意如果是Insert（替换到较大的），要返回`right+1`或`left`。
- [left, right)，`left, right = 0, len(nums)`，`while left < right`，`left = mid+1`，`right = mid`

### Two Pointer

快慢指针（同向），高低（左右）指针（反向）

### Linked list

- Dummy head

- Iteration vs Two Pointer: 
  - Iteration has one main pointer

- Iteration vs Recrusion
  - 空间：迭代O(1) < 递归O(N)
  - 时间：迭代O(1) = 递归O(1)

### Hashtable

- Array Hash
- Set Hash
- Map Hash

### Heap

- 向上调整
- 向下调整

初始化、插入、删除

https://blog.csdn.net/qq_36528114/article/details/78173951

Binary Tree

- DFS 深度优先
  - 前序、中序、后序遍历
    - 递归、递推（stack）
- BFS 广度优先
  - 层序遍历
    - queue
- 通过本题可以了解求二叉树深度 和 二叉树高度的差异，求深度适合用前序遍历，而求高度适合用后序遍历。 

BST 二叉搜索树采用中序遍历，其实就是一个有序数组。

- 平衡二叉搜索数是不是二叉搜索树和平衡二叉树的结合？
  - 是的，是二叉搜索树和平衡二叉树的结合。

- 平衡二叉树与完全二叉树的区别在于底层节点的位置？
  - 是的，完全二叉树底层必须是从左到右连续的，且次底层是满的。

- 堆是完全二叉树和排序的结合，而不是平衡二叉搜索树？
  - 堆是一棵完全二叉树，同时保证父子节点的顺序关系（有序）。 但完全二叉树一定是平衡二叉树，堆的排序是父节点大于子节点，而搜索树是父节点大于左孩子，小于右孩子，所以堆不是平衡二叉搜索树。




