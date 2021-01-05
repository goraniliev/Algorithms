class CharMatcher:
    def countMatches(self, a):
        n = len(a)
        cnt = 0

        for i in range(n):
            for j in range(i + 1, n):
                smaller_len = min(len(a[i]), len(a[j]))
                for k in range(smaller_len):
                    if a[i][k] == a[j][k]:
                        cnt += 1

        return cnt

if __name__ == '__main__':
    print(CharMatcher().countMatches(["lyNLRl", "zOUDymfIu", "QidYNw", "UKHZIrXw", "GoFDteZodT", "cjRPTcfJHH"]))
