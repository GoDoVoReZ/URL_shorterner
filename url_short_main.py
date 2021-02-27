import pyshorteners
from url_db import *
from tqdm import trange
import time
from colored import fg, bg, attr

def main():

    s = pyshorteners.Shortener()

    db_create()

    url  = str(input('Enter your url here: '))

    def short_url():
        shorted_url = s.chilpit.short(url)

        return shorted_url

    def show_urls():
        print('%s--------------------------------------------------\n %s' % (fg(79), attr(1)))
        for i in trange(100):
            time.sleep(0.01)
        print('%s--------------------------------------------------\n %s' % (fg(79), attr(1)))
        print(f'Default URL: {url} \n')
        print('%s--------------------------------------------------\n %s' % (fg(79), attr(1)))
        print(f'%sShorted URL: {short_url()}%s' % (fg(154), attr(1)))
        print('%s--------------------------------------------------\n %s' % (fg(79), attr(1)))


    show_urls()
    insert_urls(url, short_url())
 
    
            

if __name__ == '__main__':
    main()