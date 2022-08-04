import random
from urllib import request
from http.cookies import SimpleCookie
from urllib.parse import parse_qs, urlparse
import scrapy
# from scrapy_playwright import 
from scrapy_splash import SplashRequest
from scrapy.http.cookies import CookieJar

def load_proxies():
    with open("/home/ubuntu/flash/flash/proxies.txt","r") as f:
        proxies = f.readlines()
    return proxies

def load_agents():
    agents = []
    with open("/home/ubuntu/flash/user-agents.txt") as f:
        lines = f.readlines()
        for line in lines:
            agents.append(line)
    return agents

class FlashSpiderSpider(scrapy.Spider):
    name = 'flash'
    last_page = "https://quizlet.com/subjects/arts-and-humanities/history-flashcards?lsid=45517675&lss=9.545421"
    allowed_domains = ['quizlet.com']
    PROXIES = load_proxies()
    AGENTS = load_agents()
    # custom_settings = {
    #     "PLAYWRIGHT_LAUNCH_OPTIONS": {
    #         "proxy": {
    #             "server": f"http://{random.choice(PROXIES).split(':')[0]}:{random.choice(PROXIES).split(':')[1]}",
    #             "username": f"{random.choice(PROXIES).split(':')[2]}",
    #             "password": f"{random.choice(PROXIES).split(':')[3]}".strip("\n"),
    #         },
            
    #     },
    #     "PLAYWRIGHT_CONTEXTS":{
    #         1:{
    #             "user_agent":f"{random.choice(AGENTS)}".strip("\n"),
    #         }
    #     }
    # }

    def start_requests(self):
        urls = [f"https://quizlet.com/subjects/arts-and-humanities/history-flashcards?page={i}" for i in range (1,667)]
        # url = 'https://httpbin.org/ip'
        for url in urls:
            agent = random.choice(self.AGENTS).strip("\n")
            proxy = random.choice(self.PROXIES)
            page_no = parse_qs(urlparse(url).query)['page'][0]
            domain,port,user,passs = proxy.split(':')[0],proxy.split(':')[1],proxy.split(':')[2],proxy.split(':')[3].strip("\n")
            yield scrapy.Request(url,callback=self.parse,meta={
                "playwright":True,
                "playwright_include_page":True,
                "playwright_context":f"page{page_no}",
                "playwright_context_kwargs":{
                    "ignore_https_errors":True,
                    "proxy": {
                        "server": f"http://{domain}:{port}",
                        "username": f"{user}",
                        "password": f"{passs}",
                    },
                    "user_agent":f"{agent}",
                }
                },errback=self.close_context_on_error)
        yield scrapy.Request(url=self.last_page,callback=self.parse,meta={
                "playwright":True,
                "playwright_include_page":True,
                "playwright_context":f"pagelast",
                "playwright_context_kwargs":{
                    "ignore_https_errors":True,
                    "proxy": {
                        "server": f"http://{domain}:{port}",
                        "username": f"{user}",
                        "password": f"{passs}",
                    },
                    "user_agent":f"{agent}",
                }
                },errback=self.close_context_on_error)

    async def parse(self, response):
        page = response.meta.get("playwright_page")
        sel = scrapy.Selector(text=response.text)
        for card in sel.xpath("//div[@class='SetPreviewCard-metadata']"):
            title = card.xpath(".//a/span/text()").get()
            term = card.xpath(".//span[@class='AssemblyPillText']/text()").get()
            username = card.xpath(".//span[@class='SetPreviewCard-username']/text()").get()
            yield {"Title":title,"Terms":term,"Username":username}
        await page.context.close()
        await page.close()

    async def close_context_on_error(self,failure):
        page = failure.request.meta["playwright_page"]
        await page.context.close()


        # print(response.request.headers)
###########################################
#
# Script to pass headers & cookies along 
#            with HTTP request
#        using "scrapy" framework
#
#                    by
#
#             Code Monkey King   
#
###########################################

