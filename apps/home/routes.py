from flask import Blueprint, render_template
from apps.home.models import GIModel, BayModel, PMTModel, PMSModel, CTModel
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
    id_gi = queryNamaGI.id
    back = True
    '''
    CRITICAL BAY
    =========================================
    '''
    query_nmLokasi = queryNamaGI.NM_LOKASI
    query_bay = BayModel.query.filter_by(GI=str(query_nmLokasi)).all()

    # print("")
    # print("PMT LIST : ", PMT_LIST, " jumlah : ", len(PMT_LIST))
    BAY_LIST = []
    ID_LIST = []

    for data in query_bay:
        ID_LIST.append(data.ID_FUNCTLOC)
        BAY_LIST.append(data.BAY)

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
        BAY_LIST=BAY_LIST,
        ID_LIST=ID_LIST,
        ID_GI=id_gi
        # PMT_LIST=PMT_LIST
    )


@home.route("/<int:id_gi>/peralatan/<string:ID_FUNCTLOC>")
def pmtList(id_gi, ID_FUNCTLOC):
    PMT_LIST = []
    query_pmt = PMTModel.query.filter_by(
        ID_FUNCTLOC=ID_FUNCTLOC).all()
    
    query_pms = PMSModel.query.filter_by(ID_FUNCTLOC=ID_FUNCTLOC).all()
    query_ct = CTModel.query.filter_by(ID_FUNCTLOC=ID_FUNCTLOC).all()
    bayGI = BayModel.query.filter_by(ID_FUNCTLOC=ID_FUNCTLOC).first()

    queryNamaGI = GIModel.query.get(id_gi)
    lat = queryNamaGI.LATITUDE
    lon = queryNamaGI.LONGITUDE
    namaGI = queryNamaGI.NM_LOKASI
    return render_template(
        "peralatan.html",
        ID_GI=id_gi,
        back=True,
        PMT=query_pmt,
        PMS=query_pms,
        CT=query_ct,
        bayGI=bayGI,
        lat=lat, lon=lon,
        namaGI=namaGI
    )
