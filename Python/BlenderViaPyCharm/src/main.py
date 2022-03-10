import importlib
import TestClass
importlib.reload(TestClass)


def main():
    print("All good")
    tc = TestClass.TestClass()
    tc.draw_monkey()


if __name__ == '__main__':
    main()
