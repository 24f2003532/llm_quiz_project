import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin

async def solve(req):
    quiz_url = req.url

    # 1. Fetch HTML
    async with aiohttp.ClientSession() as session:
        async with session.get(quiz_url) as resp:
            html = await resp.text()

    # 2. Detect “cutoff” quiz (demo-audio)
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text().lower()

    if "cutoff" in text:
        # EmailNumber logic (JS)
        answer = sum(ord(c) for c in req.email)

        # Submit
        submit_url = urljoin(quiz_url, "/submit")
        payload = {
            "email": req.email,
            "secret": req.secret,
            "url": quiz_url,
            "answer": answer
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(submit_url, json=payload) as resp:
                try:
                    return await resp.json()
                except:
                    return {
                        "correct": False,
                        "reason": await resp.text()
                    }

    # Other quiz types (NOT required for demo)
    return {"correct": False, "reason": "Unsupported quiz type"}
