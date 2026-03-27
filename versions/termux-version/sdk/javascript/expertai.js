class ExpertAI {
    constructor({ apiKey, baseUrl = "http://localhost:8000" }) {
        this.apiKey = apiKey;
        this.baseUrl = baseUrl;
    }

    async chat(content, model = "qwen-3.5-27b", options = {}) {
        const url = `${this.baseUrl}/v1/chat/completions`;
        const body = {
            model,
            messages: [{ role: "user", content }],
            ...options
        };

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-api-key': this.apiKey
            },
            body: JSON.stringify(body)
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const data = await response.json();
        return data.choices[0].message.content;
    }

    async listModels() {
        const url = `${this.baseUrl}/v1/models`;
        const response = await fetch(url, {
            headers: { 'x-api-key': this.apiKey }
        });
        const data = await response.json();
        return data.data;
    }
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = ExpertAI;
}
