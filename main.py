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

    requests = request.json if request.json else request.form

    id = requests.get('id', None)
    player = requests.get('player', None)
    posX = int(requests.get('position[x]', None))
    posY = int(requests.get('position[y]', None))

    return jsonify(partida.realiza_jogada(id, player, posX, posY)), 200


if __name__ == '__main__':
    aplicacao.debug = True
    aplicacao.run(host="0.0.0.0")