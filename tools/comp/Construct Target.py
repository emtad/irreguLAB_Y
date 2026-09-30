inv = th.tree_to_list(Inventory)
inventory = {}

conn = th.tree_to_list(Connectivity)
connectivity = {}

pos = 0
for i, c in zip(inv, conn):
    i = i[0]
    inventory[pos] = i
    connectivity[pos] = c
    pos+=1

Target = Target().construct(inventory, connectivity).json