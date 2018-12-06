read_ints = lambda: list(map(int, input().split(' ')))


def solve(T, forbidden_seqs):
    # remove the useless forbidden sequences: O(n)
    forbidden_seqs.sort(key=lambda x: len(x))
    valid_forb_seqs = []
    for seq in forbidden_seqs:
        for valid_seq in valid_forb_seqs.copy():
            if seq.startswith(valid_seq):
                break
        else:
            valid_forb_seqs.append(seq)

    # compute the reductions
    reduction = map(lambda f_seq: 2 ** (T - len(f_seq)), valid_forb_seqs)

    return 2 ** T - sum(reduction)


if __name__ == '__main__':
    cases = read_ints()[0]

    forbidden_seqs = []

    with open('output.txt', 'w') as f:
        for i in range(1, cases + 1):
            T, P = read_ints()
            forbidden_seqs = [input() for _ in range(P)]
            result = solve(T, forbidden_seqs)
            f.write('Case #{}: {}\n'.format(i, result))
            print('Case #{}: {}'.format(i, result))
