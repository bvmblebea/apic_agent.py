from requests import get


class ApicAgent:
	def __init__(self, user_agent: str):
		self.api = "https://api.apicagent.com"
		self.headers = {
			"user-agent": user_agent
		}
		self.user_agent = user_agent
		self.user_agent_info = get(
			f"{self.api}?ua={self.user_agent}",
			headers=self.headers).json()
		
	def get_user_agent_info(self):
		return self.user_agent_info
	
	def get_user_agent_browser(self):
		return self.user_agent_info["browser_family"]
	
	def get_user_agent_client(self):
		return self.user_agent_info["client"]
	
	def get_user_agent_device(self):
		return self.user_agent_info["device"]
	
	def get_user_agent_os(self):
		return self.user_agent_info["os"]
