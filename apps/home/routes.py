from flask import Blueprint, render_template
from apps.home.models import GIModel, BayModel
import json

home = Blueprint("home", __name__, template_folder="templates/",
                 static_folder='static/')


@home.route("/")
def index():
    lon = []
    lat = []
    gi = []
    url = []
    ids = []
    query = GIModel.query.all()
    for data in query:
        out_ids = data.id
        out_url = data.NM_LOKASI_URL
        out_lon = data.LONGITUDE
        out_lon = float(out_lon)
        out_lat = data.LATITUDE
        out_lat = float(out_lat)
        out_gi = data.NM_LOKASI
        ids.append(out_ids)
        url.append(out_url)
        lon.append(out_lon)
        lat.append(out_lat)
        gi.append(out_gi)

    return render_template(
        "index.html",
        title="PLN UPT Surabaya",
        lons=lon,
        lats=lat,
        gis=gi,
        idx=ids
    )


@home.route("/<int:id>")
def gi_detail(id):
    queryNamaGI = GIModel.query.get(id)
    lat = queryNamaGI.LATITUDE
    lon = queryNamaGI.LONGITUDE
    ultg = queryNamaGI.ULTG
    statusOperasi = queryNamaGI.STATUS_OPERASI
    idFunctloc = queryNamaGI.ID_FUNCTLOC
    tegangan = queryNamaGI.TEGANGAN
    tglOperasi = queryNamaGI.TGL_OPRS
    alamat = queryNamaGI.ALAMAT
    back = True

    '''
    CRITICAL BAY
    =========================================
    '''
    query_nmLokasi = queryNamaGI.NM_LOKASI
    query_bay = BayModel.query.filter_by(GI=str(query_nmLokasi)).all()

    ULTG_LIST = []
    GI_LIST = []
    BAY_LIST = []
    FUNGSI_LIST = []
    ID_FUNCTLOC_LIST = []
    SUP_FUNCTLOC_LIST = []
    NM_LOKASI_LIST = []
    DESKRIPSI_LIST = []
    ID_LOCATION_LIST = []
    ID_PARENT_LIST = []
    TEGANGAN_LIST = []
    KD_FUNGSI_LIST = []
    KD_WILAYAH_LIST = []
    TGL_OPRS_LIST = []
    TGL_TDK_OPRS_LIST = []
    FLAG_LIST = []
    WORKCENTER_LIST = []
    ID_PLANT_LIST = []
    ID_TRAGI_LIST = []
    NOMORGI_LIST = []
    KD_GROUPLOKASI_LIST = []
    ID_SECTION_LIST = []
    BOUND_LIST = []
    BA_CODE_LIST = []
    ASSET_LOKASI_LIST = []
    BAYGROUP_LIST = []
    MVA_LIST = []
    NOSIRKIT_LIST = []
    COSTCENTER_LIST = []
    BC_FLC_LIST = []

    for data in query_bay:

        ULTG_LIST.append(data.ULTG)
        GI_LIST.append(data.GI)
        BAY_LIST.append(data.BAY)
        FUNGSI_LIST.append(data.FUNGSI)
        ID_FUNCTLOC_LIST.append(data.ID_FUNCTLOC)
        SUP_FUNCTLOC_LIST.append(data.SUP_FUNCTLOC)
        NM_LOKASI_LIST.append(data.NM_LOKASI)
        DESKRIPSI_LIST.append(data.DESKRIPSI)
        ID_LOCATION_LIST.append(data.ID_LOCATION)
        ID_PARENT_LIST.append(data.ID_PARENT)
        TEGANGAN_LIST.append(data.TEGANGAN)
        KD_FUNGSI_LIST.append(data.KD_FUNGSI)
        KD_WILAYAH_LIST.append(data.KD_WILAYAH)
        TGL_OPRS_LIST.append(data.TGL_OPRS)
        TGL_TDK_OPRS_LIST.append(data.TGL_TDK_OPRS)
        FLAG_LIST.append(data.FLAG)
        WORKCENTER_LIST.append(data.WORKCENTER)
        ID_PLANT_LIST.append(data.ID_PLANT)
        ID_TRAGI_LIST.append(data.ID_TRAGI)
        NOMORGI_LIST.append(data.NOMORGI)
        KD_GROUPLOKASI_LIST.append(data.KD_GROUPLOKASI)
        ID_SECTION_LIST.append(data.ID_SECTION)
        BOUND_LIST.append(data.BOUND)
        BA_CODE_LIST.append(data.BA_CODE)
        ASSET_LOKASI_LIST.append(data.ASSET_LOKASI)
        BAYGROUP_LIST.append(data.BAYGROUP)
        MVA_LIST.append(data.MVA)
        NOSIRKIT_LIST.append(data.NOSIRKIT)
        COSTCENTER_LIST.append(data.COSTCENTER)
        BC_FLC_LIST.append(data.BC_FLC)

    return render_template(
        "gi_detail.html",
        back=back,
        title=queryNamaGI.NM_LOKASI,
        namaGI=queryNamaGI.NM_LOKASI,
        lat=lat, lon=lon,
        ultg=ultg,
        statusOperasi=statusOperasi,
        idFunctloc=idFunctloc,
        tegangan=tegangan,
        tglOperasi=tglOperasi,
        alamat=alamat,

        GI_LIST=GI_LIST,
        BAY_LIST=BAY_LIST,
        FUNGSI_LIST=FUNGSI_LIST,
        ID_FUNCTLOC_LIST=ID_FUNCTLOC_LIST,
        SUP_FUNCTLOC_LIST=SUP_FUNCTLOC_LIST,
        NM_LOKASI_LIST=NM_LOKASI_LIST,
        DESKRIPSI_LIST=DESKRIPSI_LIST,
        ID_LOCATION_LIST=ID_LOCATION_LIST,
        ID_PARENT_LIST=ID_PARENT_LIST,
        TEGANGAN_LIST=TEGANGAN_LIST,
        KD_FUNGSI_LIST=KD_FUNGSI_LIST,
        KD_WILAYAH_LIST=KD_WILAYAH_LIST,
        TGL_OPRS_LIST=TGL_OPRS_LIST,
        TGL_TDK_OPRS_LIST=TGL_TDK_OPRS_LIST,
        FLAG_LIST=FLAG_LIST,
        WORKCENTER_LIST=WORKCENTER_LIST,
        ID_PLANT_LIST=ID_PLANT_LIST,
        ID_TRAGI_LIST=ID_TRAGI_LIST,
        NOMORGI_LIST=NOMORGI_LIST,
        KD_GROUPLOKASI_LIST=KD_GROUPLOKASI_LIST,
        ID_SECTION_LIST=ID_SECTION_LIST,
        BOUND_LIST=BOUND_LIST,
        BA_CODE_LIST=BA_CODE_LIST,
        ASSET_LOKASI_LIST=ASSET_LOKASI_LIST,
        BAYGROUP_LIST=BAYGROUP_LIST,
        MVA_LIST=MVA_LIST,
        NOSIRKIT_LIST=NOSIRKIT_LIST,
        COSTCENTER_LIST=COSTCENTER_LIST,
        BC_FLC_LIST=BC_FLC_LIST
    )
