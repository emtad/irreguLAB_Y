fm = FileManager('jsonl', 'fork-inventory', Path)
if Save is True and Instance is not None:
    fm.write(Instance)
elif Reset:
    fm.reset()