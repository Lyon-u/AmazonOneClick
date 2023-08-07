import logging


def logo_parser(response):
    logo = ''
    try:
        logging.warning(f"开始从解析{response.url}logo")
        logo = response.xpath("""//a[@class='logo Header__logo__NZN2D']/img/@src""").get()
        logging.warning(f"logo为{logo}") if logo else logging.critical(f"logo为空")
    except Exception as e:
        logging.critical(f"在{response.url}页面解析Logo时出现异常：{e}")
    finally:
        return '' if logo is None else logo
