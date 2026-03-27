# ExpertAI Platform API Reference

ExpertAI Platform provides a standardized OpenAI-compatible API and custom management endpoints.

## Base URL
`http://localhost:8000`

## Authentication
Every request to the AI models must include an `x-api-key` header.

## Chat Completions (OpenAI Compatible)
**POST** `/v1/chat/completions`

### Header
- `x-api-key`: `sk-xxxx...`

### Request Body
```json
{
  "model": "chat-expert",
  "messages": [
    { "role": "user", "content": "Write a python script to search the web" }
  ],
  "max_tokens": 512,
  "temperature": 0.7
}
```

### Response
```json
{
  "id": "chatcmpl-1729123456",
  "object": "chat.completion",
  "created": 1729123456,
  "model": "chat-expert",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Sure, here is the code... [TOOL EXECUTION]: Searching the web for..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "completion_tokens": 50,
    "total_tokens": 50
  }
}
```

## Admin Management API

- `GET /api/admin/keys`: List all API keys.
- `POST /api/admin/keys?usage_limit=1000`: Generate a new key.
- `DELETE /api/admin/keys/{key}`: Delete an existing key.
- `GET /api/admin/logs`: List recent activity logs.
- `GET /api/admin/analytics`: Get detailed analytics data.
- `GET /api/admin/tools`: List all installed tools and plugins.
