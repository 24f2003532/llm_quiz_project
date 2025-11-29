import aiohttp
import base64

async def load_audio(url: str):
    """
    Downloads audio file from URL and returns base64 string.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.read()
            return base64.b64encode(data).decode()
