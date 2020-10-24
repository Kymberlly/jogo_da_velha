let partida = 0;
let jogador1 = '';
let id_partida = '';

function jogadorAtual(jogador1){
    if(partida % 2 == 0)
        return jogador1
    return jogador1 == 'X' ? 'O' : 'X';
}

function comecaJogada(){
    partida = 0;
    $('#bt_iniciar').css('display', 'none');
    $('#tabuleiro, #menu').css('display', 'flex');
    $('#tabuleiro tr td').removeClass().css("pointer-events", "auto");

    $.ajax({
        url: '/game',
        type:'POST',
    }).done((retorno) => {
        id_partida = retorno.id;
        jogador1 = retorno.firstPlayer;

        $('.id_jogo').html(id_partida);
        $('.jogador_atual').html(jogador1);

    }).fail((retorno) => {
        alert('Falha ao iniciar partida, tente novamente!');
    });
}

function marcaJogada(jObj, player){
    partida++;
    classeQuadro = player == 'X' ? 'marcaX' : 'marcaO';
    $('.jogador_atual').html(player == 'X' ? 'O' : 'X');
    jObj.css("pointer-events", "none").addClass(classeQuadro);
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
        dataType:'json',
        type:'POST',
        headers:{'Content-Type': 'application/json'},
        data: JSON.stringify(data)
    }).done((retorno) => {
        if(retorno.msg)
            return alert(retorno.msg);

        marcaJogada(jObj, player);

        vencedor = retorno.winner;
        if(vencedor){
            if(vencedor == 'Draw')
                mensagem = 'Jogo finalizou em Empate!';
            else
                mensagem = `Jogador ${vencedor} ganhou o jogo`;

            if(confirm(`${mensagem}. Deseja iniciar uma nova partida?`))
                comecaJogada();
            else
                return
        }

    }).fail((retorno) => {
        alert('Falha ao realizar jogada, tente novamente!');
    });
}