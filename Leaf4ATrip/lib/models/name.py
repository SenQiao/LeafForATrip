class Name:
	def __init__(self, id: int, label: str):
		self.id = id
		self.label = label
	def get_text(self) -> str:
		return self.label;