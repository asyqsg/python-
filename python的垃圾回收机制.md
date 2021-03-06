# python的垃圾回收机制

1：引用回收

每次生成新对象的时候都会自动分配内存

例如：

```python
a = node(1)#在第四行时，node(1)会被回收，引用为0
b = node(2)
c = node(3)
a = node(4)
```

即生成了一个内存

对于每一个内存都会生成引用计数，当引用计数为0时，python会自动回收内存，即垃圾回收（GC）



2.代回收

对于引用回收来说，其有一个缺陷：

**由其是在双向链表时**

```python
n1.next = n2
n2.pre = n1
```

n1和n2相互引用，引用总是不为0。

为此引入代回收（generation GC）

每当建立一个链表的时候，都会将其加入零代链表

随后遍历检查每个对象的引用次数，随后随着引用计数，将其按规则减去数字，当有对象引用数字为0时，其内存释放，此时引用数字不为0的放入一代链表，经过相同的过程，继续放入二代链表。



**什么时候继续遍历，或者说什么时候进行引用-的过程**

当计数对象的数值和被释放的对象计数差值到达某个阈值，其就会启动。



弱代假说：

即代数越大的，其遍历频率就会更少 --- **能够快速的处理那些变成垃圾的新对象**





[**参考文献**]( https://www.cnblogs.com/xiugeng/p/10514101.html )