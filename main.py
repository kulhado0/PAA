from brute_force import BruteForce
from dynamic import Dynamic
from guloso import Guloso


def main():
    brute_force_exec()
    dynamic_exec()
    guloso_exec()


def brute_force_exec():
    brute_force = BruteForce()
    min_path = brute_force.get_min_path()
    print('Distância percorrida (Brute Force): ', min_path)


def dynamic_exec():
    dynamic_programming = Dynamic()
    min_path = dynamic_programming.get_min_path()
    print('Distância percorrida (Programação dinâmica): ', min_path)


def guloso_exec():
    guloso = Guloso()
    min_path = guloso.get_min_path()
    print('Distância percorrida (Algoritmo Guloso): ', min_path)


if __name__ == '__main__':
    main()
