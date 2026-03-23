const graficoDB = document.getElementById("grafico-dashboard");

const chart = new Chart(graficoDB, {
    type: 'doughnut',

    data: {
        labels: [
            'Veiculos',
            'Equipamentos diversos',
            'Maquinas',
            'Informatica e comunicação',
            'Móveis e utensílios',
            'Imóveis'
        ],

        datasets: [{
            label: 'Quantidade',
            data: [0, 0, 0, 0, 0, 0], // começa zerado

            backgroundColor: [
                '#2f4cee',
                '#5fc266',
                '#e12a2a',
                '#fee924',
                '#b342ff',
                '#84f2cb'
            ],

            borderColor: [
                '#1f2f47',
                '#2d512f',
                '#562c2c',
                '#4e4421',
                '#3f2a4c',
                '#1f2f47'
            ],

            borderWidth: 2,
            hoverOffset: 8
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        animation: {
            duration: 2000,
            easing: 'easeInOutQuart'
        },

        cutout: "65%",

        plugins: {
            legend: {
                position: 'bottom', // 👈 embaixo
                align: 'center',

                labels: {
                    usePointStyle: true, // 👈 bolinha
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

// animação real
setTimeout(() => {
    chart.data.datasets[0].data = [200, 450, 600, 900, 500, 60];
    chart.update();
}, 200);