import scrapy
from PipelineA.items import AmazonBrandSite


class BrandSiteSpider(scrapy.Spider):
    name = "brandSiteSpiderop"
    allowed_domains = ["amazon.com"]

    def __init__(self, url=None, *args, **kwargs):
        super(BrandSiteSpider, self).__init__(*args, **kwargs)
        self.url = url.split("?")[0] if url else None

    def start_requests(self):
        if self.url:
            yield scrapy.Request(url=self.url, callback=self.parse, method='GET')

    def parse(self, response, **kwargs):
        brand_info = {
            "logo_image_source": response.urljoin(
                response.xpath("//a[contains(@class, 'logo Header__logo')]/img/@src").get('')),
            "logo_text": response.xpath("//h1[@itemprop='itemListElement']/a/span/text()").get('')
        }

        navs = response.xpath("//ul[@class='Navigation__navList__HrEra']")
        pages = [self._extract_page_info(selector, response) for selector in navs.xpath("./li")]
        filtered_pages = [page for page in pages if page and '/feed' not in page['page_url']]
        yield AmazonBrandSite(brand_info=brand_info, pages=filtered_pages)

    def _extract_page_info(self, selector, response):
        page_info = {}
        page_href_selector = selector.xpath("./a")

        if not page_href_selector:
            return page_info

        page_info["page_name"] = self._get_page_name(page_href_selector)
        page_info["page_url"] = response.urljoin(page_href_selector.xpath("./@href").get(''))
        page_info["is_page_group"] = page_href_selector.xpath("./@aria-haspopup").get() == "true"

        if page_info["is_page_group"]:
            subpages = [self._extract_subpage_info(subpage_selector, response) for subpage_selector in
                        selector.xpath("./div[contains(@class,'Navigation__navList__HrEra level2')]/ul/li")]
            filtered_subpages = [subpage for subpage in subpages if subpage]
            page_info["sub_pages"] = filtered_subpages

        return page_info

    def _extract_subpage_info(self, selector, response):
        subpage_info = {}
        page_href_selector = selector.xpath("./a")
        if not page_href_selector:
            return subpage_info

        subpage_info["page_name"] = self._get_page_name(page_href_selector)
        subpage_info["page_url"] = response.urljoin(page_href_selector.xpath("./@href").get(''))

        return subpage_info

    def _get_page_name(self, selector):
        return selector.xpath("./span/text()").get() or selector.xpath("./span/span/text()").get() or ""
