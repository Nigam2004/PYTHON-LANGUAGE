import asyncio
#async helps Python handle multiple tasks efficiently when they spend time waiting for network, database, or other I/O operations.
async def get_data():
      return "data recieved"

async def main():
    result=await get_data()
    print(result) 
asyncio.run(main())

