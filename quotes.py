import httpx

async def get_quote():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.quotable.io/random")
        data = response.json()
        return {
            "quote": data["content"],
            "author": data["author"]
        }