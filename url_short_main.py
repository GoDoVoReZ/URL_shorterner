import pyshorteners
from url_db import *
import tqdm
import time

def main():

    s = pyshorteners.Shortener()

    db_create()

    url  = str(input('Enter your url here: '))

    def short_url():
        shorted_url = s.chilpit.short(url)

        for i in tqdm(range(5)):
            time.sleep(1//3)


        return shorted_url

    def show_urls():
        print(f'Default URL: {url} \n')
        print(f'Shorted URL: {short_url()}')

    show_urls()
    insert_urls(url, short_url())
    
            

if __name__ == '__main__':
    main()