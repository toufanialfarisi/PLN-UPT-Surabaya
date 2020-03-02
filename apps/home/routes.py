from flask import Blueprint, render_template
from apps.home.models import GIModel
import json

home = Blueprint("home", __name__, template_folder="templates/", static_folder='static/')


@home.route("/")
def index():
    lon = []
    lat = []
    gi = []
    url = []
    query = GIModel.query.all()
    for data in query:
        out_url = data.NM_LOKASI_URL
        out_lon = data.LONGITUDE
        out_lon = float(out_lon)
        out_lat = data.LATITUDE
        out_lat = float(out_lat)
        out_gi = data.NM_LOKASI
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
        idx=url
    )

@home.route("/<string:url>")
def gi_detail(url):
    queryNamaGI = GIModel.query.filter_by(NM_LOKASI_URL=url).first()
    lat = queryNamaGI.LATITUDE
    lon = queryNamaGI.LONGITUDE
    ultg = queryNamaGI.ULTG
    statusOperasi = queryNamaGI.STATUS_OPERASI
    idFunctloc = queryNamaGI.ID_FUNCTLOC
    tegangan = queryNamaGI.TEGANGAN
    tglOperasi = queryNamaGI.TGL_OPRS
    alamat = queryNamaGI.ALAMAT
    back=True
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
        alamat=alamat
    )