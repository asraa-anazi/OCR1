const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['12/12', '13/12', '14/12', '15/12', '16/12', '17/12', '18/12'],
        datasets: [{
            label: 'Glucose Levels mmol/L',
            data: [4.2, 8.3, 6.1, 5.1, 5.3, 8.7, 10.4],
            backgroundColor: [
                'rgba(97, 205, 133, 1)',
                'rgba(255, 114, 5, 1)',
                'rgba(97, 205, 133, 1)',
                'rgba(97, 205, 133, 1)',
                'rgba(97, 205, 133, 1)',
                'rgba(255, 114, 5, 1)',
                'rgba(230, 39, 39, 1)'
            ],
            borderColor: [
                'rgba(97, 205, 133, 1)',
                'rgba(255, 114, 5, 1)',
                'rgba(97, 205, 133, 1)',
                'rgba(97, 205, 133, 1)',
                'rgba(97, 205, 133, 1)',
                'rgba(255, 114, 5, 1)',
                'rgba(230, 39, 39, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});