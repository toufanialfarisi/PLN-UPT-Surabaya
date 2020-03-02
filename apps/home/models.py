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

    # def __repr__(self):
    #     return f"GI {NM_LOKASI} dengan ID {id} berhasil dibuat"
