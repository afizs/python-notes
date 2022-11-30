import asyncio

async def function_1():
	for i in range(100000):
		if i % 50000 == 0:
			print('Hello from function_1\n')
			
			# Pause the execution 
			await asyncio.sleep(0.02)
	return 0

async def function_2():
	print(">>> I am from function_2 \n")
	return 0

async def main():
	f1 = loop.create_task(function_1())
	f2 = loop.create_task(function_2())
	await asyncio.wait([f1, f2])



loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
