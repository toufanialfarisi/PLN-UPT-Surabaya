from apps import db


class GIModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ULTG = db.Column(db.String(100))
    STATUS_OPERASI = db.Column(db.String(100))
    ID_FUNCTLOC = db.Column(db.String(100))
    NM_LOKASI = db.Column(db.String(100))
    NM_LOKASI_URL = db.Column(db.String(100))
    TEGANGAN = db.Column(db.Integer)
    TGL_OPRS = db.Column(db.String(100))
    ALAMAT = db.Column(db.TEXT)
    LATITUDE = db.Column(db.Float(100))
    LONGITUDE = db.Column(db.Float(100))
    # GI_DETAIL = db.relationship("BayModel", backref='detail_gi')

    # def __repr__(self):
    #     return f"GI {NM_LOKASI} dengan ID {id} berhasil dibuat"
'''
Index(['ULTG', 'ULTG', 'BAY', 'FUNGSI', 'ID_FUNCTLOC', 'SUP_FUNCTLOC',
       'NM_LOKASI', 'DESKRIPSI', 'ID_LOCATION', 'ID_PARENT', 'TEGANGAN',
       'KD_FUNGSI', 'KD_WILAYAH', 'TGL_OPRS', 'TGL_TDK_OPRS', 'FLAG',
       'WORKCENTER', 'ID_PLANT', 'ID_TRAGI', 'NOMORGI', 'KD_GROUPLOKASI',
       'ID_SECTION', 'BOUND', 'BA_CODE', 'ASSET_LOKASI', 'BAYGROUP', 'MVA',
       'NOSIRKIT', 'COSTCENTER', 'BC_FLC'],
      dtype='object')
'''

class BayModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # id_gi_detail = db.Column(db.Integer, db.ForeignKey('gimodel.id'))
    ULTG = db.Column(db.String(100))
    GI =  db.Column(db.String(100))
    BAY = db.Column(db.String(100))
    FUNGSI = db.Column(db.String(100))
    ID_FUNCTLOC = db.Column(db.String(100))
    SUP_FUNCTLOC = db.Column(db.String(100))
    NM_LOKASI = db.Column(db.String(100))
    DESKRIPSI = db.Column(db.String(100))
    ID_LOCATION = db.Column(db.Float(100)) 
    ID_PARENT = db.Column(db.String(100))
    TEGANGAN = db.Column(db.Float(100))
    KD_FUNGSI = db.Column(db.String(100))
    KD_WILAYAH = db.Column(db.Float(100))
    TGL_OPRS = db.Column(db.String(100))
    TGL_TDK_OPRS = db.Column(db.String(100))
    FLAG = db.Column(db.Float(100))
    WORKCENTER = db.Column(db.String(100))
    ID_PLANT = db.Column(db.Float(100))
    ID_TRAGI = db.Column(db.Float(100))
    NOMORGI = db.Column(db.Float(100))
    KD_GROUPLOKASI = db.Column(db.Float(100))
    ID_SECTION = db.Column(db.String(100))
    BOUND = db.Column(db.String(100))
    BA_CODE = db.Column(db.Float(100))
    ASSET_LOKASI = db.Column(db.Float(100))
    BAYGROUP = db.Column(db.Float(100))
    MVA = db.Column(db.Float(100))
    NOSIRKIT = db.Column(db.Float(100))
    COSTCENTER = db.Column(db.Float(100))
    BC_FLC = db.Column(db.String(100))






