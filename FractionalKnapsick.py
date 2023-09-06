from sys import stdin


def optimal_value(capacity, weights, values):
    if capacity == 0 or len(weights) == 0 or len(values) == 0:
        return 0
    value = 0.
    fractionalWeights =  list(map(lambda x : [x,values[x]/weights[x]], range(len(weights))))
    fractionalWeights.sort(key = lambda x : x[1], reverse = True)
    for fractionalWeight in fractionalWeights:
        if weights[fractionalWeight[0]] <= capacity:
            value = value + values[fractionalWeight[0]]
            capacity = capacity - weights[fractionalWeight[0]]
        else:
            value = value + fractionalWeight[1] * capacity
            capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