# # packages
# from http.cookies import SimpleCookie
# import scrapy
# from scrapy.crawler import CrawlerProcess
# import json
# from rich.pretty import pprint

# # spider class
# class HeadersCookies(scrapy.Spider):
#     # spider name
#     name = 'headerscookies'
    
#     # urls
#     url_request = 'https://eoxkp4ymu1uhkqh.m.pipedream.net'
#     url_flash = 'https://quizlet.com'
    
#     # custom headers
#     headers = {
#         ':authority': 'quizlet.com',
#         ':method': 'GET',
#         ':path': '/subjects/arts-and-humanities/history-flashcards',
#         ':scheme': 'https',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#         'cache-control': 'max-age=0',
#         'cookie': 'app_session_id=dbfd5e6a-a075-4946-aa35-be4015592d8f; akv={}; qi5=18uh9wigyuvk2:murrL3f5BK0Rp.Ji90s4; qtkn=zCKG4femURebQMqN7Wf7Dg; fs=rg3gs0; __cf_bm=C9lMdGbPiOYiwWkQaq_zdc5rvyYbEPgIu3t7im5BllU-1659622320-0-AWamUYPFoA3WLdOwgTjDImb/xf20YMLKzhh0/YLd2Hm3Dqj/hzerkxakOxw7JYgDG8HY1w7l6yndS4eYInKeAa4=; __cfruid=44975196e2d1b623cbdf68b8ca84197ed3dcd847-1659622320; _cfuvid=kESpE10lQTNtnuoe1UxrmqPxEc9JoBWgE9eRartzytE-1659622320803-0-604800000',
#         'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
#         'sec-ch-ua-mobile': '?1',
#         'sec-ch-ua-platform': "Android",
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
#     }
    
    
#     # parse cookies
#     def parse_cookies(self, raw_cookies):
#         # parsed cookies
#         cookies = {}
        
#         # loop over cookies
#         for cookie in raw_cookies.split('; '):    
#             try:
#                 if "OptanonConsent" in cookie:
#                     # init cookie key
#                     key = cookie.split('===')[0]
#                     key = key.replace("===","=")
#                     val = cookie.split('===')[1]
#                     val = val.replace('===','=')
#                         # pprint(val)
#                 else:
#                     # init cookie key
#                     key = cookie.split('=')[0]
#                     if key == "__cf_bm":
#                         # init cookie value
#                         val = cookie.split('=')[1]
#                         val = f"{val}="
#                     else:
#                         val = cookie.split('=')[1]
#                         # pprint(val)
                    
#                 # parse raw cookie string
#                 cookies[key] = val
            
#             except:
#                 pass
#         pprint(raw_cookies)
#         pprint(cookies,expand_all=True)
#         return cookies
    
