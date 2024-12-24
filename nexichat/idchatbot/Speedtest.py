import asyncio
import speedtest
from pyrogram import filters, Client
from pyrogram.types import Message

server_result_template = (
    "✯ Speedtest Results ✯\n\n"
    "Client:\n"
    "» ISP: {isp}\n"
    "» Country: {country}\n\n"
    "Server:\n"
    "» Name: {server_name}\n"
    "» Country: {server_country}, {server_cc}\n"
    "» Sponsor: {sponsor}\n"
    "» Latency: {latency} ms\n"
    "» Ping: {ping} ms"
)

def run_speedtest():
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        test.download()
        test.upload()
        results = test.results.dict()
        results["share"] = test.results.share() if test.results.share() else None
        return results
    except speedtest.SpeedtestException as e:
        return {"error": f"Speedtest Error: {e}"}
    except Exception as e:
        return {"error": f"Unexpected Error: {e}"}

@Client.on_message(filters.command(["speedtest", "spt"], prefixes=["."]))
async def speedtest_function(client, message: Message):
    m = await message.reply_text("Running speedtest...")
    try:
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, run_speedtest)
        
        if "error" in result:
            await m.edit_text(result["error"])
            return
        
        output = server_result_template.format(
            isp=result["client"]["isp"],
            country=result["client"]["country"],
            server_name=result["server"]["name"],
            server_country=result["server"]["country"],
            server_cc=result["server"]["cc"],
            sponsor=result["server"]["sponsor"],
            latency=result["server"]["latency"],
            ping=result["ping"],
        )

        if result["share"]:
            await message.reply_photo(photo=result["share"], caption=output)
        else:
            await message.reply_text(output)

        await m.delete()
    except Exception as e:
        await m.edit_text(f"Unexpected Error: {e}")
