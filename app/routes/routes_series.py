from flask import Blueprint
from app.controllers import series_controller as s_c


bp_series = Blueprint("bp_series", __name__, url_prefix="/series")

# bp_series.get("")(s_c.get_all_series)
# bp_series.get("/<int:serie_id>")(s_c.get_one_serie)
bp_series.get("")(s_c.get_series)
bp_series.get("/<int:id>")(s_c.get_series)
bp_series.post("")(s_c.post_new_serie)

