from base import BaseCrawler


class ExampleCrawler(BaseCrawler):

    def __init__(self, cfg):
        name = cfg['name']
        url = cfg['url']
        start = cfg['start']
        end = cfg['end']
        super(name, url, start, end)

    def craw_a_step(self, idx, data)
