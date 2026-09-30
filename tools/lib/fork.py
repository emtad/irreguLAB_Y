class Fork:
    def __init__(self):
        self.uuid = str(gu.uuid4()) # uuid v4 for unique identification
        self.sid = self.uuid[:5] # short form id to be human readable
        self.vect = None # nested list containing branch control point vectors (relative to bifurcation node) [[branch 0 start vector, end vector, end point], [branch 1, ...], [branch 2 ...]]
        self.rad = None # list containing end radius per branch ()
        self.trans = None # transform from world xy to position when captured

    def construct(self, vect, rad, trans=None, pos=None):
        self.vect = vect
        self.rad = rad
        self.trans = trans
        return self

    def read(self, inst):
        self.uuid = inst['uuid']
        self.sid = inst['sid']
        self.vect = inst['vect']
        self.rad = inst['rad']
        self.trans = inst['trans']
        return self

    def deconstruct(self):
        uuid = self.uuid
        sid = self.sid
        vect = self.vect
        rad = self.rad
        trans = self.trans
        return (uuid, sid, vect, rad, trans)
    
    @property
    def json(self):
        json = {
        'uuid' : self.uuid,
        'sid' : self.sid,
        'vect' : self.vect,
        'rad' : self.rad,
        'trans' : self.trans,
        }
        return json