import pandas as pd
from apps.home.models import GIModel, BayModel
from apps import db

def bay():
    data_src = "data/gi_bay.xlsx"
    data = pd.read_excel(data_src)
    columns = data.columns
    data_type = data.dtypes
    # print(columns)    
    # print(data_type)
    data2 = data.values
    for idx in range(data.shape[0]):
        out_data = data2[idx]
        ULTG = out_data[0]
        GI = out_data[1]
        BAY = out_data[2]
        FUNGSI = out_data[3]
        ID_FUNCTLOC = out_data[4]
        SUP_FUNCTLOC = out_data[5]
        NM_LOKASI = out_data[6]
        DESKRIPSI = out_data[7]
        ID_LOCATION = out_data[8]
        ID_PARENT = out_data[9]
        TEGANGAN = out_data[10]
        KD_FUNGSI = out_data[11]
        KD_WILAYAH = out_data[12]
        TGL_OPRS = out_data[13]
        TGL_TDK_OPRS = out_data[14]
        FLAG = out_data[15]
        WORKCENTER = out_data[16]
        ID_PLANT = out_data[17]
        ID_TRAGI = out_data[18]
        NOMORGI = out_data[19]
        KD_GROUPLOKASI = out_data[20]
        ID_SECTION = out_data[21]
        BOUND = out_data[22]
        BA_CODE = out_data[23]
        ASSET_LOKASI = out_data[24]
        BAYGROUP = out_data[25]
        MVA = out_data[26]
        NOSIRKIT = out_data[27]
        COSTCENTER = out_data[28]
        BC_FLC = out_data[29]

        model = BayModel(
            ULTG = ULTG,
            GI = GI,
            BAY = BAY,
            FUNGSI = FUNGSI,
            ID_FUNCTLOC = ID_FUNCTLOC,
            SUP_FUNCTLOC = SUP_FUNCTLOC,
            NM_LOKASI = NM_LOKASI,
            DESKRIPSI = DESKRIPSI,
            ID_LOCATION = ID_LOCATION,
            ID_PARENT = ID_PARENT,
            TEGANGAN = TEGANGAN,
            KD_FUNGSI = KD_FUNGSI,
            KD_WILAYAH = KD_WILAYAH,
            TGL_OPRS = TGL_OPRS,
            TGL_TDK_OPRS = TGL_TDK_OPRS,
            FLAG = FLAG,
            WORKCENTER = WORKCENTER,
            ID_PLANT = ID_PLANT,
            ID_TRAGI = ID_TRAGI,
            NOMORGI = NOMORGI,
            KD_GROUPLOKASI = KD_GROUPLOKASI,
            ID_SECTION = ID_SECTION,
            BOUND = BOUND,
            BA_CODE = BA_CODE,
            ASSET_LOKASI = ASSET_LOKASI,
            BAYGROUP = BAYGROUP,
            MVA = MVA,
            NOSIRKIT = NOSIRKIT,
            COSTCENTER = COSTCENTER,
            BC_FLC = BC_FLC
        )
        db.session.add(model)
        db.session.commit()
        print("all data of BayModel was inserted successfully")
'''
        ULTG =
        GI =
        BAY = 
        FUNGSI = 
        ID_FUNCTLOC = 
        SUP_FUNCTLOC = 
        NM_LOKASI = 
        DESKRIPSI = 
        ID_LOCATION = 
        ID_PARENT = 
        TEGANGAN = 
        KD_FUNGSI = 
        KD_WILAYAH = 
        TGL_OPRS = 
        TGL_TDK_OPRS = 
        FLAG = 
        WORKCENTER = 
        ID_PLANT = 
        ID_TRAGI = 
        NOMORGI = 
        KD_GROUPLOKASI = 
        ID_SECTION = 
        BOUND = 
        BA_CODE = 
        ASSET_LOKASI = 
        BAYGROUP = 
        MVA = 
        NOSIRKIT = 
        COSTCENTER = 
        BC_FLC = 
'''

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
    # bay()
    addAll()