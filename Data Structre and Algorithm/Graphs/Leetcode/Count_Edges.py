graph = {
    '0' : ['2','5'],
    '1' : [ ],
    '2' : ['3','4'],
    '3' : ['6'],
    '4' : [ ],
    '5' : ['3','6'],
    '6': ['4','7','8'],
    '7': ['8'],
    '8': [],
}

queue=[]
visited=[]
def count_edges(g):
    count=0
    for i in g.keys():
        count=count+len(g[i])
    return count/2

print(count_edges(graph))

