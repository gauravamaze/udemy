from dataclasses import dataclass, field, astuple, asdict
import inspect
from pprint import pprint

@dataclass(frozen=True, order=True)
class Comment:
    # id : int
    # text : str
    # replies : list[int] = field(default_factory=list)

    name: list[int] = field(default_factory=list)
    cal: float = field(default_factory=10)

def main():
    c = Comment(["a"], "test")
    print(c)
    # print(astuple(c))
    # print(asdict(c))
    # pprint(inspect.getmembers(Comment, inspect.isfunction))

if __name__ == "__main__":
    main()