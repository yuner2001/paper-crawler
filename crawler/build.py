from cvpr-crawler import
type = {
    'example': ExampleCrawler,
}


def build_crawler(cfg):
    name = cfg['name']
    return type[name](cfg)
