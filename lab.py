import pandas as pd
from apps.home.models import (
    GIModel, 
    BayModel, 
    PMTModel, 
    PMSModel,
    CTModel,
    PTModel
)
from apps import db
import timeit


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
        print(out_data)
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
    print("all data of BayModel were inserted successfully")


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
        print(test_data)
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
    print("All GI Data were inserted into db successfully")


def removeAll():
    query = GIModel.query.all()
    for dt in query:
        db.session.delete(dt)
        db.session.commit()
    print("data successfully deleted")

def PMS():
    data_src = "data/peralatan/pms.xlsx"
    data = pd.read_excel(data_src)
    data2 = data.values
    out = data.loc[data['NMTRAGI'] == 'UPT SURABAYA']
    for idx in range(out.shape[0]):
        pms_data = out.values[idx]
        print(pms_data)
        NMTRAGI=pms_data[0]
        NAMAGI=pms_data[1]
        NAMABAY=pms_data[2]
        STATUS_ALAT=pms_data[3]

        ### bermasalah ###
        # TECHIDENTNO=pms_data[4]
        ### bermasalah ###

        EQ_NUMBER=pms_data[5]
        SERIAL_ID=pms_data[6]
        ID_BAY=pms_data[7]
        KODE_PST=pms_data[8]
        KD_STATUS=pms_data[9]
        TEG_OPRS=pms_data[10]
        MERK=pms_data[11]
        TIPE=pms_data[12]
        PHASA=pms_data[13]
        BUATAN=pms_data[14]
        THN_BUAT=pms_data[15]
        TGL_OPRS=pms_data[16]
        PENEMPATAN=pms_data[17]
        KETERANGAN=pms_data[18]
        FLAG=pms_data[19]
        ID_KOMPARTEMEN=pms_data[20]
        KELENGKAPAN=pms_data[21]
        ASSET=pms_data[22]
        CONS_TYPE=pms_data[23]
        JENIS=pms_data[24]
        TEG_NOM=pms_data[25]
        ARUS_NOM=pms_data[26]
        MKNK_PGRK=pms_data[27]
        SHORT_TIME_SCC=pms_data[28]
        PEAK_SCC=pms_data[29]
        BIL=pms_data[30]
        SIL=pms_data[31]
        PFW=pms_data[32]
        BERAT=pms_data[33]
        STANDART=pms_data[34]
        PASANGAN=pms_data[35]
        WKT_BUKA=pms_data[36]
        WKT_TUTUP=pms_data[37]
        THN_KTK=pms_data[38]
        ARUS_HS_PEAK=pms_data[39]
        CREEP_DIST_SUPPORT=pms_data[40]
        DUR_HUB_SING=pms_data[41]
        TEG_AC_MOTOR=pms_data[42]
        TEG_DC_MOTOR=pms_data[43]
        MATERIAL_INSULATOR=pms_data[44]
        TYPE_ID=pms_data[45]
        EQUIPMENT_NUMBER=pms_data[46]
        ID_FUNCTLOC=pms_data[47]
        CCODE=pms_data[48]

        model = PMSModel(
            NMTRAGI=NMTRAGI,
            NAMAGI=NAMAGI,
            NAMABAY=NAMABAY,
            STATUS_ALAT=STATUS_ALAT,

            ### bermasalah ###
            # TECHIDENTNO=TECHIDENTNO,
            ### bermasalah ###

            EQ_NUMBER=EQ_NUMBER,
            SERIAL_ID=SERIAL_ID,
            ID_BAY=ID_BAY,
            KODE_PST=KODE_PST,
            KD_STATUS=KD_STATUS,
            TEG_OPRS=TEG_OPRS,
            MERK=MERK,
            TIPE=TIPE,
            PHASA=PHASA,
            BUATAN=BUATAN,
            THN_BUAT=THN_BUAT,
            TGL_OPRS=TGL_OPRS,
            PENEMPATAN=PENEMPATAN,
            KETERANGAN=KETERANGAN,
            FLAG=FLAG,
            ID_KOMPARTEMEN=ID_KOMPARTEMEN,
            KELENGKAPAN=KELENGKAPAN,
            ASSET=ASSET,
            CONS_TYPE=CONS_TYPE,
            JENIS=JENIS,
            TEG_NOM=TEG_NOM,
            ARUS_NOM=ARUS_NOM,
            MKNK_PGRK=MKNK_PGRK,
            SHORT_TIME_SCC=SHORT_TIME_SCC,
            PEAK_SCC=PEAK_SCC,
            BIL=BIL,
            SIL=SIL,
            PFW=PFW,
            BERAT=BERAT,
            STANDART=STANDART,
            PASANGAN=PASANGAN,
            WKT_BUKA=WKT_BUKA,
            WKT_TUTUP=WKT_TUTUP,
            THN_KTK=THN_KTK,
            ARUS_HS_PEAK=ARUS_HS_PEAK,
            CREEP_DIST_SUPPORT=CREEP_DIST_SUPPORT,
            DUR_HUB_SING=DUR_HUB_SING,
            TEG_AC_MOTOR=TEG_AC_MOTOR,
            TEG_DC_MOTOR=TEG_DC_MOTOR,
            MATERIAL_INSULATOR=MATERIAL_INSULATOR,
            TYPE_ID=TYPE_ID,
            EQUIPMENT_NUMBER=EQUIPMENT_NUMBER,
            ID_FUNCTLOC=ID_FUNCTLOC,
            CCODE=CCODE
        )
        db.session.add(model)
        db.session.commit()
        print("All PMS data were imported successfully")

