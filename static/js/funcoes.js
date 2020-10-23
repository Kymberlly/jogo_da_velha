let partida = 0;
let jogador1 = '';
let id_partida = '';

function jogadorAtual(jogador1){
    if(partida % 2 == 0)
        return jogador1
    return jogador1 == 'X' ? 'O' : 'X';
}

function comecaJogada(){
//    $('#bt_iniciar').css('display', 'none');
    $('#tabuleiro, #menu').css('display', 'block');

    $.ajax({
        url: '/game',
        type:'POST',
    }).done((retorno) => {
        id_partida = retorno.id;
        jogador1 = retorno.firstPlayer;

        $('.id_jogo').html(id_partida);
        $('.jogador_atual').html(jogador1);
    });
}

function realizaJogada(obj){
    const jObj = $(obj);
    const player = jogadorAtual(jogador1);

    data = {
        'id': id_partida,
        'player': player,
        'position': {'x': jObj.attr('x'), 'y': jObj.attr('y')}
    }

    $.ajax({
        url: `/game/${id_partida}/movement`,
        data: data,
        dataType:'json',
        type:'POST',
    }).done((retorno) => {
        partida++;
        classeQuadro = player == 'X' ? 'marcaX' : 'marcaO';
        $('.jogador_atual').html(player == 'X' ? 'O' : 'X');
        jObj.prop('onclick', null).addClass(classeQuadro);

        vencedor = retorno.winner;
        if(vencedor){
            if(vencedor == 'Draw'){
                alert('Jogo finalizou em Empate!');
            }
            else{
                alert(`Jogador vencedor: ${retorno.winner}`);
            }
        }

    });
}