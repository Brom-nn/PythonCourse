import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler:        # Имена классов должно быть согласно CapWords

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):   # Каждое следующее слово в Имени функций должно начинаться с большой буквы
          mp3s = []                      # нет 4 отступов в теле функции rename, не на равне с другиме строками в теле функции
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname)) # лишние скобки в конце строки )).
          f = open(output, 'r')           # нет 4 отступов в теле цикла for, не на равне с другиме строками в теле цикла
          f.write(str(self.map))          # нет 4 отступов в теле цикла for, не на равне с другиме строками в теле цикла

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:   # тело with имеет разный индекс отступов в каждой строке. Неверный аргумент(filename).
            self.map = ast.literal_eval(f.read())
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:       # тело цикла for имеет разный индекс отступов в каждой строке.
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) # лишня скобка в конце строки ).
        os.remove(restore_path)
                
     def generateName(self, seed=time()): # функция generateName имеет больше 4 отступов.
          return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info')
          else:
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()