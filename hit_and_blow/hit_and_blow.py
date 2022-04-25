import random, re


class HitAndBlow:
    def __init__(self, name = 'test'):
        self.name = name
        self.state_dict = dict()

    def reset(self):
        return self.state_dict.fromkeys(('answer', 'times'), 0)


    def setup(self):
        self.state_dict = self.reset()
        correct = random.sample(list(range(10)), 3)
        self.state_dict['answer'] = correct
        # print(self.state_dict)

    def play(self):
        self.setup()
        while True:
            num = input('>>>')
            if re.match(r'\d{3}', num):
                self.state_dict['times'] += 1
                answer = list(map(int, num[:]))
                hit = blow = 0
                for n in range(len(answer)):
                    t = 'x'
                    try:
                        t = list(self.state_dict['answer']).index(answer[n])

                    except ValueError:
                        pass

                    if t != 'x':
                        if t == n:
                            hit += 1

                        else:
                            blow += 1

                print('hit: {} blow: {}'.format(hit, blow))
                if hit == 3:
                    print('--結果--\n名前: {}\n挑戦回数: {}\n答え: {}'.format(self.name, self.state_dict['times'], self.state_dict['answer']))
                    break


if __name__ == '__main__':
    name = input('name > ')
    HitAndBlow(name).play()
