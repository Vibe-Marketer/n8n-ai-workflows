# 🧑‍💻 Contribution Guidelines  
*"Build with precision."* — **Sayed Allam**  

## 🔧 Workflow Standards  
### 1.1 Structure  
- **Single Responsibility Principle**: Each workflow solves exactly one problem  
- **Documentation**: Embed in JSON `notes` field:  
  ```json  
  "notes": "## Usage\n1. Set {{ $secrets.API_KEY }}\n2. Configure trigger interval"  
1.2 Submission Process
bash
# 1. Create feature branch  
git checkout -b feat/[ai-service]-[function]  

# 2. Add workflow to category folder  
/llm-chat/agent-handoff.json  

# 3. Verify functionality  
n8n execute --file your_workflow.json  
1.3 Code Review Checklist
✅ Test Coverage: Works with n8n v1.32+
✅ Error Handling: Graceful API failure modes
✅ Performance: No unnecessary API calls

🔝 Back to Top
