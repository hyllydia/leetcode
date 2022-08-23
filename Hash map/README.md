**哈希表-Hash table , 哈希表是根据关键码的值而直接进行访问的数据结构。**

哈希表中关键码就是死数组的索引下标， 然后通过下标直接访问数组中的元素，如下图：

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f399e941-9138-4a10-a66e-423d61874cdf/Untitled.png)

一般哈希表都是用来快速判断一个元素是否出现集合里。复杂度为O(1)。

**哈希函数**

将元素映射到哈希表上， 涉及到hash function, 就是哈希函数。

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bcc0c644-b417-41c1-a2ed-26f9edaaa014/Untitled.png)

如果学生的数量大于哈希表的大小怎么办，此时就算哈希函数计算的再均匀，也避免不了会有几位学生的名字同时映射到哈希表 同一个索引下标的位置。

**哈希碰撞**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/49a2e40f-7e6e-4886-a056-0256898cc663/Untitled.png)

一般哈希碰撞有两种解决方法， **拉链法和线性探测法**。

### **总结**
当我们遇到了要快速判断一个元素是否出现集合里的时候， 就要考虑哈希法。

但是哈希法也是牺牲了空间换取了时间， 因为我们要使用额外的数组， 
set或者是map（字典）来存放数据， 才能实现快速的查找。

如果做面试题目的时候遇到需要判断一个元素是否出现过的场景也应该第一时间想到哈希法。