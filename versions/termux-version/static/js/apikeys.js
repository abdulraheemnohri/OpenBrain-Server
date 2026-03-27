document.addEventListener('DOMContentLoaded', function() {
    fetchKeys();
});

async function fetchKeys() {
    const response = await fetch('/api/admin/keys');
    const keys = await response.json();
    const body = document.getElementById('apiKeysBody');
    body.innerHTML = keys.map(key => `
        <tr class="hover:bg-gray-50 transition">
            <td class="py-4 px-6 text-sm font-mono text-gray-600">${key.key}</td>
            <td class="py-4 px-6">
                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${key.status === 'active' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}">
                    ${key.status}
                </span>
            </td>
            <td class="py-4 px-6 text-sm text-gray-500">${key.usage_limit || 'Unlimited'}</td>
            <td class="py-4 px-6 text-sm text-gray-500">${key.usage_count}</td>
            <td class="py-4 px-6 text-sm text-gray-500">${new Date(key.created_at).toLocaleDateString()}</td>
            <td class="py-4 px-6 text-sm">
                <button onclick="deleteKey('${key.key}')" class="text-red-600 hover:text-red-900 font-semibold">Delete</button>
            </td>
        </tr>
    `).join('');
}

async function generateNewKey() {
    const limit = prompt("Enter usage limit (default 1000):", "1000");
    const response = await fetch(`/api/admin/keys?usage_limit=${limit}`, { method: 'POST' });
    const data = await response.json();
    alert(`New Key Generated: ${data.key}`);
    fetchKeys();
}

async function deleteKey(key) {
    if (confirm(`Are you sure you want to delete ${key}?`)) {
        await fetch(`/api/admin/keys/${key}`, { method: 'DELETE' });
        fetchKeys();
    }
}
