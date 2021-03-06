# 选择排序 

**原理**:

> 每一趟从待排序的记录中选出最小的元素，顺序放在已排好序的序列最后，直到全部记录排序完毕。

**实现**
# 插入排序

**原理:**

> 每步将一个待排序序列按数据大小插到前面已经排序的序列中的适当位置，直到全部数据插入完毕为止。 
>
> 假设有一组无序序列  ： 
> (1) 将这个序列的第一个元素视为一个有序序列； 
> (2) 依次把 剩下的元素依次插入到这个有序序列中； 
**实现**:
# 归并排序

**原理**:

> 先把待排序序列以中点二分，接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间. 

**实现**:
# 快速排序

**原理**:

> 取数组任一元素,以该元素划分数组,小于该元素放到left数组中,大于该元素的放到right数组.
>
> 划分完毕得到三个数组:比该元素小的数组,等于该元素的数组,大于该元素的数组.
>
> 将left,right数组重复执行之前的步骤.完毕,原数组有序.

**实现**:
# 堆排序

**原理**:

> - 构建大根堆/小根堆
> - 将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端
> - 重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序
>
> 1)父节点i的左子节点在位置(2*i+1);
> (2)父节点i的右子节点在位置(2*i+2);
> (3)子节点i的父节点在位置floor((i-1)/2);

**实现**:

# 希尔排序

**原理**:

> 改良版的插入排序,普通的插入排序,每次遍历只移动一个元素
>
> 而希尔排序的排序步长是在逐渐缩小至1.
>
> 假设有一组无序序列  ： 
> (1) 步长i设为数组长度的一半,将这个序列的前i个元素视为一个有序序列； 
> (2) 从第i+1个开始,依次将元素按照步长插入到 "有序序列"

**实现**:
# 小范围排序

已知一个几乎有序的数组，几乎有序是指，如果把数组排好顺序的话，每个元素移动的距离可以不超过k，并且k相对于数组来说比较小。请选择一个合适的排序算法针对这个数据进行排序。

**原理**：

> 采用原始序列对排序过程有影响的算法：堆排序，插入排序。

**实现：**
# 重复值判断

> 用速度快的排序算法排序，然后俩俩比较，发现相同的就返回
# 有序数组合并

> 数组合并很像 归并排序的 “归并”操作，但由于A数组具有包容B数组的空间，所以不需要“归并”时，借助一个缓冲数组。
>
> 当A数组与B数组从大到小比较时，将大的放在A数组末尾，这样依次迭代下去，即可完成排序