def PMT():
    data_src = "data/peralatan/pmt.xlsx"
    data = pd.read_excel(data_src)
    data = data.loc[data['NMTRAGI'] == 'UPT SURABAYA']
    data = data.values
    # print(data2.shape)
    for idx in range(data.shape[0]):
        pmt_data = data[idx]
        print(pmt_data)
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
    print("All PMT data were inserted")


def CT():
    data_src = "data/peralatan/ct.xlsx"
    data = pd.read_excel(data_src)
    data = data.loc[data['NMTRAGI'] == 'UPT SURABAYA']
    data = data.values
    for idx in range(data.shape[0]):
        data_ct = data[idx]
        print(data_ct)
        NMTRAGI=data_ct[0]
        NAMAGI=data_ct[1]   
        NAMABAY=data_ct[2]
        STATUS_ALAT=data_ct[3]
        # TECHIDENTNO=data_ct[4]
        EQ_NUMBER=data_ct[5]
        EQUIPMENT_NUMBER=data_ct[6]
        SERIAL_ID=data_ct[7]
        ID_BAY=data_ct[8]
        ID_FUNCTLOC=data_ct[9]
        KODE_PST=data_ct[10]
        KD_STATUS=data_ct[11]
        TEG_OPRS=data_ct[12]
        MERK=data_ct[13]
        TIPE=data_ct[14]
        PHASA=data_ct[15]
        BUATAN=data_ct[16]
        THN_BUAT=data_ct[17]
        TGL_OPRS=data_ct[18]
        PENEMPATAN=data_ct[19]
        KETERANGAN=data_ct[20]
        ASSET=data_ct[21]
        CONS_TYPE=data_ct[22]
        FLAG=data_ct[23]
        ID_KOMPARTEMEN=data_ct[24]
        JENIS=data_ct[25]
        TEG_MAKS=data_ct[26]
        ISOLASI=data_ct[27]
        ISC_1S=data_ct[28]
        ISC_3S=data_ct[29]
        BIL=data_ct[30]
        SIL=data_ct[31]
        PFW=data_ct[32]
        TAP_CT=data_ct[33]
        I_RATED_PRI=data_ct[34]
        I_RATED_SEC=data_ct[35]
        RATING_ARUS=data_ct[36]
        I_THERM_CONT=data_ct[37]
        I_DYN=data_ct[38]
        BURDEN=data_ct[39]
        CLASS=data_ct[40]
        FUNGSI=data_ct[41]
        HOUSING=data_ct[42]
        CREEP_DIST=data_ct[43]
        HEAD_HOUSING=data_ct[44]
        BASE_HOUSING=data_ct[45]
        BERAT_TOT=data_ct[46]
        STANDARD=data_ct[47]
        JML_CORE=data_ct[48]
        RATIO_CORE_1=data_ct[49]
        CLASS_CORE_1=data_ct[50]
        BURDEN_CORE_1=data_ct[51]
        RATIO_CORE_2=data_ct[52]
        CLASS_CORE_2=data_ct[53]
        BURDEN_CORE_2=data_ct[54]
        RATIO_CORE_3=data_ct[55]
        CLASS_CORE_3=data_ct[56]
        BURDEN_CORE_3=data_ct[57]
        RATIO_CORE_4=data_ct[58]
        CLASS_CORE_4=data_ct[59]
        BURDEN_CORE_4=data_ct[60]
        RATIO_CORE_5=data_ct[61]
        CLASS_CORE_5=data_ct[62]
        BURDEN_CORE_5=data_ct[63]
        RATIO_CORE_6=data_ct[64]
        CLASS_CORE_6=data_ct[65]
        BURDEN_CORE_6=data_ct[66]
        PASANGAN=data_ct[67]
        TYPE_ID=data_ct[68]
        CCODE=data_ct[69] 

        model = CTModel(
            NMTRAGI=NMTRAGI,
            NAMAGI=NAMAGI,   
            NAMABAY=NAMABAY,
            STATUS_ALAT=STATUS_ALAT,
            # TECHIDENTNO=TECHIDENTNO,
            EQ_NUMBER=EQ_NUMBER,
            EQUIPMENT_NUMBER=EQUIPMENT_NUMBER,
            SERIAL_ID=SERIAL_ID,
            ID_BAY=ID_BAY,
            ID_FUNCTLOC=ID_FUNCTLOC,
            KODE_PST=KODE_PST,
            KD_STATUS=KD_STATUS,
            TEG_OPRS=TEG_OPRS,
            MERK=MERK,
            TIPE=TIPE,
            PHASA=PHASA,
            BUATAN=BUATAN,
            THN_BUAT=THN_BUAT,
            TGL_OPRS=TGL_OPRS,
            PENEMPATAN=PENEMPATAN,
            KETERANGAN=KETERANGAN,
            ASSET=ASSET,
            CONS_TYPE=CONS_TYPE,
            FLAG=FLAG,
            ID_KOMPARTEMEN=ID_KOMPARTEMEN,
            JENIS=JENIS,
            TEG_MAKS=TEG_MAKS,
            ISOLASI=ISOLASI,
            ISC_1S=ISC_1S,
            ISC_3S=ISC_3S,
            BIL=BIL,
            SIL=SIL,
            PFW=PFW,
            TAP_CT=TAP_CT,
            I_RATED_PRI=I_RATED_PRI,
            I_RATED_SEC=I_RATED_SEC,
            RATING_ARUS=RATING_ARUS,
            I_THERM_CONT=I_THERM_CONT,
            I_DYN=I_DYN,
            BURDEN=BURDEN,
            CLASS=CLASS,
            FUNGSI=FUNGSI,
            HOUSING=HOUSING,
            CREEP_DIST=CREEP_DIST,
            HEAD_HOUSING=HEAD_HOUSING,
            BASE_HOUSING=BASE_HOUSING,
            BERAT_TOT=BERAT_TOT,
            STANDARD=STANDARD,
            JML_CORE=JML_CORE,
            RATIO_CORE_1=RATIO_CORE_1,
            CLASS_CORE_1=CLASS_CORE_1,
            BURDEN_CORE_1=BURDEN_CORE_1,
            RATIO_CORE_2=RATIO_CORE_2,
            CLASS_CORE_2=CLASS_CORE_2,
            BURDEN_CORE_2=BURDEN_CORE_2,
            RATIO_CORE_3=RATIO_CORE_3,
            CLASS_CORE_3=CLASS_CORE_3,
            BURDEN_CORE_3=BURDEN_CORE_3,
            RATIO_CORE_4=RATIO_CORE_4,
            CLASS_CORE_4=CLASS_CORE_4,
            BURDEN_CORE_4=BURDEN_CORE_4,
            RATIO_CORE_5=RATIO_CORE_5,
            CLASS_CORE_5=CLASS_CORE_5,
            BURDEN_CORE_5=BURDEN_CORE_5,
            RATIO_CORE_6=RATIO_CORE_6,
            CLASS_CORE_6=CLASS_CORE_6,
            BURDEN_CORE_6=BURDEN_CORE_6,
            PASANGAN=PASANGAN,
            TYPE_ID=TYPE_ID,
            CCODE=CCODE,
        )
        db.session.add(model)
        db.session.commit()
    print("All CT Data were successfully imported")


