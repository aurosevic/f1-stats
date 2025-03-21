fetch('data/2025/starting-grid/1-Australia.csv')
    .then(response => response.text())
    .then(data => {
        const rows = data.split('\n').slice(1);
        const drivers = rows.map(row => row.split(',')[2]);
        const times = rows.map(row => row.split(',')[4]);

        const formattedTimes = times.map(time => {
            if (!time) return null;
            const [minutes, seconds, milliseconds] = time.split(/[:.]/);
            return parseInt(minutes) * 60 + parseInt(seconds) + parseInt(milliseconds) / 1000;
        }).filter(time => time !== null);

        const ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: drivers,
                datasets: [{
                    label: 'Time',
                    data: formattedTimes,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: false,
                        ticks: {
                            callback: function (value) {
                                const minutes = Math.floor(value / 60);
                                const seconds = Math.floor(value % 60);
                                const milliseconds = Math.floor((value % 1) * 1000);
                                return `${minutes}:${seconds}.${milliseconds}`;
                            }
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                const value = context.raw;
                                const minutes = Math.floor(value / 60);
                                const seconds = Math.floor(value % 60);
                                const milliseconds = Math.floor((value % 1) * 1000);
                                return `${minutes}:${seconds}.${milliseconds}`;
                            }
                        }
                    }
                },
                interaction: {
                    mode: 'index',
                    intersect: false
                }
            }
        });
    });

fetch('data/2025/race-result/1-Australia.csv')
    .then(response => response.text())
    .then(data => {
        const rows = data.split('\n').slice(1);
        const cars = rows.map(row => row.split(',')[3]);
        const points = rows.map(row => row.split(',')[6]);

        const groupedData = rows.reduce((acc, row) => {
            const [position, driverNumber, driver, car, laps, timeRetired, points] = row.split(',');
            if (!car) return acc; // Skip rows with undefined car values
            if (!acc[car]) {
                acc[car] = 0;
            }
            acc[car] += parseInt(points);
            return acc;
        }, {});

        const sortedData = Object.entries(groupedData).sort((a, b) => b[1] - a[1]);
        const carLabels = sortedData.map(entry => entry[0]);
        const carPoints = sortedData.map(entry => entry[1]);

        const ctx2 = document.getElementById('myChart2').getContext('2d');
        new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: carLabels,
                datasets: [{
                    label: 'Points',
                    data: carPoints,
                    backgroundColor: 'rgba(153, 102, 255, 0.2)',
                    borderColor: 'rgba(153, 102, 255, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                return context.raw;
                            }
                        }
                    }
                },
                interaction: {
                    mode: 'index',
                    intersect: false
                }
            }
        });
    });

fetch('data/2025/race-result/1-Australia.csv')
    .then(response => response.text())
    .then(data => {
        const rows = data.split('\n').slice(1);
        const drivers = rows.map(row => row.split(',')[2]);
        const points = rows.map(row => row.split(',')[6]);

        const ctx3 = document.getElementById('myChart3').getContext('2d');
        new Chart(ctx3, {
            type: 'bar',
            data: {
                labels: drivers,
                datasets: [{
                    label: 'Points',
                    data: points,
                    backgroundColor: 'rgba(255, 159, 64, 0.2)',
                    borderColor: 'rgba(255, 159, 64, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                return context.raw;
                            }
                        }
                    }
                },
                interaction: {
                    mode: 'index',
                    intersect: false
                }
            }
        });
    });