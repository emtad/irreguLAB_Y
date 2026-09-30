if Instance is not None:
    uuid, sid, tar, inv, trans = Draft().read(Instance).deconstruct()

    target = []
    branches = tar
    for b in branches:
        branch = []
        for v in b:
            branch.append(rg.Vector3d(*v))
        target.append(branch)

    inventory = []
    iden = []
    for key, item in inv.items():
        inventory.append([item])
        iden.append(key)

    transform = []
    branches = []
    for i in iden:
        if i in trans:
            branches.append([trans[i]])
        else:
            branches.append([])
    for b in branches:
        branch = []
        for i in b:
            t = rg.Transform.Identity
            t.M00 = i[0][0]
            t.M01 = i[0][1]
            t.M02 = i[0][2]
            t.M03 = i[0][3]

            t.M10 = i[1][0]
            t.M11 = i[1][1]
            t.M12 = i[1][2]
            t.M13 = i[1][3]

            t.M20 = i[2][0]
            t.M21 = i[2][1]
            t.M22 = i[2][2]
            t.M23 = i[2][3]

            t.M30 = i[3][0]
            t.M31 = i[3][1]
            t.M32 = i[3][2]
            t.M33 = i[3][3]
            
            branch.append(t)
        transform.append(branch)

    Target = th.list_to_tree(target)
    Inventory = th.list_to_tree(inventory)
    Transform = th.list_to_tree(transform)