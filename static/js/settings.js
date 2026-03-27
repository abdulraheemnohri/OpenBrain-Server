document.addEventListener('DOMContentLoaded', function() {
    // Logic for loading and saving settings
    console.log("Settings page loaded.");
    fetchTools();
});

async function fetchTools() {
    const response = await fetch('/api/admin/tools');
    const tools = await response.json();
    const container = document.getElementById('toolsList');
    container.innerHTML = tools.map(tool => `
        <div class="bg-blue-50 border border-blue-200 p-6 rounded-xl shadow-sm hover:shadow-md transition">
            <h4 class="font-bold text-blue-800 text-lg mb-2">${tool.name}</h4>
            <p class="text-blue-600 text-sm">${tool.description}</p>
            <div class="mt-4 flex items-center">
                <span class="w-3 h-3 bg-green-500 rounded-full mr-2"></span>
                <span class="text-xs font-bold text-green-700 uppercase tracking-widest">Active</span>
            </div>
        </div>
    `).join('');
}

async function saveSettings() {
    const rateLimit = document.querySelector('input[type="number"]').value;
    const tokenLimit = document.querySelectorAll('input[type="number"]')[1].value;

    // In a real system, we'd persist this in the DB.
    alert(`Settings saved locally: Rate Limit = ${rateLimit}, Token Limit = ${tokenLimit}`);

    // Example: fetch('/api/admin/settings', { method: 'POST', body: ... })
}

// Bind save button
const saveBtn = document.querySelector('button');
if (saveBtn) {
    saveBtn.addEventListener('click', saveSettings);
}
