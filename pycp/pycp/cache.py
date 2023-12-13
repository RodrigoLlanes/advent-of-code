from typing import Callable, TypeVar, Generic, List

T = TypeVar("T")


class Cache(Generic[T]):
    def __init__(self, f: Callable[[...], T], params: List[int]) -> None:
        self.f = f
        self.mem = {}
        self.params = params

    def clear(self) -> None:
        self.mem.clear()

    def __call__(self, *args) -> T:
        if len(self.params) == 0:
            key = tuple(args)
        else:
            key = tuple(args[i] for i in self.params)

        if key not in self.mem:
            self.mem[key] = self.f(*args)
        return self.mem[key]


def cache(*params: int) -> Callable[[Callable[[...], T]], Cache[T]]:
    def wrapper(f: Callable[[...], T]) -> Cache[T]:
        return Cache(f, list(params))
    return wrapper
