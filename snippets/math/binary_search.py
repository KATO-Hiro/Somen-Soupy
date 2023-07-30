# -*- coding: utf-8 -*-


# TODO: Change lower value if necessary.
ng = 0
ok = 10**9 + 1

ok = 0
ng = 10**9 + 1


def binary_search(ok, ng):
    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if is_met_conditions(wj):
            ok = wj
        else:
            ng = wj

    return ok


def is_met_conditions(wj) -> bool:
    # TODO: Write here.

    # Condition is True.
    if True:
        return True
    else:
        return False


ans = binary_search(ok=ok, ng=ng)
print(ans)
