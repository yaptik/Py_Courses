from package_bank import stats as bs, logic as bl, exports as be


def main():
    bs.stat()
    bl.add(123)
    bl.change(321)
    bl.delete(453)
    bl.show()
    li = [1, 2, 3, 4576, 5, 23]
    be.export(li)


if __name__ == '__main__':
    print('main.py was started')
    main()
