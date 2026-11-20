import asyncio
from time import perf_counter


async def get_request():
    await asyncio.sleep(3)
    return "GET"


async def post_request():
    await asyncio.sleep(1)
    return "POST"


async def main():
    get = asyncio.create_task(get_request())
    post = asyncio.create_task(post_request())
    # await get
    # await post
    await get, post
    print(f"Get: {get.result()}, post: {post.result()}")


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    end = perf_counter()
    print(end - start)
