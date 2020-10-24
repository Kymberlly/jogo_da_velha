from flask import Flask, jsonify, request, render_template
from jogo_da_velha import JogoDaVelha
aplicacao = Flask('jogo_velha', template_folder='templates')


@aplicacao.route('/')
def inicio():
    return render_template('inicio.html'), 200


@aplicacao.route('/game', methods=['POST'])
@aplicacao.route('/game/<string:id>/movement', methods=['POST'])
def game(id=None):
    if not id:
        global partida
        partida = JogoDaVelha()
        return jsonify(partida.iniciar_partida()), 200

    req = request.get_json()
    id = req.get('id', None)
    player = req.get('player', None)
    position = req.get('position', {})
    return jsonify(partida.realiza_jogada(id, player, position)), 200


if __name__ == '__main__':
    aplicacao.debug = True
    aplicacao.run(host="0.0.0.0")