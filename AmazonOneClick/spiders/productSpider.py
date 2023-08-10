import scrapy


class ProductspiderSpider(scrapy.Spider):
    name = "productSpider"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/COOFANDY-Shirts-Wrinkle-Free-Sleeve-Casual/dp/B09L8GNVJC?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Workout-Bodybuilding-Weightlifting-Training/dp/B085NF55WL?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Casual-Summer-Elastic-Trousers/dp/B07MBMKTQL?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Cotton-Henley-Sleeve-Hippie/dp/B08L6G6HCN?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Workout-Fitness-Bodybuilding-Sleeveless/dp/B07YC7DMF9?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Sleeve-Shirts-Button-Casual/dp/B093RZQLVX?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Textured-Designer-Western-Regular/dp/B083P314GB?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Regular-Fit-Short-Sleeve-Cotton-Casual/dp/B08FR31BH4?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Workout-Training-Bodybuilding-Weightlifting/dp/B0BS2N3PV6?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Trousers-Drawstring-Vacation-Summer/dp/B083V254PX?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Cotton-Henley-Sleeve-Hippie/dp/B083K8DD4K?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Fashion-Cotton-Hippie-Shirts/dp/B07MW7MGRQ?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Embroidered-Sleeve-Western-Regular-Fit/dp/B087WM19FT?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Vertical-Striped-Sleeve-Hawaiian/dp/B09KNB98S6?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Casual-Cotton-Sleeve-Collar/dp/B082XVRTJH?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Workout-Lightweight-Bodybuilding-Training/dp/B09LTRY112?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Casual-Blazer-Button-Blazers/dp/B09Z1S62F9?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Pieces-Cotton-Sleepwear-Pajamas/dp/B089Q4B87F?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Packable-Waterproof-Lightweight-Raincoat/dp/B095NYS5BW?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Casual-Button-Summer-Sleeve/dp/B09N6LJF5F?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Sleeve-Cotton-Chambray-Untucked/dp/B0BKCBK6DM?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Sleeve-Button-Regular-Cotton/dp/B094G1CTL9?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Gym-Shorts-Weightlifting-Bodybuilding/dp/B08HWZ7ZNX?ref_=ast_sto_dp&th=1&psc=1",
        "https://www.amazon.com/COOFANDY-Cotton-Casual-Blazer-Lightweight/dp/B07KWN8S8H?ref_=ast_sto_dp&th=1&psc=1"
    ]
    cookies = {
        "anonymid": "j7wsz80ibwp8x3",
        "_r01_": "1",
        "ln_uact": "mr_mao_hacker@163.com",
        "_de": "BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
        "depovince": "GW",
        "jebecookies": "2fb888d1-e16c-4e95-9e59-66e4a6ce1eae|||||",
        "ick_login": "1c2c11f1-50ce-4f8c-83ef-c1e03ae47add",
        "p": "158304820d08f48402be01f0545f406d9",
        "first_login_flag": "1",
        "ln_hurl": "http://hdn.xnimg.cn/photos/hdn521/20180711/2125/main_SDYi_ae9c0000bf9e1986.jpg",
        "t": "adb2270257904fff59f082494aa7f27b9",
        "societyguester": "adb2270257904fff59f082494aa7f27b9",
        "id": "327550029",
        "xnsid": "4a536121",
        "loginfrom": "syshome",
        "wp_fold": "0"
    }

    headers = {
        'Host': 'www.amazon.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; \
                           SM-A520F Build/NRD90M; wv) AppleWebKit/537.36 \
                           (KHTML, like Gecko) Version/4.0 \
                           Chrome/65.0.3325.109 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,\
                           application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, method='GET',headers=self.headers,cookies=self.cookies)
            break

    def parse(self, response):
        print(response.text)
        image_group_selectors = response.xpath(
            "//span[@id='productTitle']")
        print(image_group_selectors)
        pass
