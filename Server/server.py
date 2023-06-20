import asyncio
import websockets
async def response(websocket, path):
	message = await websocket.recv()
	print(f"We got the message from the client: {message}")
	await websocket.send(f"I can confirm I got your message!, your message was: {message}")
start_server = websockets.serve(response, 'localhost', 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
