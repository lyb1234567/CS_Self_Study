## Peak Finding
In this section, we are going to talking about the algorithm of peak Finding. Some corresponding concepts and code for implementation will given as follows:
- [Concept](#concept)
- [Implementation](#implementation)
- [Comparison](#comparison-of-the-binary-search-and-noraml-version-of-peakfinding-algorithm)


### Concept
Before we start to talk about the peak finding algorithm, we first need to define the concept of a peak in a list. By peak in a **1D** list, we mean if in at i, $p_i \geq p_{i-1}$ and $p_i \geq p_{i+1}$， we said $p_i$ is a peak. And, at the end of the **1D** array, we can say the last element is a peak, if $p_{last}>p_{last-1}$.

### Implementation

**Straight Algorithm**
First, the straightforward Algorithm, will be just traverse all the elements of the one dimension array and use the condtion above to find the peak. The worst time complexity is $O(n)$. 

The implementation is:
```python
def peak_finder_normal(lst):
    peak=[]
    find_peak=False
    neighbour=[]
    for i in range(len(lst)):
        if i>=0 and i<len(lst)-1:
            if lst[i]>=lst[i-1] and lst[i]>lst[i+1]:
                find_peak = True
                peak.append(lst[i])
                left=lst[i-1]
                right=lst[i+1]
                neighbour.append(left)
                neighbour.append(right)
                break
        else:
            if lst[i]>=lst[i-1]:
                find_peak = True
                peak.append(lst[i])
                left = lst[i - 1]
                neighbour.append(left)
                break
    if find_peak:
        return (peak,neighbour)
    else:
        return False
```
**Improvemen: Binary Search of the sublist**
To improve the starightforward algorithm, we can first start with the middle of the one dimension array, and the direction can be determined by checking if the current middle element is greater or equal to its neighbours. If so, then we find a peak, otherwise, the direction will start from the element which is bigger than the current middle element and update the middle index.

The computational complexity can be:
$$ T(n)=T(\frac{n}{2})+\theta(1)+\dots(log2(n) times)\theta(1)=\theta(log2(n))$$

The implementation is:
```python
def peak_finder_binary_search(lst):
    peak=[]
    find_peak=False
    middle=(len(lst)-1)>>1
    low=0
    high=len(lst)-1
    neighbour=[]
    while middle>low and middle<high:
        if lst[middle]>=lst[middle+1] and lst[middle]>=lst[middle-1]:
            find_peak=True
            peak.append(lst[middle])
            left = lst[middle - 1]
            right = lst[middle + 1]
            neighbour.append(left)
            neighbour.append(right)
            break
        else:
            if lst[middle+1]>=lst[middle]:
                middle=(middle+1+high)>>1
            elif lst[middle -1] >= lst[middle]:
                middle=(middle-1+low)>>1
    if find_peak:
        return (peak,neighbour)
    else:
        return find_peak 
```

**Comparison**
If $n=10000000$, the noram peakfinder will cost around 2300000 ms, while the peak finder using binary search will cost only 26 ms, which is a lot more efficient !!:

![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/MIT-6.006/PeakFinding/image/Comparison.png?raw=true)

**2D**
When it comes to Two-dimensional version:
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/MIT-6.006/PeakFinding/image/2D.PNG?raw=true)
if a is a peak, then it mush satisfy the following condition:
$$a\geq b, a\geq c, a\geq d, a\geq e$$

**Implementation**

**Dive and conquer** 
- Pick middle column j=m/2
- Find global maximum on column j at (i,j)
- Compare (i,j-1),(i,j) and (i,j+1)
- pick (i,j-1)>(i,j)
- Similarly for right
- (i,j) is a 2D-peak if neither condition holds
- Solve the new problems with half the numebr of columns
- When you have a singel column, find global maximum and you are done

The implementation will be:
```python
import numpy as np
def slice_column(lst,index):
    if len(lst)<=1:
        return lst[lst[0][index]]
    else:
        temp=[]
        for i in range(len(lst)):
            temp.append(lst[i][index])
        return temp

def slice_column_multiple(lst,start,stop):
    if len(lst)<=1:
        return lst[start:stop]
    else:
        temp=[]
        for i in range(len(lst)):
            temp.append(lst[i][start:stop+1])
        return temp
def array_to_lst(lst):
    temp=[]
    for i in range(len(lst)):
        temp.append(lst[i][0])
    return temp

def peak_finder(lst):
    sub_lst=lst[0]
    support_lst=lst
    length=len(sub_lst)
    middle=(len(sub_lst)-1)>>1
    low=0
    high=len(sub_lst)-1
    find_peak=False
    peak=[]
    while middle>=low and middle<=high:
        temp=slice_column(lst,middle)
        temp_max=max(temp)
        temp_max_index=temp.index(temp_max)
        sublist=lst[0]
        if len(sublist)==1:
            lst=array_to_lst(lst)
            peak.append(max(lst))
            return peak
        if lst[temp_max_index][middle]>=lst[temp_max_index][middle-1] and lst[temp_max_index][middle]>=lst[temp_max_index][middle+1]:
            peak.append(lst[temp_max_index][middle])
            break
        elif lst[temp_max_index][middle]<lst[temp_max_index][middle-1]:
            if middle==0:
                middle = middle + 1
                lst = slice_column_multiple(lst, middle, high)
                temp_list = lst[0]
                high = len(temp_list) - 1
                middle = high >> 1
                continue
            middle=middle-1
            lst=slice_column_multiple(lst,low,middle)
            temp_lst=lst[0]
            middle=len(temp_lst)-1
        elif lst[temp_max_index][middle]<lst[temp_max_index][middle+1]:
            middle=middle+1
            lst = slice_column_multiple(lst, middle,high)
            temp_list=lst[0]
            high=len(temp_list)-1
            middle=high>>1
    return peak
```
**Scan all the element**
We can also scan all the elements of the 2D version, which however will cause time complexity of $O(n^2)$
```python
def peak_finder_noraml(lst):
    peak=[]
    for i in range(len(lst)):
        sublst=lst[i]
        for j in range(len(sublst)):
            if i==0 and j==0:
                if lst[i][j]>=lst[i+1][j] and lst[i][j]>=lst[i][j+1]:
                    peak.append(lst[i][j])
                    return peak
            if i==0 and j==len(lst[0])-1:
                if lst[i][j] >= lst[i + 1][j] and lst[i][j] >= lst[i][j-1]:
                    peak.append(lst[i][j])
                    return peak
            if i==len(lst)-1 and j==0:
                if lst[i][j] >= lst[i-1][j] and lst[i][j] >= lst[i][j+1]:
                    peak.append(lst[i][j])
                    return peak
            if i==len(lst)-1 and j==len(lst[0])-1:
                if lst[i][j] >= lst[i-1][j] and lst[i][j] >= lst[i][j-1]:
                    peak.append(lst[i][j])
                    return peak
            if i==0 and j>0 and j<len(lst[0])-1:
                if lst[i][j]>=lst[i][j+1] and lst[i][j]>=lst[i][j-1] and lst[i][j]>=lst[i+1][j]:
                    peak.append(lst[i][j])
                    return peak
            if i==len(lst)-1 and j>0 and j<len(lst[0])-1:
                if lst[i][j]>=lst[i][j+1] and lst[i][j]>=lst[i][j-1] and lst[i][j]>=lst[i-1][j]:
                    peak.append(lst[i][j])
                    return peak
            if i>0 and i<len(lst)-1 and j>0 and j<len(lst[0])-1:
                if lst[i][j] >= lst[i][j + 1] and lst[i][j] >= lst[i][j - 1] and lst[i][j] >= lst[i - 1][j] and lst[i][j]>=lst[i+1][j]:
                    peak.append(lst[i][j])
                    return peak
            if j==0 and i>0 and i<len(lst)-1:
                if lst[i][j]>=lst[i+1][j] and lst[i][j]>=lst[i-1][j] and lst[i][j]>=lst[i][j+1]:
                    peak.append(lst[i][j])
                    return peak
            if j==len(lst[0])-1 and i>0 and i<len(lst)-1:
                if lst[i][j]>=lst[i+1][j] and lst[i][j]>=lst[i-1][j] and lst[i][j]>=lst[i][j-1]:
                    peak.append(lst[i][j])
                    return peak
    return peak
```
### Comparison of the binary search and noraml version of Peakfinding Algorithm
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/MIT-6.006/PeakFinding/image/Comparison2.PNG?raw=true)