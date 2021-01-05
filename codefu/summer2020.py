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


class RoboAdvisor:
    def calculateReturn(self, appl, tsla, zm, dividends):

        weekly_optimal = dividends[:]

        days = len(appl)

        daily_optimal = 0

        overall_gain = 0

        for i in range(days):
            weekly_optimal[0] += appl[i]
            weekly_optimal[1] += tsla[i]
            weekly_optimal[2] += zm[i]

            largest = max(appl[i], tsla[i], zm[i])
            if largest > 0:
                daily_optimal += largest

            if i and i % 5 == 4:
                week_gain = max(daily_optimal, max(weekly_optimal), 0)
                overall_gain += week_gain
                weekly_optimal = dividends[:]
                daily_optimal = 0

        return overall_gain


class Lego:

    def findNumberOfWays(self, w, h, lengths):
        mod = 1000007

        lengths.sort()

        dp = [0] * (w + 1)

        dp[0] = 1

        for i in range(1, w + 1):
            for l in lengths:
                if l > i:
                    break

                dp[i] = (dp[i] + dp[i - l]) % mod

        return (dp[w] ** h) % mod


if __name__ == '__main__':
    # print(CharMatcher().countMatches(["lyNLRl", "zOUDymfIu", "QidYNw", "UKHZIrXw", "GoFDteZodT", "cjRPTcfJHH"]))
    # print(RoboAdvisor().calculateReturn(
    #     [1, 3, -2, 3, 5, 1, 3, -2, 3, 5, 1, 3, -2, 3, 5, 1, 3, -2, 3, 5],
    #     [2, 4, -2, 4, 4, 2, 4, -2, 4, 4, 2, 4, -2, 4, 4, 2, 4, -2, 4, 4],
    #     [-1, 2, -3, 2, 1, -1, 2, -3, 2, 1, -1, 2, -3, 2, 1, -1, 2, -3, 2, 1],
    #     [1, 1, 1]))
    print(Lego().findNumberOfWays(157, 374, [159,2,259,356,134,41,10,394,210,216,281,127]))
