# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from urllib.parse import urlparse

def extract_base_url(url):
  """
  Extracts the base URL (scheme and netloc) from a given URL.

  Args:
    url: The full URL string.

  Returns:
    The base URL, including the scheme and netloc (e.g., "https://www.example.com").
  """
  parsed_url = urlparse(url)
  return f"{parsed_url.scheme}://{parsed_url.netloc}"
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        base=extract_base_url(startUrl)
        n=len(base)
        def basecrawl(seen,current):
            print(seen,current)
            new=htmlParser.getUrls(current)
            for x in new:
                print(' '*5,x)
                if x not in seen and x[:n]==base:
                    seen.add(x)
                    basecrawl(seen,x)

            return
        links=set()
        links.add(startUrl)
        print(links)
        basecrawl(links,startUrl)
        return list(links)
