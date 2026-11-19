import asyncio


async def get_http_request():
    print("GET request start")
    await asyncio.sleep(1)
    print("GET request end")
    return "return value"


async def main():
    print(f"Get: {await get_http_request()}")


if __name__ == "__main__":
    asyncio.run(main())
