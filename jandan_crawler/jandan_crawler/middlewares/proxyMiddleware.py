import base64


# Start your middleware class
import random


class proxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = random.choice(self.proxy_list)

    proxy_list = ['http://110.182.62.2:8118', 'http://120.25.171.183:8080', 'http://183.61.236.54:3128',
                  'http://121.33.226.167:3128', 'http://101.201.235.141:8000', 'http://115.46.64.8:8123',
                  'http://110.208.19.113:8080', 'http://61.180.16.198:3128'
                  ]
