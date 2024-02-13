import os
from dotenv import load_dotenv

class Credentials:
	def __init__(self, server, port, username, password, recipient, validated_email):
		self._server = server
		self._port = port
		self._username = username
		self._password = password
		self._recipient = recipient
		self._validated_email = validated_email
	
	@classmethod
	def from_env(cls):
		load_dotenv()
		server = "smtp.gmail.com"
		port = 587
		username = os.getenv("SMTP_USERNAME")
		password = os.getenv("SMTP_PASSWORD")
		recipient = os.getenv("SMTP_RECIPIENT")
		validated_email = os.getenv("VERIFIED_EMAIL")
		return cls(server, port, username, password, recipient, validated_email)

	def get_username(self):
		return self._username

	def get_recipient(self):
		return self._recipient

	def get_password(self):
		return self._password

	def get_server(self):
		return self._server

	def get_port(self):
		return self._port
	
	def get_port(self):
		return self._port
	
	def get_verified_email(self):
		return self._validated_email