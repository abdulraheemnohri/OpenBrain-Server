document.addEventListener('DOMContentLoaded', function() {
    fetchLogs();
});

async function fetchLogs() {
    const response = await fetch('/api/admin/logs?limit=50');
    const logs = await response.json();
    const body = document.getElementById('logsTableBody');
    body.innerHTML = logs.map(log => `
        <tr class="hover:bg-gray-50 transition">
            <td class="py-4 px-6 text-sm text-gray-500">${new Date(log.timestamp).toLocaleString()}</td>
            <td class="py-4 px-6 text-sm font-mono text-gray-600">${log.api_key.substring(0, 10)}...</td>
            <td class="py-4 px-6 text-sm text-gray-700 font-medium">${log.query.substring(0, 80)}...</td>
            <td class="py-4 px-6 text-sm text-gray-500">${(log.response_time || 0).toFixed(2)}s</td>
            <td class="py-4 px-6 text-sm text-gray-500">${log.tokens}</td>
            <td class="py-4 px-6 text-sm text-gray-400 font-mono">${log.ip_address}</td>
        </tr>
    `).join('');
}
