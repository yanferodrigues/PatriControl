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

const tabela = document.querySelector(".opcao-tabela");
const cards = document.querySelector(".opcao-cards");
const botaoTrocar = document.querySelector(".botao-trocar-planilha")

function controlarTabela() {
    if (window.innerWidth <= 1000) {
        tabela.classList.remove("ativo");
        cards.classList.add("ativo");
        botaoTrocar.style.display = "none"
    } else {
        botaoTrocar.style.display = "flex"
    }
}

window.addEventListener("resize", controlarTabela);
window.addEventListener("load", controlarTabela);