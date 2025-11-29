import aiohttp

async def submit_answer(submit_url: str, email: str, secret: str, answer):
    """
    Sends the answer back to the quiz submit URL.
    The grader expects:
    {
        "email": "<your email>",
        "secret": "<your secret>",
        "answer": <answer>
    }
    """

    payload = {
        "email": email,
        "secret": secret,
        "answer": answer
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(submit_url, json=payload) as resp:
            try:
                data = await resp.json()
            except:
                text = await resp.text()
                return {"correct": False, "reason": f"Invalid response: {text}"}

            return data
