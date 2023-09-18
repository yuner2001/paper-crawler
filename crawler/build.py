from base import BaseCrawler

type = {
    'example': ExampleCrawler,
}


def build_crawler(cfg):
    name = cfg['name']
    return type[name](cfg)
