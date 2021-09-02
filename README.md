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







