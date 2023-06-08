# to day i will create chat boot like chat GPT using python && api
# fast need modul i am use my modul mahdix
import os
try:
    import mahdix as m
except:
    os.system('pip install mahdix')
# we neeed a logo for this chat boot
print(m.my_color+m.makelogo(text='GPT'))
while True:
    # input txt user 
    txt = input(f'{m.LI_GREEN}INPUT TeXT:{m.LI_YELLOW}')
    # need api for request
    api =f'https://teampeaky.xyz/gpt.php?Text={txt}'
    req =m.rqg(api).json()
    print(m.linex())
    out =req["result"]
    randomcoloure = m.rc(m.mycolor)
    print(f'{randomcoloure}GPT :{out}')
    print(m.linex())
# NOW SOME COUSTOMAIze
# NOW WE CREATE A  LOP FO EVER
