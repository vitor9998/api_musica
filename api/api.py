from flask import Blueprint, Response, request, jsonify
from service import Musicas


Lista = Blueprint(
    "artista", __name__, url_prefix="/v1/musicas"
)

@Lista.route("/artista", methods=["GET"])
def artista():
    service = Musicas()
    #dados = request.json
    resultado = service.lista_de_musicas(33)
    return jsonify(resultado),200

