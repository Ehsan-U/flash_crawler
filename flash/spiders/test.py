# # # from urllib import request
# # # from http.cookies import SimpleCookie
# # # import scrapy
# # # from scrapy_splash import SplashRequest
# # # from scrapy.http.cookies import CookieJar

# # # def parse_cookie(cookies=None):
# # #     raw = [
# # # {
# # #     "domain": ".quizlet.com",
# # #     "expirationDate": 1659615627.115833,
# # #     "hostOnly": "false",
# # #     "httpOnly": "true",
# # #     "name": "__cf_bm",
# # #     "path": "/",
# # #     "sameSite": "no_restriction",
# # #     "secure": "true",
# # #     "session": "false",
# # #     "storeId": "0",
# # #     "value": "dM.cpSqcHUGRr.UuJXvmDFazG2wSiNkTA9EUfZagnxA-1659613827-0-AWcMCwUwi5Xd4co97Q7/B/IIPIPoh4G83SeqEm+d2Uy0k+FI9eNdgZfWUo6gqwvL3dxMTHO5GvpGu0CbIofK6rU=",
# # #     "id": 1
# # # },
# # # {
# # #     "domain": ".quizlet.com",
# # #     "hostOnly": "false",
# # #     "httpOnly": "true",
# # #     "name": "__cfruid",
# # #     "path": "/",
# # #     "sameSite": "no_restriction",
# # #     "secure": "true",
# # #     "session": "true",
# # #     "storeId": "0",
# # #     "value": "5c7585ba56fbdf46b9a0b39114cbea110ae0107d-1659613827",
# # #     "id": 2
# # # },
# # # {
# # #     "domain": ".quizlet.com",
# # #     "hostOnly": "false",
# # #     "httpOnly": "true",
# # #     "name": "_cfuvid",
# # #     "path": "/",
# # #     "sameSite": "no_restriction",
# # #     "secure": "true",
# # #     "session": "true",
# # #     "storeId": "0",
# # #     "value": "F.R0jxQDk.wJM_RUbzddbX1OOl_xA2hOOYpQJCEKPfU-1659613827135-0-604800000",
# # #     "id": 3
# # # },
# # # {
# # #     "domain": ".quizlet.com",
# # #     "expirationDate": 1659634974,
# # #     "hostOnly": "false",
# # #     "httpOnly": "false",
# # #     "name": "arp_scroll_position",
# # #     "path": "/",
# # #     "sameSite": "unspecified",
# # #     "secure": "false",
# # #     "session": "false",
# # #     "storeId": "0",
# # #     "value": "0",
# # #     "id": 4
# # # },
# # # {
# # #     "domain": ".quizlet.com",
# # #     "expirationDate": 1691149827,
# # #     "hostOnly": "false",
# # #     "httpOnly": "false",
# # #     "name": "OptanonConsent",
# # #     "path": "/",
# # #     "sameSite": "lax",
# # #     "secure": "false",
# # #     "session": "false",
# # #     "storeId": "0",
# # #     "value": "isGpcEnabled=0&datestamp=Thu+Aug+04+2022+16%3A50%3A27+GMT%2B0500+(Pakistan+Standard+Time)&version=6.34.0&isIABGlobal='false'&hosts=&consentId=a4191b22-21ee-44f0-a9f6-e22abc612d1d&interactionCount=1&landingPath=https%3A%2F%2Fquizlet.com%2Fsubjects%2Farts-and-humanities%2Fhistory-flashcards&groups=C0001%3A1%2CN01%3A1%2CC0002%3A1%2CC0004%3A1",
# # #     "id": 5
# # # },
# # # {
# # #     "domain": "quizlet.com",
# # #     "expirationDate": 1659700222.140847,
# # #     "hostOnly": "true",
# # #     "httpOnly": "true",
# # #     "name": "akv",
# # #     "path": "/",
# # #     "sameSite": "unspecified",
# # #     "secure": "true",
# # #     "session": "false",
# # #     "storeId": "0",
# # #     "value": "%7B%7D",
# # #     "id": 6
# # # },
# # # {
# # #     "domain": "quizlet.com",
# # #     "expirationDate": 1659615629,
# # #     "hostOnly": "true",
# # #     "httpOnly": "false",
# # #     "name": "app_session_id",
# # #     "path": "/",
# # #     "sameSite": "unspecified",
# # #     "secure": "true",
# # #     "session": "false",
# # #     "storeId": "0",
# # #     "value": "10719b3b-ffe1-46d3-9cf3-5b330f7f2c97",
# # #     "id": 7
# # # },
# # # {
# # #     "domain": "quizlet.com",
# # #     "expirationDate": 1974969383.382625,
# # #     "hostOnly": "true",
# # #     "httpOnly": "true",
# # #     "name": "fs",
# # #     "path": "/",
# # #     "sameSite": "unspecified",
# # #     "secure": "true",
# # #     "session": "false",
# # #     "storeId": "0",
# # #     "value": "rg36sm",
# # #     "id": 8
# # # },
# # # {
# # #     "domain": "quizlet.com",
# # #     "expirationDate": 1675161405,
# # #     "hostOnly": "true",
# # #     "httpOnly": "false",
# # #     "name": "g_state",
# # #     "path": "/",
# # #     "sameSite": "unspecified",
# # #     "secure": "false",
# # #     "session": "false",
# # #     "storeId": "0",
# # #     "value": "{\"i_p\":1659616605579,\"i_l\":1}",
# # #     "id": 9
# # # },
# # # {
# # #     "domain": "quizlet.com",
# # #     "expirationDate": 1974969383.382575,
# # #     "hostOnly": "true",
# # #     "httpOnly": "true",
# # #     "name": "qi5",
# # #     "path": "/",
# # #     "sameSite": "unspecified",
# # #     "secure": "true",
# # #     "session": "false",
# # #     "storeId": "0",
# # #     "value": "a12mdgr0t6fx%3AgpsUd4D4XfOpi91BGsX9",
# # #     "id": 10
# # # },
# # # {
# # #     "domain": "quizlet.com",
# # #     "hostOnly": "true",
# # #     "httpOnly": "true",
# # #     "name": "qmeasure__persistence",
# # #     "path": "/",
# # #     "sameSite": "unspecified",
# # #     "secure": "true",
# # #     "session": "true",
# # #     "storeId": "0",
# # #     "value": "%7B%2226%22%3A%2210000000%22%2C%2222%22%3A%2200000001%22%2C%2219%22%3A%2200010000%22%7D",
# # #     "id": 11
# # # },
# # # {
# # #     "domain": "quizlet.com",
# # #     "hostOnly": "true",
# # #     "httpOnly": "false",
# # #     "name": "qtkn",
# # #     "path": "/",
# # #     "sameSite": "unspecified",
# # #     "secure": "true",
# # #     "session": "true",
# # #     "storeId": "0",
# # #     "value": "FQ5ewDdEmyfbUUvrCwfBxF",
# # #     "id": 12
# # # },
# # # {
# # #     "domain": "quizlet.com",
# # #     "hostOnly": "true",
# # #     "httpOnly": "false",
# # #     "name": "session_landing_page",
# # #     "path": "/",
# # #     "sameSite": "unspecified",
# # #     "secure": "true",
# # #     "session": "true",
# # #     "storeId": "0",
# # #     "value": "SubjectPage%2FSubject",
# # #     "id": 13
# # # }
# # # ]
# # #     sc = SimpleCookie()
# # #     cjar = CookieJar()
# # #     for c in raw:
# # #         sc.load(c)
# # #         cjar.set_cookie()
    
