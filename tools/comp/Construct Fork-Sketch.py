vect = th.tree_to_list(Vectors)
vectors = {}
i = 0
for fork in vect:
    if fork is not None:
        f = []
        for path in fork:
            if path is not None:
                for branch in path:
                    b = []
                    for v in branch:
                        b.append([v.X, v.Y, v.Z])
                    f.append(b)
    vectors[i] = f
    i+=1

rad = th.tree_to_list(Radius)
radius = {}
i = 0
for fork in rad:
    if fork is not None:
        f = []
        for path in fork:
            if path is not None:
                for branch in path:
                    b = []
                    for r in branch:
                        b.append(r)
                    f.append(b)
    radius[i] = f
    i+=1

trans = th.tree_to_list(Transform)
transform = {}
i = 0
for fork in trans:
    if fork is not None:
        f = []
        for t in fork:
            matrix = [
                [t.M00, t.M01, t.M02, t.M03],
                [t.M10, t.M11, t.M12, t.M13],
                [t.M20, t.M21, t.M22, t.M23],
                [t.M30, t.M31, t.M32, t.M33]
            ]
            f.append(matrix)
    transform[i] = f[0]
    i+=1

instance = []
for f in vectors:
    inst = Fork().construct(vectors[f], radius[f], transform[f]).json
    instance.append(inst)

Instance = th.list_to_tree(instance)