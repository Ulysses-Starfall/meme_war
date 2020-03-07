# coding:utf-8
import sys

from PIL import Image


class MemeWarClient(object):
    arg_type_list = ['s', 'e']
    start_arg = None

    @classmethod
    def check_args(cls, arg):
        if arg in cls.arg_type_list:
            cls.start_arg = arg
            return True

        return False

    @classmethod
    def set_tasks(cls):
        if cls.start_arg == 's':
            pass
        elif cls.start_arg == 'e':
            pass
        else:
            pass


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Need args: s|e")
        sys.exit(0)

    if not MemeWarClient.check_args(sys.argv[1]):
        print("Wrong arg type, args must be :s|e")
        sys.exit(0)

    MemeWarClient.set_tasks()
