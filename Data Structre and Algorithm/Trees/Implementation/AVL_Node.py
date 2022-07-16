class AVL_Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
        self.parent = None
        self.bf=0