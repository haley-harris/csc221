#!python3

import requests, os, bs4

# starting url
url = 'https://xkcd.com'

# creates directory to store comics in
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):

    # download page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # find url of comic image
    comic_elem = soup.select('#comic img')

    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')

        # download image
        print('Downloading image %s...' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

        # save image to xkcd directory
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)),
                     'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

        # get Prev button's url
        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prev_link.get('href')
