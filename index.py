# -*- coding: utf-8 -*-
import logging
import asyncio
from pyppeteer import launch
from pyppeteer.util import check_chromium, chromium_executable

loop = asyncio.get_event_loop()

async def main():
    browser = await launch(headless=True, args = ['--no-sandbox'], devtools=False)
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    await page.screenshot({'path': '/tmp/baidu.png'})
    await browser.close()

def handler(event, context):
  logger = logging.getLogger()
  logger.info(chromium_executable())

  return loop.run_until_complete(main())