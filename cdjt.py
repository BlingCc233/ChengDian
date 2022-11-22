import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
from fake_useragent import UserAgent

url = "https://www.wjx.cn/vm/t9rH0Rm.aspx# "  # 测试网址
'''
print(r"""
    本程序用于成电抢票
""")
url = input('输入问卷地址:')
'''
async def run():
    driver = await launch({
        # 谷歌浏览器的安装路径
        'executablePath': r'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
        # Pyppeteer 默认使用的是无头浏览器
        'headless': False,
        # 设置Windows-size和Viewport大小来实现网页完整显示
        'args': ['--no-sandbox', '--window-size=1480,760', '--disable-infobars'],
        'dumpio': True,
    })

    # 用 newPage 方法相当于浏览器中新建了一个选项卡,同时新建了一个Page对象
    page = await driver.newPage()
    # 简称换头
    await page.setUserAgent(
        UserAgent().random)

    await page.setViewport({'width': 1480, 'height': 760})
    # 反爬虫跳入网页
    await stealth(page)
    await page.goto(url)  # 问卷星网址

    # 模拟输入 账号密码  {'delay': rand_int()} 为输入时间
    await page.type('#q1', "曹福泰")
    await page.type('#q2', "2022080911020")

    await page.waitFor(1000)
    await page.click("#ctlNext")



asyncio.get_event_loop().run_until_complete(run())