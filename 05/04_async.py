import asyncio
from time import perf_counter


async def get_request():
    await asyncio.sleep(3)
    return "json data"


async def main():
    await asyncio.gather(*[get_request() for _ in range(100)])


if __name__ == "__main__":
    start = perf_counter()
    print("start main")
    asyncio.run(main())
    print("end main")
    end = perf_counter()
    print(end - start)
