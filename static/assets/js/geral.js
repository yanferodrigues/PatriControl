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
    const cards = document.querySelectorAll(".main-principal-patrimonio-card")
    const planilha = document.querySelector(".tabela-ativos")

    cards.forEach(card => {
        card.classList.toggle("ativo")
    })

    planilha.classList.toggle("ativo")
}


