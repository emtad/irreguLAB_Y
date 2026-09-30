if None not in Instance:
    iden = []
    siden = []
    vectors = []
    radius = []
    transform = []
    position = []
    for inst in Instance:
        uuid, sid, vect, rad, trans, pos = Fork().read(inst).deconstruct()
        iden.append([uuid])
        siden.append([sid])

        tree = []
        for b in vect:
            branch = []
            for v in b:
                branch.append(rg.Vector3d(*v))
            tree.append(branch)
        vectors.append(tree)
  
        tree = []
        for b in rad:
            tree.append(b[0])
        radius.append(tree)

        i = trans
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
        transform.append([t])
        position.append([pos])

    UUID = th.list_to_tree(iden)
    ID = th.list_to_tree(siden)
    Vectors = th.list_to_tree(vectors)
    Radius = th.list_to_tree(radius)
    Transform = th.list_to_tree(transform)
    