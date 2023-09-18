import tqdm
from selenium import webdriver

from logger import craw_logger


class BaseCrawler(object):

    def __init__(self, url, start, end):
        assert start <= end, 'start index must lower than end!'
        self.name = 'base'
        self.url = url
        self._start = start
        self._end = end
        self.data = list()
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        craw_logger.info(f'{self.name}-crawler initialized!')
        craw_logger.info(f'total item:{self.end - self.start}.')

    @property
    def start(self):
        return self.start

    @property
    def end(self):
        return self._end

    def craw_a_step(self, idx, *args):
        '''
            here to put your own crwaler logic
        '''
        raise NotImplementedError

    def craw(self, *args):
        try:
            craw_logger.info(f'{self.name} start to craw!')
            for i in tqdm(range(self.end - self.start)):
                i = i + self.start
                self.craw_a_step(i, *args)
            craw_logger.info(f'{self.name} finish to crawl!')
        finally:
            craw_logger.exception(
                f'somthing wrong happend when crawling data, terminate on index {i - self.start}')
