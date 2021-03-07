import collections
import itertools


list_of_letters = list('абракадабра')
letter_cnt = collections.Counter(list_of_letters)


emotion_cnt = collections.Counter({'like': 2, 'dislake': 3})
iter_list = list(emotion_cnt.elements())


def tail(filename, n=2):
    """Возвращает n последних строк файла'"""
    with open(filename) as f:
        return collections.deque(f, n)


def moving_average(iterable, n=3):
    it = iter(iterable)

    # print(it)
    # for i in it:
    #     print(i)

    d = collections.deque(itertools.islice(it, n-1))
    print(d)

    d.appendleft(0)
    s = sum(d)

    for elem in it:
        print(elem)

        s += elem - d.popleft()
        d.append(elem)

        print(s)

        yield s / n






if __name__ == '__main__':
    # print(letter_cnt)
    # print(emotion_cnt)
    # print(iter_list)
    # print(letter_cnt.most_common(3))
    # print(letter_cnt.most_common(3))
    # print(letter_cnt.most_common()[:-3: -1])

    # filename = '/home/user/PycharmProjects/pytest/collections/files/text.txt'
    # x = tail(filename)
    # print(x)

    iterable = [40, 30, 50, 46, 39, 44]
    x = moving_average(iterable)
    print(x)