#     def raw_parse(self):
#         cookies = 'app_session_id=dbfd5e6a-a075-4946-aa35-be4015592d8f; akv={}; qi5=18uh9wigyuvk2:murrL3f5BK0Rp.Ji90s4; qtkn=zCKG4femURebQMqN7Wf7Dg; fs=rg3gs0; session_landing_page=SubjectPage/Subject; hide-fb-button=0; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Aug+04+2022+19:22:29+GMT+0500+(Pakistan+Standard+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=3045bf47-7117-4406-96db-beb07ef87ce3&interactionCount=1&landingPath=https://quizlet.com/subjects/arts-and-humanities/history-flashcards&groups=C0001:1,N01:1,C0002:1,C0004:1; __cf_bm=k8NKd6G9IprsxVP2dBUcJwWagn_dALSmHtB2ob1EsL0-1659623265-0-AUvNTqWOmxPIeEYxYwh3K18wahhnA6ADejcw4M5V9H9lAehSqijjsuMS1s9ISDQXWFJSyKESR15+/4cS1+lDHLw=; __cfruid=01598ad4ede73076cc533e1443719cbfc90cef9c-1659623265; _cfuvid=_GJF6NUQu7ofXRr.0UJrUv4TwlL8TmvZVLqgv4Gfg9k-1659623265828-0-604800000'
#         s = SimpleCookie()
#         s.load(cookies)
#         ready = {}
#         for k,v in s.items():
#             # print(k, v.value)
#             ready[k] = v.value
#         pprint(ready)
#         return ready
#     # crawler's entry point
#     def start_requests(self):
#         # raw = [
#         #     b'app_session_id=dbfd5e6a-a075-4946-aa35-be4015592d8f; expires=Thu, 04-Aug-2022 14:42:00 GMT; Max-Age=1800; path=/; secure=',
#         #     b'akv={}; expires=Fri, 05-Aug-2022 14:12:00 GMT; Max-Age=86400; path=/; secure=; httponly='
#         #     b'qi5=18uh9wigyuvk2:murrL3f5BK0Rp.Ji90s4; expires=Sun, 01-Aug-2032 14:12:00 GMT; Max-Age=315360000; path=/; secure=; httponly=',
#         #     b'qtkn=zCKG4femURebQMqN7Wf7Dg; path=/; secure=',
#         #     b'fs=rg3gs0; expires=Sun, 01-Aug-2032 14:12:00 GMT; Max-Age=315360000; path=/; secure=; httponly=',
#         #     b'__cf_bm=C9lMdGbPiOYiwWkQaq_zdc5rvyYbEPgIu3t7im5BllU-1659622320-0-AWamUYPFoA3WLdOwgTjDImb/xf20YMLKzhh0/YLd2Hm3Dqj/hzerkxakOxw7JYgDG8HY1w7l6yndS4eYInKeAa4=; path=/; expires=Thu, 04-Aug-22 14:42:00 GMT; domain=.quizlet.com; HttpOnly=; Secure=; SameSite=None',
#         #     b'__cfruid=44975196e2d1b623cbdf68b8ca84197ed3dcd847-1659622320; path=/; domain=.quizlet.com; HttpOnly=; Secure=; SameSite=None',
#         #     b'_cfuvid=kESpE10lQTNtnuoe1UxrmqPxEc9JoBWgE9eRartzytE-1659622320803-0-604800000; path=/; domain=.quizlet.com; HttpOnly=; Secure=; SameSite=None',
#         #     b'OptanonConsent===isGpcEnabled=0&datestamp=Thu+Aug+04+2022+19%3A18%3A02+GMT%2B0500+(Pakistan+Standard+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=3045bf47-7117-4406-96db-beb07ef87ce3&interactionCount=1&landingPath=https%3A%2F%2Fquizlet.com%2Fsubjects%2Farts-and-humanities%2Fhistory-flashcards&groups=C0001%3A1%2CN01%3A1%2CC0002%3A1%2CC0004%3A1',
#         #     b'session_landing_page=SubjectPage%2FSubject; hide-fb-button=0;'
#         # ]
#         # # extract raw cookies
#         # raw_cookies = '; '.join([
#         #     cookie.decode('utf-8') for cookie in raw
#         # ])
#         # self.parse_cookies(raw_cookies),
#         # pprint(self.headers)
#         # make HTTP GET request to "requestbin.com"
#         yield scrapy.Request(
#             url=self.url_flash,
#             headers=self.headers,
#             # cookies=self.raw_parse(raw_cookies),
#             cookies=self.raw_parse(),
#             callback=self.parse
#         )
        
#     # parse response
#     def parse(self, response):
#         print("\nCookie: ",response.headers.getlist('Set-Cookie'))
#         print("\Headers: ",response.headers.getlist('Set-Cookie'))
        


# # main driver
# if __name__ == '__main__':
#     # run spider
#     process = CrawlerProcess()
#     process.crawl(HeadersCookies)
#     process.start()














        
        
        
        
        
        
