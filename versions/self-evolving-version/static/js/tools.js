document.addEventListener('DOMContentLoaded', function() {
    fetchTools();
});

async function fetchTools() {
    const response = await fetch('/api/admin/tools');
    const tools = await response.json();
    const container = document.getElementById('toolsList');
    container.innerHTML = tools.map(tool => `
        <div class="bg-white p-8 rounded-2xl shadow-xl border border-gray-100 transition hover:shadow-2xl">
            <h4 class="font-bold text-gray-800 text-xl mb-3">${tool.name}</h4>
            <p class="text-gray-600 text-sm mb-6">${tool.description}</p>
            <div class="flex items-center justify-between">
                <span class="px-3 py-1 bg-green-100 text-green-800 text-xs font-bold rounded-full uppercase">Enabled</span>
                <button class="text-blue-600 text-xs font-bold hover:underline">Configure</button>
            </div>
        </div>
    `).join('');
}