# # #     return cjar

# # # class FlashSpiderSpider(scrapy.Spider):
# # #     name = 'flash'
# # #     c = CookieJar()
# # #     cjar = parse_cookie()
# # #     allowed_domains = ['quizlet.com']
# # #     def start_requests(self):
# # #         url = "https://quizlet.com/subjects/arts-and-humanities/history-flashcards"
# # #         yield scrapy.Request(url,callback=self.parse,meta={"cookiejar":self.cjar})

# # #     def parse(self, response):
# # #         print(response.text)
# # #         print(response.request.headers)
# # #         print(response.headers)
# # ###########################################
# # #
# # # Script to pass headers & cookies along 
# # #            with HTTP request
# # #        using "scrapy" framework
# # #
# # #                    by
# # #
# # #             Code Monkey King   
# # #
# # ###########################################

# # # packages
# # import scrapy
# # from scrapy.crawler import CrawlerProcess
# # import json

# # # spider class
# # class HeadersCookies(scrapy.Spider):
# #     # spider name
# #     name = 'headerscookies'
    
# #     # urls
# #     url_request = 'https://eoxkp4ymu1uhkqh.m.pipedream.net'
# #     # url_rightmove = 'https://quizlet.com/subjects/arts-and-humanities/history-flashcards'
    
