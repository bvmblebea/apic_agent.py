# apic_agent.py
Web-API for [apicagent.com](https://www.apicagent.com) website to detect browser, OS, device from user agent string

## Example
```python
import apic_agent
apic_agent = apic_agent.ApicAgent(user_agent="")
user_agent_info = apic_agent.get_user_agent_info()
print(user_agent_info)
```