def PT():
    data_src = "data/peralatan/pt.xlsx"
    data = pd.read_excel(data_src)
    data = data.loc[data['NMTRAGI'] == 'UPT SURABAYA']
    data = data.values 
    for idx in range(data.shape[0]):
        data_pt = data[idx]
        print(data_pt)
        NMTRAGI=data_pt[0]
        NAMAGI=data_pt[1]
        NAMABAY=data_pt[2]
        STATUS_ALAT=data_pt[3]
        SERIAL_ID=data_pt[4]
        TYPE_ID=data_pt[5]
        ID_BAY=data_pt[6]
        KODE_PST=data_pt[7]
        KD_STATUS=data_pt[8]
        TEG_OPRS=data_pt[9]
        PHASA=data_pt[10]
        BUATAN=data_pt[11]
        THN_BUAT=data_pt[12]
        TGL_OPRS=data_pt[13]
        KETERANGAN=data_pt[14]
        ID_KOMPARTEMEN=data_pt[15]
        FLAG=data_pt[16]
        MERK=data_pt[17]
        TIPE=data_pt[18]
        JENIS=data_pt[19]
        TEG_MAKS=data_pt[20]
        TEG_PRIM=data_pt[21]
        TEG_SEC=data_pt[22]
        JML_CORE=data_pt[23]
        CLASS_CORE_1=data_pt[24]
        CLASS_CORE_2=data_pt[25]
        CLASS_CORE_3=data_pt[26]
        BURDEN_CORE_1=data_pt[27]
        BURDEN_CORE_2=data_pt[28]
        BURDEN_CORE_3=data_pt[29]
        C1=data_pt[30]
        C2=data_pt[31]
        C3=data_pt[32]
        BIL=data_pt[33]
        SIL=data_pt[34]
        PFW=data_pt[35]
        RVF_CONT=data_pt[36]
        RVF_30S=data_pt[37]
        ISOLASI=data_pt[38]
        CREEP_DIST=data_pt[39]
        HOUSING=data_pt[40]
        TOLERANSI=data_pt[41]
        TAN_DELTA=data_pt[42]
        BERAT_TOTAL=data_pt[43]
        STANDARD=data_pt[44]
        PASANGAN=data_pt[45]
        RATED_FREQ=data_pt[46]
        PENEMPATAN=data_pt[47]
        WAVE_TRAP=data_pt[48]
        CONS_TYPE=data_pt[49]
        # TECHIDENTNO=data_pt[50]
        ASSET=data_pt[51]
        EQ_NUMBER=data_pt[52]
        EQUIPMENT_NUMBER=data_pt[53]
        ID_FUNCTLOC=data_pt[54]
        THERM_BURDEN=data_pt[55]
        CCODE=data_pt[56]
        model = PTModel(
            NMTRAGI=NMTRAGI,
            NAMAGI=NAMAGI,
            NAMABAY=NAMABAY,
            STATUS_ALAT=STATUS_ALAT,
            SERIAL_ID=SERIAL_ID,
            TYPE_ID=TYPE_ID,
            ID_BAY=ID_BAY,
            KODE_PST=KODE_PST,
            KD_STATUS=KD_STATUS,
            TEG_OPRS=TEG_OPRS,
            PHASA=PHASA,
            BUATAN=BUATAN,
            THN_BUAT=THN_BUAT,
            TGL_OPRS=TGL_OPRS,
            KETERANGAN=KETERANGAN,
            ID_KOMPARTEMEN=ID_KOMPARTEMEN,
            FLAG=FLAG,
            MERK=MERK,
            TIPE=TIPE,
            JENIS=JENIS,
            TEG_MAKS=TEG_MAKS,
            TEG_PRIM=TEG_PRIM,
            TEG_SEC=TEG_SEC,
            JML_CORE=JML_CORE,
            CLASS_CORE_1=CLASS_CORE_1,
            CLASS_CORE_2=CLASS_CORE_2,
            CLASS_CORE_3=CLASS_CORE_3,
            BURDEN_CORE_1=BURDEN_CORE_1,
            BURDEN_CORE_2=BURDEN_CORE_2,
            BURDEN_CORE_3=BURDEN_CORE_3,
            C1=C1,
            C2=C2,
            C3=C3,
            BIL=BIL,
            SIL=SIL,
            PFW=PFW,
            RVF_CONT=RVF_CONT,
            RVF_30S=RVF_30S,
            ISOLASI=ISOLASI,
            CREEP_DIST=CREEP_DIST,
            HOUSING=HOUSING,
            TOLERANSI=TOLERANSI,
            TAN_DELTA=TAN_DELTA,
            BERAT_TOTAL=BERAT_TOTAL,
            STANDARD=STANDARD,
            PASANGAN=PASANGAN,
            RATED_FREQ=RATED_FREQ,
            PENEMPATAN=PENEMPATAN,
            WAVE_TRAP=WAVE_TRAP,
            CONS_TYPE=CONS_TYPE,
            # TECHIDENTNO=TECHIDENTNO,
            ASSET=ASSET,
            EQ_NUMBER=EQ_NUMBER,
            EQUIPMENT_NUMBER=EQUIPMENT_NUMBER,
            ID_FUNCTLOC=ID_FUNCTLOC,
            THERM_BURDEN=THERM_BURDEN,
            CCODE=CCODE
        )
        db.session.add(model)
        db.session.commit()
    print("All PT Data were imported successfully")


def LA():
    pass 

def showMetaLA():
    pass 


    



def showMetaPT():
    data_src = "data/peralatan/pt.xlsx"
    data = pd.read_excel(data_src)
    data = data.loc[data['NMTRAGI'] == 'UPT SURABAYA']
    print(data.dtypes)

def queryProgress():
    bay()
    GI()
    PMT()
    PMS()
    CT()
    PT()

import os 
if __name__ == "__main__":
    queryProgress()
    
    
