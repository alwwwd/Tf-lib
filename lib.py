import asyncio, requests
from json_print import json_print 
version = "2.0 BUILD"
print(f"TF_lib\nверсия: {version}\nНачинаю работу!")

async def update_status(mes,code_and_status):
    while True:
        for key in code_and_status.keys():
                status = 0
                code = code_and_status[key]["code"]
                await asyncio.sleep(0.1)
                response = requests.get(f"https://testflight.apple.com/join/{code}",headers={"accept-language":"en-GB,en;q=0.9"})
                html = response.text
                # Получаем содержимое атрибута conten
                appname = code_and_status[key]["name"]
                # and "В настоящее время для работы с этой бета-версией новые тестировщики не принимаются." not in html "Штат" not in html and
                if "full" not in html and "close" not in html :
                    status = 1
                    if status == 1:
                        if status != code_and_status[key]["status"]:
                            code_and_status[key]["status"] = status 
                            await asyncio.sleep(0)
                            await mes.answer(f"🇷🇺https://testflight.apple.com/join/{code} {appname} открыт!\n\n\n🇬🇧https://testflight.apple.com/join/{code} {appname} is open!")
                            await asyncio.sleep(0.1)
                else:
                    status = 2
                    await asyncio.sleep(0.1)
                    code_and_status[key]["status"] = 2
                    await asyncio.sleep(0.1)