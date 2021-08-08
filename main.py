import asyncio
from logic.services.observer import Observer


async def main():
    observer = Observer()
    await observer.start()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
