class Target:
    def __init__(self):
        self.uuid = str(gu.uuid4()) # uuid v4 for unique identification
        self.sid = self.uuid[:5] # short form id to be human readable
        self.pinv = None # placeholder fork inventory as dictionary (position in topology - fork-sketch instance)
        self.conn = None # connectivity diagram as dictionary

    def construct(self, pinv, conn):
        self.pinv = pinv
        self.conn = conn
        return self

    def read(self, inst):
        self.uuid = inst['uuid']
        self.sid = inst['sid']
        self.pinv = inst['pinv']
        self.conn = inst['conn']
        return self

    def deconstruct(self):
        uuid = self.uuid
        sid = self.sid
        pinv = self.pinv
        conn = self.conn
        return (uuid, sid, pinv, conn)
    
    @property
    def json(self):
        json = {
        'uuid' : self.uuid,
        'sid' : self.sid,
        'pinv' : self.pinv,
        'conn' : self.conn,
        }
        return json

# dictionary for pinv:
#dictionary = {
#    'pos' : instance
#    # pos = position index of fork
#    # instance = fork instance
#}

#dictionary for conn:
#dictionary = {
#    'pos' : [[fork_index, branch_index], [fork_index, branch_index], [fork_index, branch_index]]
#    # pos = position index of fork
#    # list =  list containing indexes of connected forks per branch
#    # [[from branch 0 to fork a, branch b], [from branch 1 to fork c, branch d], [from branch 2 to fork e, branch f]]
#}

# reconstruction: create target skeleton from individual fork centerlines -> multi-piping
# - OUTPUT A: connectivity diagram:
#   - use transforms from placeholder fork inventory to recreate nodes
#   - use connectivity to draw lines between nodes
# - OUTPUT B: target skeleton
#   - load placeholder fork inventory and position with transforms to recreate points (shared points at joints are duplicate)
#   (- run target geometry script in reverse to fuse forks)
