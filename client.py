import asyncio
import websockets

ipAddress = "192.168.0.100"
port = "8765"

receiveFile = open("file.stl", "wb")
configFile = open("configFile.txt", "w")

async def hello():
    uri = "ws://" + ipAddress + ":" + port
    async with websockets.connect(uri) as websocket:
        input("Press enter to start:")        
        print("requesting file...")
        
        file = await websocket.recv()
        
        print("printed successfully!")
        receiveFile.write(file)
        print("wrote to file!")
        receiveFile.close()

asyncio.get_event_loop().run_until_complete(hello())
 
