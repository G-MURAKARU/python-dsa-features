import contextlib


def passwordCracker(passwords, loginAttempt, memo: dict = None):
    # Write your code here

    # if not loginAttempt:
    #     return ""

    # all_ways = ""

    # for password in passwords:
    #     with contextlib.suppress(ValueError):
    #         if loginAttempt.index(password) == 0:
    #             suffix = loginAttempt[len(password) :]
    #             suffix_ways = passwordCracker(passwords, suffix)
    #             target_ways = password
    #             # target_ways.extend(iter(suffix_ways))
    #             target_ways += f" {suffix_ways}"
    #             # all_ways.extend(iter(target_ways))
    #             all_ways += target_ways

    # return all_ways

    if memo is None:
        memo = {}

    if loginAttempt in memo:
        return memo.get(loginAttempt)

    if not loginAttempt:
        return ""

    the_way = "WRONG PASSWORD"

    for password in passwords:
        with contextlib.suppress(ValueError):
            if loginAttempt.index(password) == 0:
                suffix = loginAttempt[len(password) :]
                found_suffix = passwordCracker(passwords, suffix, memo)
                if found_suffix == "WRONG PASSWORD":
                    continue
                the_way = f"{password} {found_suffix}".rstrip()
                break

    memo[loginAttempt] = the_way
    return the_way


print(
    passwordCracker(
        "because can do must we what".split(" "), "wedowhatwemustbecausewecan"
    )
)

print(
    passwordCracker(
        "a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa".split(" "),
        "aaaaaaaaaab",
    )
)

print(passwordCracker("ab abcd cd".split(" "), "abcd"))
