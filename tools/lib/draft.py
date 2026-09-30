class Draft:
    def __init__(self):
        self.uuid = str(gu.uuid4()) # uuid v4 for unique identification
        self.sid = self.uuid[:5] # short form id to be human readable
        self.inv = None # fork inventory
        self.tar = None # target fork topology
        self.trans = None # fork instance transformation

    def construct(self, tar, inv, trans):
        self.tar = tar
        self.inv = inv
        self.trans = trans
        return self

    def read(self, inst):
        self.uuid = inst['uuid']
        self.sid = inst['sid']
        self.tar = inst['tar']
        self.inv = inst['inv']
        self.trans = inst['trans']
        return self

    def deconstruct(self):
        uuid = self.uuid
        sid = self.sid
        tar = self.tar
        inv = self.inv
        trans = self.trans
        return (uuid, sid, tar, inv, trans)
    
    @property
    def json(self):
        json = {
        'uuid' : self.uuid,
        'sid' : self.sid,
        'tar' : self.tar,
        'inv' : self.inv,
        'trans' : self.trans
        }
        return json