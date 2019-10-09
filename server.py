#!/usr/bin/env python

# WS server example

import asyncio
import websockets

filesToSend = []
updateFileName = "updatedMeshes.txt"
sendBytes = open("meshes/testMesh2.stl", "rb").read()
configFile = open(updateFileName)

def listToString(myList):
    s = ""
    for item in myList:
        s = s + item + ", "
    return s

def toUniqueSet(myList):
    returnList = []
    for item in myList:
        if item not in returnList:
            returnList.append(item)
    return returnList


def checkUpdateFile():
    filesToSend.clear()
    updateFile = open(updateFileName)
    for line in updateFile:
        print("opening " + line)
        filesToSend.append(line)        
    toUniqueSet(filesToSend)
    print("files to send: " + listToString(filesToSend))
    if len(filesToSend) > 0:
        return True
    print("no update files found")
    return False
    
    


async def fileSend(websocket, path):   
    checkUpdateFile()
    
    for file in filesToSend:
        sendBytes = open("meshes/" + file + ".stl", "rb").read()
        await websocket.send(sendBytes)
        print(file + ".stl sent!")
    open(updateFileName, 'w').close()
    
start_server = websockets.serve(fileSend, '192.168.0.112', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
