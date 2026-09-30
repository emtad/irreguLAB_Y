fm = FileManager('json', 'aggregation-draft', Path)
if Save is True and Draft is not None:
    fm.write(Draft)
elif Reset:
    fm.reset()