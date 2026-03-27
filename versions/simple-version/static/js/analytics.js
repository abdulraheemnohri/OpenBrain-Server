document.addEventListener('DOMContentLoaded', function() {
    fetchAnalytics();
});

async function fetchAnalytics() {
    const response = await fetch('/api/admin/analytics');
    const data = await response.json();

    // Requests Chart
    const reqCtx = document.getElementById('requestsChart').getContext('2d');
    new Chart(reqCtx, {
        type: 'bar',
        data: {
            labels: data.daily.map(m => m.date).reverse(),
            datasets: [{
                label: 'Total Requests',
                data: data.daily.map(m => m.total_requests).reverse(),
                backgroundColor: 'rgba(54, 162, 235, 0.7)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: { responsive: true }
    });

    // Tokens Chart
    const tokenCtx = document.getElementById('tokensChart').getContext('2d');
    new Chart(tokenCtx, {
        type: 'line',
        data: {
            labels: data.daily.map(m => m.date).reverse(),
            datasets: [{
                label: 'Tokens Consumed',
                data: data.daily.map(m => m.total_tokens).reverse(),
                borderColor: 'rgba(255, 99, 132, 1)',
                fill: false,
                tension: 0.1
            }]
        },
        options: { responsive: true }
    });

    // Latency Chart
    const latencyCtx = document.getElementById('latencyChart').getContext('2d');
    new Chart(latencyCtx, {
        type: 'line',
        data: {
            labels: data.daily.map(m => m.date).reverse(),
            datasets: [{
                label: 'Average Latency (ms)',
                data: data.daily.map(m => (m.avg_response_time * 1000).toFixed(0)).reverse(),
                borderColor: 'rgba(153, 102, 255, 1)',
                fill: true,
                backgroundColor: 'rgba(153, 102, 255, 0.1)',
                tension: 0.3
            }]
        },
        options: { responsive: true }
    });
}
