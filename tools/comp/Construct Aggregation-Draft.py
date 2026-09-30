tar = Target
inv = {}
trans = {}
pos = {}

inventory = th.tree_to_list(Inventory)
transform = th.tree_to_list(Transform)
for inven, transf in zip(inventory, transform):
    inven = inven[0]
    iden = inven['uuid']
    inv[iden] = inven
    if transf is not None:
        for t in transf:
            matrix = [
                [t.M00, t.M01, t.M02, t.M03],
                [t.M10, t.M11, t.M12, t.M13],
                [t.M20, t.M21, t.M22, t.M23],
                [t.M30, t.M31, t.M32, t.M33]
            ]
            if iden in trans:
                trans[iden].append(matrix)
            else:
                trans[iden] = [matrix]

Draft = Draft().construct(tar, inv, trans).json