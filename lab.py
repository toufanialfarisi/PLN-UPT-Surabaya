import pandas as pd
from apps.home.models import GIModel, BayModel, PMTModel
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
            ULTG=ULTG,
            GI=GI,
            BAY=BAY,
            FUNGSI=FUNGSI,
            ID_FUNCTLOC=ID_FUNCTLOC,
            SUP_FUNCTLOC=SUP_FUNCTLOC,
            NM_LOKASI=NM_LOKASI,
            DESKRIPSI=DESKRIPSI,
            ID_LOCATION=ID_LOCATION,
            ID_PARENT=ID_PARENT,
            TEGANGAN=TEGANGAN,
            KD_FUNGSI=KD_FUNGSI,
            KD_WILAYAH=KD_WILAYAH,
            TGL_OPRS=TGL_OPRS,
            TGL_TDK_OPRS=TGL_TDK_OPRS,
            FLAG=FLAG,
            WORKCENTER=WORKCENTER,
            ID_PLANT=ID_PLANT,
            ID_TRAGI=ID_TRAGI,
            NOMORGI=NOMORGI,
            KD_GROUPLOKASI=KD_GROUPLOKASI,
            ID_SECTION=ID_SECTION,
            BOUND=BOUND,
            BA_CODE=BA_CODE,
            ASSET_LOKASI=ASSET_LOKASI,
            BAYGROUP=BAYGROUP,
            MVA=MVA,
            NOSIRKIT=NOSIRKIT,
            COSTCENTER=COSTCENTER,
            BC_FLC=BC_FLC
        )
        db.session.add(model)
        db.session.commit()
    print("all data of BayModel was inserted successfully")


def URL(NM_LOKASI):
    NM_LOKASI = NM_LOKASI.split()
    out = '-'.join(NM_LOKASI)
    return out


def GI():
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
        NM_LOKASI_URL = URL(NM_LOKASI=test_data[3])
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


def PMT():
    data_src = "data/peralatan/pmt.xlsx"
    data = pd.read_excel(data_src, sheet_name="data")
    data2 = data.values
    # print(data2.shape)
    for idx in range(data.shape[0]):
        pmt_data = data2[idx]
        NMTRAGI = pmt_data[0]
        NAMAGI = pmt_data[1]
        NAMABAY = pmt_data[2]
        STATUS_ALAT = pmt_data[3]
        TECHIDENTNO = pmt_data[4]
        EQ_NUMBER = pmt_data[5]
        EQUIPMENT_NUMBER = pmt_data[6]
        SERIAL_ID = pmt_data[7]
        ID_BAY = pmt_data[8]
        ID_FUNCTLOC = pmt_data[9]
        KODE_PST = pmt_data[10]
        KD_STATUS = pmt_data[11]
        TEG_OPRS = pmt_data[12]
        PHASA = pmt_data[13]
        TGL_OPRS = pmt_data[14]
        THN_BUAT = pmt_data[15]
        BUATAN = pmt_data[16]
        PENEMPATAN = pmt_data[17]
        KETERANGAN = pmt_data[18]
        FLAG = pmt_data[19]
        MERK = pmt_data[20]
        TIPE = pmt_data[21]
        ASSET = pmt_data[22]
        CONS_TYPE = pmt_data[23]
        DESCRIPTION = pmt_data[24]
        RATING_ARUS = pmt_data[25]
        BREAKING_CURRENT = pmt_data[26]
        MKNK_PGRK = pmt_data[27]
        MEDIA_PMDM = pmt_data[28]
        JENIS = pmt_data[29]
        RATING_TEG = pmt_data[30]
        MAKING_CURRENT = pmt_data[31]
        BIL = pmt_data[32]
        SIL = pmt_data[33]
        PFW = pmt_data[34]
        WKT_BUKA = pmt_data[35]
        WKT_TUTUP = pmt_data[36]
        WKT_BREAK = pmt_data[37]
        DUR_HUB_SING = pmt_data[38]
        SEKUENSIAL = pmt_data[39]
        TEKANAN = pmt_data[40]
        THN_KTK = pmt_data[41]
        THN_ISO = pmt_data[42]
        BERAT = pmt_data[43]
        STANDARD = pmt_data[44]
        PASANGAN = pmt_data[45]
        TOLERANSI = pmt_data[46]
        HOUSING = pmt_data[47]
        JML_TRIP_COIL = pmt_data[48]
        TYPE_ID = pmt_data[49]
        ID_KOMPARTEMEN = pmt_data[50]
        EQ_NUMBER_REF = pmt_data[51]
        CCODE = pmt_data[52]

        model = PMTModel(
            NMTRAGI=NMTRAGI,
            NAMAGI=NAMAGI,
            NAMABAY=NAMABAY,
            STATUS_ALAT=STATUS_ALAT,
            TECHIDENTNO=TECHIDENTNO,
            EQ_NUMBER=EQ_NUMBER,
            EQUIPMENT_NUMBER=EQUIPMENT_NUMBER,
            SERIAL_ID=SERIAL_ID,
            ID_BAY=ID_BAY,
            ID_FUNCTLOC=ID_FUNCTLOC,
            KODE_PST=KODE_PST,
            KD_STATUS=KD_STATUS,
            TEG_OPRS=TEG_OPRS,
            PHASA=PHASA,
            TGL_OPRS=TGL_OPRS,
            THN_BUAT=THN_BUAT,
            BUATAN=BUATAN,
            PENEMPATAN=PENEMPATAN,
            KETERANGAN=KETERANGAN,
            FLAG=FLAG,
            MERK=MERK,
            TIPE=TIPE,
            ASSET=ASSET,
            CONS_TYPE=CONS_TYPE,
            DESCRIPTION=DESCRIPTION,
            RATING_ARUS=RATING_ARUS,
            BREAKING_CURRENT=BREAKING_CURRENT,
            MKNK_PGRK=MKNK_PGRK,
            MEDIA_PMDM=MEDIA_PMDM,
            JENIS=JENIS,
            RATING_TEG=RATING_TEG,
            MAKING_CURRENT=MAKING_CURRENT,
            BIL=BIL,
            SIL=SIL,
            PFW=PFW,
            WKT_BUKA=WKT_BUKA,
            WKT_TUTUP=WKT_TUTUP,
            WKT_BREAK=WKT_BREAK,
            DUR_HUB_SING=DUR_HUB_SING,
            SEKUENSIAL=SEKUENSIAL,
            TEKANAN=TEKANAN,
            THN_KTK=THN_KTK,
            THN_ISO=THN_ISO,
            BERAT=BERAT,
            STANDARD=STANDARD,
            PASANGAN=PASANGAN,
            TOLERANSI=TOLERANSI,
            HOUSING=HOUSING,
            JML_TRIP_COIL=JML_TRIP_COIL,
            TYPE_ID=TYPE_ID,
            ID_KOMPARTEMEN=ID_KOMPARTEMEN,
            EQ_NUMBER_REF=EQ_NUMBER_REF,
            CCODE=CCODE
        )
        db.session.add(model)
        db.session.commit()
    print("All PMT data was inserted")


if __name__ == "__main__":
    bay()
    GI()
    PMT()
