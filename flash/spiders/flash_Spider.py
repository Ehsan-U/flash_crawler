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

