from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class routeConsumer(WebsocketConsumer):

	def connect(self):
		async_to_sync(self.channel_layer.group_add)('visc',self.channel_name)
		self.accept()

	def disconnect(self, close_code):
		async_to_sync(self.channel_layer.group_discard)('visc',self.channel_name)

	def receive(self, text_data):
		text_data_json = json.loads(text_data)
		async_to_sync(self.channel_layer.group_send)('visc',{
			'type':'voice_command',
			'data':text_data_json}
			)

	def voice_command(self, event):
		data = event['data']
		self.send(json.dumps(data))
