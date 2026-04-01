const graficoDB = document.getElementById("grafico-dashboard");

const chart = new Chart(graficoDB, {
    type: 'doughnut',

    data: {
        labels: [], // 🔥 agora vem do backend

        datasets: [{
            label: 'Quantidade',
            data: [], // começa vazio

            backgroundColor: [
                '#2f4cee',
                '#5fc266',
                '#e12a2a',
                '#fee924',
                '#b342ff',
                '#84f2cb',
                '#ff8c42',
                '#00c2ff',
                '#ff66b2',
                '#a3ff12'
            ],

            borderColor: [
                '#1f2f47',
                '#2d512f',
                '#562c2c',
                '#4e4421',
                '#3f2a4c',
                '#1f2f47',
                '#5a2e1f',
                '#003f5c',
                '#4c1f3a',
                '#3a4c1f'
            ],

            borderWidth: 2,
            hoverOffset: 8
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        animation: {
            duration: 1500,
            easing: 'easeInOutQuart'
        },

        cutout: "65%",

        plugins: {
            legend: {
                position: 'bottom',
                align: 'center',

                labels: {
                    usePointStyle: true,
                    pointStyle: 'circle',
                    boxWidth: 10,
                    padding: 15,
                    color: "#697082",
                }
            }
        },

        layout: {
            padding: {
                top: 20,
                bottom: 20
            }
        }
    }
});


// 🔥 FUNÇÃO QUE BUSCA DO DJANGO
function carregarGrafico() {
    fetch('api/grafico/')
        .then(response => response.json())
        .then(data => {

            console.log("Dados do Django:", data);

            // 🔥 AGORA VEM TUDO DINÂMICO
            chart.data.labels = data.labels;
            chart.data.datasets[0].data = data.valores;

            chart.update();
        })
        .catch(error => console.error("Erro ao carregar gráfico:", error));
}


// 🔥 EXECUTA AO CARREGAR A PÁGINA
document.addEventListener("DOMContentLoaded", () => {
    carregarGrafico();
});