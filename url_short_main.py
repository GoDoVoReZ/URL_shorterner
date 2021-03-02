import pyshorteners
from url_db import *
from tqdm import trange
import time
from colored import fg, bg, attr



def short_url(url):

    s = pyshorteners.Shortener()

    shorted_url = s.chilpit.short(url)

    insert_urls(url=url, shorted_url=shorted_url)

    return shorted_url