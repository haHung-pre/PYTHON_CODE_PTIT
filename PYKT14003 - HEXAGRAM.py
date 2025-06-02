from itertools import permutations, combinations

T = int(input())
for _ in range(T):
    a = list(map(int, input().split()))
    total = sum(a)
    if total % 3:
        print(0)
        continue
    s = total // 3
    V = [(k, j, i) for i in range(1, 12)
                      for j in range(1, i)
                      for k in range(1, j)
                      if a[i] + a[j] + a[k] + a[0] == s]
    perm_cache = {v: list(permutations(v)) for v in V}
    c_perm_cache = {}
    ans = 0
    for A, B in combinations(V, 2):
        if set(A) & set(B):
            continue
        C = tuple(sorted(set(range(1, 12)) - set(A) - set(B)))
        if C not in c_perm_cache:
            c_perm_cache[C] = list(permutations(C))
        for pa in perm_cache[A]:
            for pb in perm_cache[B]:
                for pc in c_perm_cache[C]:
                    if (a[pc[0]] + a[pa[0]] + a[pb[0]] + a[pc[1]] == s and
                        a[pc[0]] + a[pa[1]] + a[pc[2]] + a[pc[4]] == s and
                        a[pc[1]] + a[pb[1]] + a[pc[3]] + a[pc[4]] == s and
                        a[pa[2]] + a[pc[2]] + a[pc[3]] + a[pb[2]] == s):
                        ans += 1
                    if (a[pa[0]] + a[pb[1]] + a[pc[1]] + a[pc[4]] == s and
                        a[pa[2]] + a[pc[0]] + a[pc[2]] + a[pc[4]] == s and
                        a[pb[0]] + a[pa[1]] + a[pc[0]] + a[pc[3]] == s and
                        a[pb[2]] + a[pc[1]] + a[pc[2]] + a[pc[3]] == s):
                        ans += 1
    print(ans)
