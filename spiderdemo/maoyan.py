
from urllib import request

url = 'https://piaofang.maoyan.com/dashboard'

url = 'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=1888f46e238c8-0f85d2ea939d0f-26031b51-1fa400-1888f46e238c8&timeStamp=1686031813868&User-Agent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2&index=613&channelId=40009&sVersion=2&signKey=4b617c39a736645978f183e02b632db4'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
        '(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
headers = {
    'User-Agent': agent
}
rq = request.Request(url, headers=headers)

resp = request.urlopen(rq)
print(resp.read().decode('utf-8'))