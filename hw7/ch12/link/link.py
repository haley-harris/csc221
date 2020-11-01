#!/usr/bin/env python3
''' Link Verification

Author: Haley Harris
'''

import argparse, requests, bs4

def verify_links(url):
    '''Given a URL of a web page, attempt to download every linked
    page on the page. Flage any pages that have a 404 "Not Found"
    status code and print them out as broken links.

    Args:
      url (str): URL to crawl and verify

    Returns:
      None

    '''
    print(f'Downloading page {url}')
    # Download page
    res = requests.get(str(url))
    res.raise_for_status()

    url_soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # select links tagged with <a>
    link_elem = url_soup.select('a')

    for link in link_elem:
      # get links from href tag
      page_links = link.get('href')

      # download links and print an exception for broken links
      try:
        res = requests.get(page_links)
        res.raise_for_status()
      except Exception:
        print(f'There was a problem with this link: {page_links}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL to verify links')

    args = parser.parse_args()

    verify_links(args.url)

if __name__=='__main__':
    main()