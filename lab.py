import pandas as pd
from apps.home.models import GIModel
from apps import db

def URL(NM_LOKASI):
    NM_LOKASI = NM_LOKASI.split()
    out = '-'.join(NM_LOKASI)
    return out

def addAll():
    data_src = "data/gi_uit_jbtb.xlsx"
    data = pd.read_excel(data_src)
    data2 = data.values
    ''' MEMASUKAN SEMUA DATA DARI DATASET KE DB '''
    for idx in range(data.shape[0]):
        test_data = data2[idx]
        ULTG = test_data[0]
        STATUS_OPERASI = test_data[1]
        ID_FUNCTLOC = test_data[2]
        NM_LOKASI = test_data[3]
        NM_LOKASI_URL = URL(NM_LOKASI = test_data[3])
        TEGANGAN = test_data[4]
        TGL_OPRS = test_data[5]
        ALAMAT = test_data[6]
        LATITUDE = test_data[7]
        LONGITUDE = test_data[8]

        model = GIModel(ULTG=ULTG,
                        STATUS_OPERASI=STATUS_OPERASI,
                        ID_FUNCTLOC=ID_FUNCTLOC,
                        NM_LOKASI=NM_LOKASI,
                        NM_LOKASI_URL=NM_LOKASI_URL,
                        TEGANGAN=TEGANGAN,
                        TGL_OPRS=TGL_OPRS,
                        ALAMAT=ALAMAT,
                        LATITUDE=LATITUDE,
                        LONGITUDE=LONGITUDE
                        )
        db.session.add(model)
        db.session.commit()
    print("All Data was inserted into db successfully")


def removeAll():
    query = GIModel.query.all()
    for dt in query:
        db.session.delete(dt)
        db.session.commit()
    print("data successfully deleted")


    


if __name__ == "__main__":
    addAll()