## Peak Finding
In this section, we are going to talking about the algorithm of peak Finding. Some corresponding concepts and code for implementation will given as follows:
- Concept
- Implementation


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