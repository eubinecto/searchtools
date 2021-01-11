from collections import Callable
from typing import List


class Builder:

    def construct(self):
        for step in self.steps():
            step()

    def steps(self) -> List[Callable]:
        raise NotImplementedError


class QueryBuilder(Builder):
    def steps(self) -> List[Callable]:
        pass


class ResultBuilder(Builder):
    def steps(self) -> List[Callable]:
        pass


class EntryBuilder(Builder):
    def steps(self) -> List[Callable]:
        pass
