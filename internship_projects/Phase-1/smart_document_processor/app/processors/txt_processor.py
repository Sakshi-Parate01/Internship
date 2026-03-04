# app/processors/txt_processor.py
import aiofiles
from .base import Processor


class TXTProcessor(Processor):

    async def process(self):
        async with aiofiles.open(self.filepath, 'r') as f:
            content = await f.read()
        return content