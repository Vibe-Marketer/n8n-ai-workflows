# 📥 How to Import Workflows

This guide covers all methods for importing workflows into your n8n instance.

## Prerequisites
- n8n instance running (v1.0+)
- API access if using remote import
- Required credentials for any integrated services

---

## Method 1: Direct JSON Import
### Via n8n UI
1. Navigate to **Workflows** → **New** → **Import**
2. Click `Upload JSON File` or paste JSON directly
3. Review and adjust any credential mappings
4. Click **Import Workflow**

```bash
# Example using curl (for n8n API)
curl -X POST \
  -H "Content-Type: application/json" \
  -H "X-N8N-API-KEY: your_api_key" \
  -d @workflow.json \
  http://your-n8n-server.com/api/v1/workflows
