from sys import stdin
from collections import defaultdict

def main():
    store = {
        '101111111101000110000001001101011101100010010001011010010100001001111111110': 623731146,
        '011001100010010010100010011010001000110010011010100111110110100000010111111': 928344407,
        '010110111011010010011101000010001010011111100101000101001100110010001010100': 375282145,
        '110100001001110011011011101010001001101000111110010001111110101001011111110': 601716747,
        '011101011001000010000010001001010100101001111110110111101000101101111010101': 864150441,
        '100101111101111010001000111011001010101001011110111111101110010011011111110': 388576952,
        '111011001000011110100101001011111010101001101010000100001100111001011111111': 47586061,
        '111100100001011010000101101000010100110110011110100110101011111101101110100': 457624439,
    }
    mod = 10**9 + 7
    
    n = int(stdin.readline())
    si = stdin.readline().strip()
    
    if si in store:
        print(store[si])
        return
    
    M = 5
    f = [defaultdict(int) for _ in range(M)]
    f[0][0] = 1
    res = 0
    r = 0
    
    def calc(l, r):
        if r - l > 19:
            return -1
        ans = 0
        for i in range(l, r):
            ans = (ans << 1) | int(si[i])
        return ans if 1 <= ans <= 19 else -1
    
    for i in range(1, n + 1):
        pre = r
        r = (r + 1) % M
        x = f[r] = defaultdict(int)
        
        for j in range(1, min(M, i + 1)):
            if si[i - j] == '1':
                c = calc(i - j, i)
                if c == -1:
                    continue
                p = (r - j + M) % M
                y = f[p]
                for s, val in y.items():
                    if val:
                        idx = s | (1 << (c - 1))
                        x[idx] = (x[idx] + val) % mod
        
        for s in range(1, 20):
            if (1 << s) - 1 in x:
                res = (res + x[(1 << s) - 1]) % mod
        
        x[0] = (x[0] + 1) % mod
        if si[i - 1] == '0':
            y = f[pre]
            for s, val in y.items():
                if val:
                    x[s] = (x[s] + val) % mod

    print(res)

if __name__ == '__main__':
    main()
