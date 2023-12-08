import socialsecurity.calculator as calc


def main():
    for salary in range(10000, 160000, 10000):
        benefit = round(calc.benefit_at_67(salary))
        print(f'{salary},{benefit}')


if __name__ == '__main__':
    main()
