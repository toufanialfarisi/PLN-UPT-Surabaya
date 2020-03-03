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
    GI = db.Column(db.String(100))
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


class PMTModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    NMTRAGI = db.Column(db.String(100))
    NAMAGI = db.Column(db.String(100))
    NAMABAY = db.Column(db.String(100))
    STATUS_ALAT = db.Column(db.String(100))
    TECHIDENTNO = db.Column(db.String(100))
    EQ_NUMBER = db.Column(db.String(100))
    EQUIPMENT_NUMBER = db.Column(db.String(100))
    SERIAL_ID = db.Column(db.String(100))
    ID_BAY = db.Column(db.String(100))
    ID_FUNCTLOC = db.Column(db.String(100))
    KODE_PST = db.Column(db.Integer)
    KD_STATUS = db.Column(db.Integer)
    TEG_OPRS = db.Column(db.Integer)
    PHASA = db.Column(db.String(100))
    TGL_OPRS = db.Column(db.String(100))
    THN_BUAT = db.Column(db.Integer)
    BUATAN = db.Column(db.String(100))
    PENEMPATAN = db.Column(db.String(100))
    KETERANGAN = db.Column(db.String(100))
    FLAG = db.Column(db.Float(100))
    MERK = db.Column(db.String(100))
    TIPE = db.Column(db.String(100))
    ASSET = db.Column(db.String(100))
    CONS_TYPE = db.Column(db.Float(100))
    DESCRIPTION = db.Column(db.String(100))
    RATING_ARUS = db.Column(db.Float(100))
    BREAKING_CURRENT = db.Column(db.Float(100))
    MKNK_PGRK = db.Column(db.String(100))
    MEDIA_PMDM = db.Column(db.String(100))
    JENIS = db.Column(db.String(100))
    RATING_TEG = db.Column(db.Float(100))
    MAKING_CURRENT = db.Column(db.Float(100))
    BIL = db.Column(db.Float(100))
    SIL = db.Column(db.Float(100))
    PFW = db.Column(db.Float(100))
    WKT_BUKA = db.Column(db.Float(100))
    WKT_TUTUP = db.Column(db.Float(100))
    WKT_BREAK = db.Column(db.Float(100))
    DUR_HUB_SING = db.Column(db.Float(100))
    SEKUENSIAL = db.Column(db.String(100))
    TEKANAN = db.Column(db.Float(100))
    THN_KTK = db.Column(db.Float(100))
    THN_ISO = db.Column(db.Float(100))
    BERAT = db.Column(db.Float(100))
    STANDARD = db.Column(db.String(100))
    PASANGAN = db.Column(db.String(100))
    TOLERANSI = db.Column(db.Float(100))
    HOUSING = db.Column(db.String(100))
    JML_TRIP_COIL = db.Column(db.Float(100))
    TYPE_ID = db.Column(db.Float(100))
    ID_KOMPARTEMEN = db.Column(db.Float(100))
    EQ_NUMBER_REF = db.Column(db.String(100))
    CCODE = db.Column(db.Integer)


'''
Index(['NMTRAGI', 'NAMAGI', 'NAMABAY', 'STATUS_ALAT', 'TECHIDENTNO',
       'EQ_NUMBER', 'EQUIPMENT_NUMBER', 'SERIAL_ID', 'ID_BAY', 'ID_FUNCTLOC',
       'KODE_PST', 'KD_STATUS', 'TEG_OPRS', 'PHASA', 'TGL_OPRS', 'THN_BUAT',
       'BUATAN', 'PENEMPATAN', 'KETERANGAN', 'FLAG', 'MERK', 'TIPE', 'ASSET',
       'CONS_TYPE', 'DESCRIPTION', 'RATING_ARUS', 'BREAKING_CURRENT',
       'MKNK_PGRK', 'MEDIA_PMDM', 'JENIS', 'RATING_TEG', 'MAKING_CURRENT',
       'BIL', 'SIL', 'PFW', 'WKT_BUKA', 'WKT_TUTUP', 'WKT_BREAK',
       'DUR_HUB_SING', 'SEKUENSIAL', 'TEKANAN', 'THN_KTK', 'THN_ISO', 'BERAT',
       'STANDARD', 'PASANGAN', 'TOLERANSI', 'HOUSING', 'JML_TRIP_COIL',
       'TYPE_ID', 'ID_KOMPARTEMEN', 'EQ_NUMBER_REF', 'CCODE'],
      dtype='object')
'''
