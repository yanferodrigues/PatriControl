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
    const cards = document.querySelector(".opcao-cards");
    const planilha = document.querySelector(".opcao-tabela");

    const estaTabelaAtiva = planilha.classList.contains("ativo");

    if (estaTabelaAtiva) {
        planilha.classList.remove("ativo");

        cards.classList.add("ativo");
    } else {
        planilha.classList.add("ativo");

        cards.classList.remove("ativo");
    }
}