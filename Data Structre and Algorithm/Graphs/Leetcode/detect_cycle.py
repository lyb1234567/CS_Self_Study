graph = {
    '0' : ['1'],
    '1':['2','0'],
    '2':[ ]
}

def cycle_detect(g):
    visited=set()
    for i in g.keys():
        visited.add(i)
        for neighbour in g[i]:
            if neighbour in visited:
                return True
    print(visited)
    return False

if __name__=="__main__":
    print(cycle_detect(graph))