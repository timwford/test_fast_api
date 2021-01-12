from enum import Enum


class Test(Enum):
    TestOne = "testone"
    TestTwo = "testtwo"


if __name__ == "__main__":
    print(list(Test))
