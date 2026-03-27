# API Reference

OpenBrain Server supports OpenAI-compatible API endpoints for easy integration.

## Chat Completions
**POST** `/v1/chat/completions`

### Header
- `x-api-key`: `sk-xxxx...`

### Request Body
```json
{
  "model": "qwen-3.5-27b",
  "messages": [
    { "role": "user", "content": "Hello!" }
  ],
  "max_tokens": 512,
  "temperature": 0.7
}
```

### Response
Standard OpenAI-compatible chat completion JSON.

## Admin API
Used by the dashboard for internal management.

- `GET /api/admin/keys`: List all API keys.
- `POST /api/admin/keys?usage_limit=1000`: Generate a new key.
- `DELETE /api/admin/keys/{key}`: Delete an existing key.
- `GET /api/admin/logs`: List recent activity logs.
- `GET /api/admin/analytics`: Get detailed analytics data.
