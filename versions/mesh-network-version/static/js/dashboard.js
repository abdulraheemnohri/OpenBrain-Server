document.addEventListener('DOMContentLoaded', function() {
    fetchAnalytics();
    fetchLogs();
    fetchKeys();
});

async function fetchAnalytics() {
    const response = await fetch('/api/admin/analytics');
    const data = await response.json();

    document.getElementById('totalRequests').innerText = data.total.total_requests || 0;
    document.getElementById('totalTokens').innerText = data.total.total_tokens || 0;
    document.getElementById('avgResponseTime').innerText = (data.total.avg_response_time || 0).toFixed(2) + 's';

    // Traffic Chart
    const ctx = document.getElementById('trafficChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.daily.map(m => m.date).reverse(),
            datasets: [{
                label: 'Requests',
                data: data.daily.map(m => m.total_requests).reverse(),
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        }
    });
}

async function fetchLogs() {
    const response = await fetch('/api/admin/logs?limit=5');
    const logs = await response.json();
    const body = document.getElementById('logsBody');
    body.innerHTML = logs.map(log => `
        <tr class="border-b">
            <td class="py-2 text-sm">${new Date(log.timestamp).toLocaleString()}</td>
            <td class="py-2 text-sm">${log.api_key.substring(0, 10)}...</td>
            <td class="py-2 text-sm">${log.query.substring(0, 50)}...</td>
        </tr>
    `).join('');
}

async function fetchKeys() {
    const response = await fetch('/api/admin/keys');
    const keys = await response.json();
    document.getElementById('activeKeys').innerText = keys.filter(k => k.status === 'active').length;
}
