left = 0
data = 1
right = 2

# this first implementation of the tree uses a 2D list (not technically an array as not all data types are the same)

array_tree = [
    [1,"M",2],
    [3,"H",4],
    [5,"T",6],
    [None,"D",None],
    [None,"K",None],
    [None,"R",None],
    [None,"X",None]
]

def in_order_traverse(p):
    if array_tree[p][left] != None:
        in_order_traverse(array_tree[p][left])
    print(array_tree[p][data])
    if array_tree[p][right] != None:
        in_order_traverse(array_tree[p][right])

def pre_order_traverse(p):
    print(array_tree[p][data])
    if array_tree[p][left] != None:
        pre_order_traverse(array_tree[p][left])
    if array_tree[p][right] != None:
        pre_order_traverse(array_tree[p][right])

def post_order_traverse(p):
    if array_tree[p][left] != None:
        post_order_traverse(array_tree[p][left])
    if array_tree[p][right] != None:
        post_order_traverse(array_tree[p][right])
    print(array_tree[p][data])

print("\n")
in_order_traverse(0)
print("\n")
pre_order_traverse(0)
print("\n")
post_order_traverse(0)