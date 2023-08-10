import scrapy
from PipelineA.items import AmazonBrandSite


class BrandSiteSpider(scrapy.Spider):
    name = "brandSiteSpider"
    allowed_domains = ["amazon.com"]

    # 将url调整为入参的形式
    def __init__(self, url=None, *args, **kwargs):
        super(BrandSiteSpider, self).__init__(*args, **kwargs)
        self.url = url

    def start_requests(self):
        self.url = self.url.split("?")[0]
        yield scrapy.Request(url=self.url, callback=self.parse, method='GET')

    def parse(self, response, **kwargs):
        # Logo解析
        brand_info = {
            "logo_image_source": "",
            "logo_text": ""
        }
        logo_image_source = ""
        logo_text = ""

        logo_selector = response.xpath("//a[contains(@class, 'logo Header__logo')]")
        if logo_selector:
            logo_source = logo_selector.xpath("./img/@src").get()
            logo_image_source = response.urljoin(logo_source)

        brand_name_selector = response.xpath("//h1[@itemprop='itemListElement']/a/span/text()")
        if brand_name_selector:
            logo_text = brand_name_selector.get()

        brand_info["logo_image_source"] = logo_image_source
        brand_info["logo_text"] = logo_text

        # 页面结构解析
        navs = response.xpath("""//ul[@class='Navigation__navList__HrEra']""")
        parent_pages_selectors = navs.xpath("./li")
        pages = []
        for parent_page_selector in parent_pages_selectors:
            # 尝试获取某个div item下的a标签
            page_href_selector = parent_page_selector.xpath("./a")

            # 如果没有href属性，则跳过
            if not page_href_selector:
                continue

            page_info = {}

            # 判断是否为页面组，根据是否为页面组决定是否递归。这个属性记录在a标签中
            is_page_group = page_href_selector.xpath("./@aria-haspopup").get()
            if is_page_group == "false":
                # 如果不是页面组，则直接解析页面
                page_href_url = page_href_selector.xpath("./@href").get()
                page_name_selector = page_href_selector.xpath("./span")

                page_name = page_name_selector.xpath(
                    "./text()").get() if page_name_selector.xpath("./text()") else (
                    page_name_selector.xpath("./span/text()").get())
                page_info["page_name"] = page_name
                page_info["page_url"] = response.urljoin(page_href_url)
                page_info['is_page_group'] = False
            else:
                # 如果是页面组，完成任务后进行递归
                page_href_url = page_href_selector.xpath("./@href").get()
                page_name_selector = page_href_selector.xpath("./span")

                page_name = page_name_selector.xpath(
                    "./text()").get() if page_name_selector.xpath("./text()") else (
                    page_name_selector.xpath("./span/text()").get())
                page_info["page_name"] = page_name
                page_info["is_page_group"] = True
                page_info["sub_pages"] = []
                subpages_nav_selectors = parent_page_selector.xpath(
                    "./div[contains(@class,'Navigation__navList__HrEra level2')]/ul/li")
                for subpages_nav_selector in subpages_nav_selectors:
                    # 尝试获取某个div item下的a标签
                    page_href_selector = subpages_nav_selector.xpath("./a")
                    # 如果没有href属性，则跳过
                    if not page_href_selector:
                        continue
                    subpage_info = {}
                    page_href_url = page_href_selector.xpath("./@href").get()
                    page_name_selector = page_href_selector.xpath("./span")

                    page_name = page_name_selector.xpath(
                        "./text()").get() if page_name_selector.xpath("./text()") else (
                        page_name_selector.xpath("./span/text()").get())
                    subpage_info["page_name"] = page_name
                    subpage_info["page_url"] = response.urljoin(page_href_url)
                    page_info["sub_pages"].append(subpage_info)
            pages.append(page_info)

        yield AmazonBrandSite(brand_info=brand_info, pages=pages)
