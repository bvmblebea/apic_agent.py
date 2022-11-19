from requests import get

class ApicAgent:
	def __init__(self, user_agent: str) -> None:
		self.api = "https://api.apicagent.com"
		self.headers = {
			"user-agent": user_agent
		}
		self.user_agent = user_agent
		self.user_agent_info = get(
			f"{self.api}?ua={self.user_agent}",
			headers=self.headers).json()
		
	def get_user_agent_info(self) -> dict:
		return self.user_agent_info
	
	def get_user_agent_browser(self) -> str:
		return self.user_agent_info["browser_family"]
	
	def get_user_agent_client(self) -> str:
		return self.user_agent_info["client"]
	
	def get_user_agent_device(self) -> str:
		return self.user_agent_info["device"]
	
	def get_user_agent_os(self) -> str:
		return self.user_agent_info["os"]
