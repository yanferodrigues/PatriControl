const overlay = document.querySelector(".overlay");
const aside = document.getElementById("aside");

function abrirMenu(btn) {
    overlay.classList.toggle("ativo");
    aside.classList.toggle("ativo");
}

function irPara(pagina) {
    window.location.href = `${pagina}`;
}

function alterarVisualizacao() {
    const cards = document.querySelector(".opcao-cards");
    const planilha = document.querySelector(".opcao-tabela");
    if (!cards || !planilha) return;

    const estaTabelaAtiva = planilha.classList.contains("ativo");

    if (estaTabelaAtiva) {
        planilha.classList.remove("ativo");
        cards.classList.add("ativo");
        document.body.classList.remove("modo-tabela");
    } else {
        planilha.classList.add("ativo");
        cards.classList.remove("ativo");
        document.body.classList.add("modo-tabela");
    }
}

const tabela = document.querySelector(".opcao-tabela");
const cards = document.querySelector(".opcao-cards");
const botaoTrocar = document.querySelector(".botao-trocar-planilha");

function controlarTabela() {
    if (!tabela || !cards || !botaoTrocar) return;
    botaoTrocar.style.display = "flex";
}

window.addEventListener("resize", controlarTabela);
window.addEventListener("load", controlarTabela);

// Filtros por coluna — estilo Excel
function filtrarTabela() {
    const filtros = document.querySelectorAll(".filtro-coluna");
    const tbody = document.querySelector(".tabela-ativos tbody");
    if (!tbody) return;

    const valores = [...filtros].map(input => ({
        col: parseInt(input.dataset.col),
        texto: input.value.toLowerCase().trim()
    }));

    tbody.querySelectorAll("tr").forEach(row => {
        const celulas = row.querySelectorAll("td");
        const visivel = valores.every(({ col, texto }) => {
            if (!texto) return true;
            const celula = celulas[col];
            return celula && celula.textContent.toLowerCase().includes(texto);
        });
        row.classList.toggle("filtrado", !visivel);
    });
}

document.querySelectorAll(".filtro-coluna").forEach(input => {
    input.addEventListener("input", filtrarTabela);
    // Impede que clique no input acione o click da linha
    input.addEventListener("click", e => e.stopPropagation());
    // Impede Enter de submeter form
    input.addEventListener("keydown", e => { if (e.key === "Enter") e.preventDefault(); });
});

// Accordion nav grupos
document.querySelectorAll(".nav-grupo").forEach(grupo => {
    if (grupo.querySelector(".link-ativo")) {
        grupo.classList.add("aberto");
    }
});

document.querySelectorAll(".nav-grupo-cabeca").forEach(cabeca => {
    cabeca.addEventListener("click", () => {
        cabeca.closest(".nav-grupo").classList.toggle("aberto");
    });
});

// Fecha menu lateral com Escape
document.addEventListener("keydown", e => {
    if (e.key === "Escape") {
        overlay.classList.remove("ativo");
        aside.classList.remove("ativo");
    }
});

// Auto-submit dos filtros de pesquisa ao mudar select
document.querySelectorAll(".main-pesquisa-patrimonio select").forEach(select => {
    select.addEventListener("change", () => {
        const form = select.closest("form");
        if (form) form.submit();
    });
});
