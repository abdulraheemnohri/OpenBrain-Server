document.addEventListener('DOMContentLoaded', function() {
    // Logic for loading and saving settings
    console.log("Settings page loaded.");
    loadSettings();
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

async function loadSettings() {
    try {
        const response = await fetch("/api/admin/settings");
        const data = await response.json();
        if (data.rate_limit) document.querySelector("input[type=\"number\"]").value = data.rate_limit;
        if (data.token_limit) document.querySelectorAll("input[type=\"number\"]")[1].value = data.token_limit;
    } catch (e) {
        console.error("Failed to load settings:", e);
    }
}

async function saveSettings() {
    const rateLimit = document.querySelector('input[type="number"]').value;
    const tokenLimit = document.querySelectorAll('input[type="number"]')[1].value;

    try {
        await fetch("/api/admin/settings", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ rate_limit: rateLimit, token_limit: tokenLimit })
        });
        alert("Settings saved successfully!");
    } catch (e) {
        alert("Failed to save settings.");
    }
}

// Bind save button
const saveBtn = document.querySelector('button');
if (saveBtn) {
    saveBtn.addEventListener('click', saveSettings);
}
