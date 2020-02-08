# 数据结构思考

array，连续内存分配，通过index来进行访问

queue，先进先出 
stack, 后进先出

list， 不连续内存，每个节点包含指向下一个节点的地址
binaryTree，二叉树 就是指向左右两个节点
tree， 树，包含一组节点指向 文件系统就是典型的tree型
graph： 图，没有向树一样有明确的层级关系
trie：特殊的树，每个节点包含当前的字母和下一个指向的字母

segment tree：
balanced tree：
blackRed tree：
complete tree：

map： 表，查询O(K) 注意hash冲突  hash_code % bucket_size，kv无序
treeMap 树表， key值有序排列

防止冲突的两个方法，一个是拉链，将冲突的bucket改为linkList
另一个是openAddress法，占用其他的bucket

set: 集合，查询O(1), hash_code % bucket_size 只存key不存value

matrix 矩阵


heap: 栈， 优先队列实现 priority_queue
minheap
maxheap
heapify


# 算法思考

recursive: 递归本质就是stack, 后进先出
backtracking: 后退的同时把路径记录下来

two-point: 双指针，从两端往中间逼近

quick-select






