const overlay = document.querySelector(".overlay")
const aside = document.getElementById("aside")

function abrirMenu(btn) {
    overlay.classList.toggle("ativo")
    aside.classList.toggle("ativo")
}

function alterarTema() {
    document.body.classList.toggle("light-mode")
}

function irPara(pagina) {
    window.location.href = `${pagina}`;
}

function alterarVisualizacao() {
    const cards = document.querySelectorAll(".main-principal-patrimonio-card-geral");
    const planilha = document.querySelector(".tabela-ativos");

    const estaTabelaAtiva = planilha.classList.contains("ativo");

    if (estaTabelaAtiva) {
        // VOLTA PRA CARD
        planilha.classList.remove("ativo");

        cards.forEach(card => {
            card.classList.add("ativo");
        });
    } else {
        // VAI PRA TABELA
        planilha.classList.add("ativo");

        cards.forEach(card => {
            card.classList.remove("ativo");
        });
    }
}