import scrapy, json, re
from urllib.parse import urlencode
from AmazonOneClick.items import Product

API_KEY = 'ae34894f-c29b-4bb1-a700-778de3f7232c'


def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


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
    custom_settings = {
        'ITEM_PIPELINES': {
            "AmazonOneClick.pipelines.AmazonOneclickPipelineA": 3,
        }
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse, method='GET')
            break

    def parse(self, response):
        image_data = json.loads(re.findall(r"colorImages':.*'initial':\s*(\[.+?\])},\n", response.text)[0])
        variant_data = re.findall(r'dimensionValuesDisplayData"\s*:\s* ({.+?}),\n', response.text)
        feature_bullets = [bullet.strip() for bullet in response.css("#feature-bullets li ::text").getall()]
        price = response.css('.a-price span[aria-hidden="true"] ::text').get("")
        if not price:
            price = response.css('.a-price .a-offscreen ::text').get("")
        yield Product(name=response.css("#productTitle::text").get("").strip(),
                      price=price,
                      stars=response.css("i[data-hook=average-star-rating] ::text").get("").strip(),
                      rating_counts=response.css("div[data-hook=total-review-count] ::text").get("").strip(),
                      feature_bullets=feature_bullets,
                      images=image_data,
                      variant_data=variant_data)