# #     # custom headers
# #     headers = {
# #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# #         'accept-encoding': 'gzip, deflate, br',
# #         'accept-language': 'en-US,en;q=0.9',
# #         'cache-control': 'no-cache',
# #         'pragma': 'no-cache',
# #         'sec-fetch-mode': 'navigate',
# #         'sec-fetch-site': 'none',
# #         'sec-fetch-user': '?1',
# #         'upgrade-insecure-requests': '1',
# #         'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# #     }
    
    
# #     # parse cookies
# #     def parse_cookies(self, raw_cookies):
# #         # parsed cookies
# #         cookies = {}
        
# #         # loop over cookies
# #         for cookie in raw_cookies.split('; '):    
# #             try:
# #                 # init cookie key
# #                 key = cookie.split('=')[0]
                
# #                 # init cookie value
# #                 val = cookie.split('=')[1]
                
# #                 # parse raw cookie string
# #                 cookies[key] = val
            
# #             except:
# #                 pass
        
# #         return cookies
    
# #     # crawler's entry point
# #     def start_requests(self):
# #         r = [
# #             'app_session_id=5d6fa34b-a435-49dc-90de-56589e7c5ae8; expires=Thu, 04-Aug-2022 13:38:28 GMT; Max-Age=1800; path=/; secure',
# #             'akv={}; expires=Fri, 05-Aug-2022 13:08:28 GMT; Max-Age=86400; path=/; secure; httponly',
# #             '__cf_bm=acUYVi3zEbFqTxNIlp7b0DH.DQ1pkF05syB4bt8XEGM-1659618509-0-AZ0AW55yYjwb09DXPwDbXDMfhyphY+NG6hNTO3/Wmxa1KXgPe/Em4p8+MS0zuYmwo/D9a9vD/VsOtsObEutCWrk=; path=/; expires=Thu, 04-Aug-22 13:38:29 GMT; domain=.quizlet.com; HttpOnly; Secure; SameSite=None',
# #             '__cfruid=1aafda8a54cc1d7afe25af875d67a825bb979ce3-1659618509; path=/; domain=.quizlet.com; HttpOnly; Secure; SameSite=None',
# #             '_cfuvid=RpCtBauEvw8P4TYcAYBjvAPB6tf8UUUwl.nW.nMkuMI-1659618509361-0-604800000; path=/; domain=.quizlet.com; HttpOnly; Secure; SameSite=None',
# #         ]
# #         # extract raw cookies
# #         raw_cookies = '; '.join([
# #             cookie
# #             for cookie in r
# #         ])
            
# #         # make HTTP GET request to "requestbin.com"
# #         yield scrapy.Request(
# #             url=self.url_request,
# #             headers=self.headers,
# #             cookies=self.parse_cookies(raw_cookies),
# #             callback=self.parse
# #         )
        
# #     # parse response
# #     def parse(self, response):
# #         print('\n\nRESPONSE URL: %s\n\n' % response.url)
        


# # # main driver
# # if __name__ == '__main__':
# #     # run spider
# #     process = CrawlerProcess()
# #     process.crawl(HeadersCookies)
# #     process.start()
# import requests

# r = requests.get("http://httpbin.org/ip",proxies={"http":"http://zproxy.lum-superproxy.io:22225"},auth=("lum-customer-hl_88d916f7-zone-data_center-ip-181.215.20.83","xm4yia2bzeh9"))
# print(r.text)
        