"""
AES-128 brute force cost - exercises 1 to 4

Assumptions:
  - Work factor to test one key: 1200 elementary instructions
  - Machine speed: 2000 Mips
  - Key length: 128 bits
  - All keys are equally probable
"""

from fractions import Fraction

# ---------------------------------------------------------------
# Given values
# ---------------------------------------------------------------
WORK_FACTOR = 1200          # elementary instructions per key tested
MIPS = 2000                 # Mips = millions (10^6) of instructions per second
KEY_BITS = 128              # key length in bits
NB_COMPUTERS = 10**9        # one billion computers on the Internet

SECONDS_PER_YEAR = 365.25 * 24 * 3600   # about 3.156e7 seconds
UNIVERSE_AGE_YEARS = 1.38e10            # for comparison only

# ---------------------------------------------------------------
# 1. Time needed to test a single key
# ---------------------------------------------------------------
# Careful: the whole denominator must be parenthesised.
#   1200 / 2 * 10**9   -> (1200/2) * 10^9  (wrong)
#   1200 / (2 * 10**9) -> 6e-7             (correct)
instructions_per_second = MIPS * 10**6          # 2000 * 10^6 = 2 * 10^9
time_per_key = WORK_FACTOR / instructions_per_second

# ---------------------------------------------------------------
# 2. Number of possible keys
# ---------------------------------------------------------------
# Each additional bit doubles the number of cases -> 2^128
nb_keys = 2 ** KEY_BITS

# ---------------------------------------------------------------
# 3. Average number of keys tested before finding the right one
# ---------------------------------------------------------------
# If the correct key sits in position k, exactly k tests are needed,
# so we average 1, 2, ..., n:
#   (1 + 2 + ... + n) / n = [n(n+1)/2] / n = (n+1)/2
def average_tests(n: int) -> Fraction:
    """Average number of tests for n equally probable keys.

    Fraction keeps the exact value: with floats the trailing 0.5 would be
    lost to rounding, since 2^128 is far beyond float precision.
    """
    return Fraction(n + 1, 2)


avg_tests = average_tests(nb_keys)          # 2^127 + 0.5
avg_tests_approx = 2 ** (KEY_BITS - 1)      # 2^127, the usual approximation

# Sanity checks on small cases: 4 keys -> 2.5, a 6-sided die -> 3.5
assert average_tests(4) == Fraction(5, 2)
assert average_tests(6) == Fraction(7, 2)

# ---------------------------------------------------------------
# 4. Average computation time
# ---------------------------------------------------------------
avg_time_1_computer = float(avg_tests) * time_per_key          # seconds
avg_time_1_billion = avg_time_1_computer / NB_COMPUTERS        # seconds


def to_years(seconds: float) -> float:
    """Convert a duration in seconds into years."""
    return seconds / SECONDS_PER_YEAR


# ---------------------------------------------------------------
# Results
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("[1] Time to test one key")
    print(f"    {WORK_FACTOR} / (2 x 10^9) = {time_per_key:.3e} s "
          f"= {time_per_key * 1e6:.1f} microseconds\n")

    print("[2] Number of possible keys")
    print(f"    2^{KEY_BITS} = {nb_keys:.6e}".replace("e+", " x 10^"))
    print(f"    (exact value: {nb_keys})\n")

    print("[3] Average number of tests")
    print(f"    (n+1)/2 = 2^127 + 0.5 ~= {float(avg_tests):.4e}")
    print(f"    check - 4 keys      : {float(average_tests(4))}")
    print(f"    check - 6-sided die : {float(average_tests(6))}\n")

    print("[4] Average computation time")
    print(f"    single computer      : {avg_time_1_computer:.3e} s "
          f"= {to_years(avg_time_1_computer):.2e} years")
    print(f"    one billion computers: {avg_time_1_billion:.3e} s "
          f"= {to_years(avg_time_1_billion):.2e} years")

    ratio = to_years(avg_time_1_billion) / UNIVERSE_AGE_YEARS
    print(f"\n    Even with a billion computers this is about {ratio:.2e} "
          f"times the age of the universe.")