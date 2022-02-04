from xml.dom import NotFoundErr
from flask import jsonify, request
from http import HTTPStatus

from itsdangerous import json
from app.models.series_model import Series


# def get_all_series() -> tuple:
#     all_series = Series.get_serie_data()
#     all_series_serialized = Series.serialize_series(all_series)

#     return jsonify(all_series_serialized), HTTPStatus.OK


# def get_one_serie(id: int) -> tuple:
#     print(id)
#     one_serie = Series.get_serie_data(id)
#     onde_serie_serialized = Series.serialize_series(one_serie)

#     return jsonify(onde_serie_serialized), HTTPStatus.OK


def get_series(id: int = None) -> tuple:
    try:
        series = Series.get_serie_data(id)
        if series is None:
            raise NotFoundErr

        series_serialized = Series.serialize_series(series)


        return {"data": series_serialized}, HTTPStatus.OK
    
    except NotFoundErr:
        return {"error": "Not found serie with this request's id"}, HTTPStatus.NOT_FOUND



def post_new_serie():

    data = request.get_json()
    try:
        serie = Series(**data)
        print(serie)
        add_serie = serie.create_series()
        print(add_serie)
        add_serie = Series.serialize_series(add_serie)
        print(add_serie)


        return jsonify(add_serie), HTTPStatus.CREATED

    except KeyError as ke:
        return {"error": f"Wrong key on request -> {str(ke)}"}, HTTPStatus.BAD_REQUEST

