# https://leetcode.com/problems/repeated-dna-sequences/

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

expected = ["AAAAACCCCC", "CCCCCAAAAA"]

def find_repeat_sequences(s: str):
    _l, n = 10, len(s)

    dna_to_int_map = {'A': 0, 'C': 1, 'T': 2, 'G': 3}
    dna_key_cnt = len(dna_to_int_map.keys())
    nums = [dna_to_int_map[s[i]] for i in range(len(s))]
    dna_pow = pow(dna_key_cnt, _l)

    h = 0
    seen, output = set(), set()
    for i in range(_l):
        h = h * dna_key_cnt + nums[i]

    seen.add(h)

    for i in range(1, n - _l + 1):  # end 10 before termination
        h = h * dna_key_cnt - nums[i - 1] * dna_pow + nums[i + _l - 1]
        if h in seen:
            output.add(s[i:i + _l])
        seen.add(h)

    return list(output)

res = find_repeat_sequences(s)
assert res == expected