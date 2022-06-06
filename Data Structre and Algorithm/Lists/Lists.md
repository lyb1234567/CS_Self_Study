#Lists
This section demonstrates some content of python list, including the concept of shallow copy and deep copy with some corresponding codes.

## Table of content
- [Table of content](#table-of-content)
  - [Copy](#copy)
  - [Shallow copy](#shallow-copy)
  - [Deep Copy](#deep-copy)


### Copy
Before we start to talk about copies, let's first see some copy examples from python

```python

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

```
As shown above, I change the one of the values from the original list. And let's see the output:

```python
Old List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ID of Old List: 140673303268168

New List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ID of New List: 140673303268168
```
As we can see  here, although we already assigned the old list to the new list before chaning the old list, the new list still changes with the change of list, which shows that the list structure in python is **reference**.

Essentially, sometimes you may want to have the original values unchanged and only modify the new values or vice versa. In Python, there are two ways to create copies:
- [Table of content](#table-of-content)
  - [Copy](#copy)
  - [Shallow copy](#shallow-copy)
  - [Deep Copy](#deep-copy)

In python, we have two methods for shallow copy and deep copy:

```python
import copy
copy.copy(x)
copy.deepcopy(x)
```
### Shallow copy
A shallow copy creates a new object which stores the reference of the original elements.

So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.

```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
```
As we can see here, we let the original list append a new list. Here is the output:
```python
Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```
We can see that, the new list doesn't change with the change of the original list anymore, since it doesn't create a nested object.

However, when we change the value of one of the nested object from the original list:
```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)
```

**Output**
```python
Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
```
As we can see here, the new list's nested object's content changes as well, since the old and new list share the same reference of the nested object

同时还有一个很重要的问题，就是在python 浅拷贝中，修改可变对象（list）不需要开辟新的空间，而修改不可变对象（str, tuple）需要开辟新的空间.对源对象的不可变元素进行修改，会开辟新的内存，就有新的引用，而浅拷贝是指向的修改前的引用，所以浅拷贝不变。

**Example**
``` python
>>> a=['hello',[1,2,3]]
>>> b=a[:]
>>> [id(x) for x in a]
[55792504, 6444104]
>>> [id(x) for x in b]
[55792504, 6444104]
>>> a[0]='world'
>>> a[1].append(4)
>>> print(a)
['world', [1, 2, 3, 4]]
>>> print(b)
['hello', [1, 2, 3, 4]]
```
可以看到，我们修改了a中字符串的值，并没有使b中的字符串对象发生变化，但我们修改了a中 list对象中的值后，b中的list对象的值发生了变化
### Deep Copy
A deep copy of an object is a copy whose properties do not share the same references (point to the same underlying values) as those of the source object from which the copy was made.

```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
```

**Output**
```python
Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```
As we can see here, with the change of the elements of the original list, the new list doesn't change at all, since they do not share the sam reference