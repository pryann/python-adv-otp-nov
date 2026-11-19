import asyncio
import aiohttp


async def get_http_request(url):
    async with aiohttp.ClientSession() as session, session.get(url) as response:
        return await response.json()


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/comments/1",
    ]

    tasks = [get_http_request(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    for r in responses:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
