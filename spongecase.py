def spongecase(str:str)->str:
    """spongecase(str:str)->str:
Makes even letters lowercase and odd letters uppercase.
Usage example:
>>>spongecase("Hello world!")
HeLlO WoRlD!"""
    return ''.join([(s.upper(),s.lower())[i%2]for i,s in enumerate(str)])

if __name__ == '__main__':
    while True:
        print(spongecase(input("Enter text to make it spongecase or press Ctrl+C to exit: ")))
