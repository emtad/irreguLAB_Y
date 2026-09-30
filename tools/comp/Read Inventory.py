fm = FileManager('jsonl', 'fork-inventory', Path)
inst = fm.read()
Instances = th.list_to_tree(inst)