# app/processors/base.py
from abc import ABC, abstractmethod


class Processor(ABC):

    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    async def process(self):
        pass