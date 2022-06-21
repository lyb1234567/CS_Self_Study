
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

