import asyncio
import random
import threading




async def main():

    async def lazy_greet(msg, deplay):
        await asyncio.sleep(deplay)
        return msg


    msgs = range(10000)
    fts = [
    asyncio.ensure_future(
        lazy_greet(m,1.99)
    )
     for m in msgs
     ]

    (done,pending) = await asyncio.wait(fts,timeout=2)
    print("NUMBER OF DONE")
    print(len(done))

    for d in done:

        d = await d

    for p in pending:
        p.cancel()




if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    loop.run_until_complete(main())

    loop.close()