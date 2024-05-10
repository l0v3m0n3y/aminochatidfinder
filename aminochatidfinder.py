import AminoLab,asyncio
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.YELLOW)
print(pyfiglet.figlet_format("aminochatidfinder", font="rectangles"))
async def main():
	client = AminoLab.AminoLab()
	email = input("Email >> ");password = input("Password >> ")
	await client.auth(email=email, password=password)
	clients = await client.my_communities()
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	ndc_Id = clients.ndc_Id[int(input("Select the community >> ")) - 1]
	print("""[1] Get Joined Chats ChatId
[2] Get Public Chats ChatId""")
	select = input("Select >> ")
	if select == "1":
	       try:
	       	joined_chats = await client.my_chat_threads(ndc_Id=ndc_Id, size=100)
	       	for title, thread_Id in zip(joined_chats.title, joined_chats.thread_Id):
	       		print(f"{title} >> {thread_Id}")
	       except Exception as e:
	       	print(e)

	elif select == "2":
	       try:
	       	public_chats = await client.get_public_chat_threads(ndc_Id=ndc_Id, size=100)
	       	for title, thread_Id in zip(public_chats.title, public_chats.thread_Id):
	       		print(f"{title} >> {thread_Id}")
	       except Exception as e:
	       	print(e)
asyncio.get_event_loop().run_until_complete(main())