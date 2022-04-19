import asyncio

async def Aman():
    await asyncio.sleep(10)
    print("Order given by Aman")

async def Kohli():
    await asyncio.sleep(5)
    print("Order given by Kohli")

async def John():
    await asyncio.sleep(1)
    print("Order given by John")

async def withAsyncio():
    order1 = asyncio.create_task(Aman())
    order2 = asyncio.create_task(Kohli())
    order3 = asyncio.create_task(John())
    print("With asyncio")
    print("Taking order")
    await order1
    await order2
    await order3
    print("Order taken")

async def withoutAsyncio():
    print("Without asyncio")
    print("Taking order")
    await Aman()
    await Kohli()
    await John()
    print("Order taken")

asyncio.run(withAsyncio())
# asyncio.run(withoutAsyncio())
