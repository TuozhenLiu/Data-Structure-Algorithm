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





