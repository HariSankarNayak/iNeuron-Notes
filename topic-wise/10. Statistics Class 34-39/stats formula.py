import math
import numpy as np
from scipy.stats import norm, binom, poisson, expon

# ================================
# 🟢 BEGINNER LEVEL
# ================================

# Mean (Average)
def mean(data):
    return sum(data) / len(data)
# Average of data

# Population Variance
def population_variance(data):
    mu = mean(data)
    return sum((x - mu) ** 2 for x in data) / len(data)
# Spread of population data

# Sample Variance
def sample_variance(data):
    mu = mean(data)
    return sum((x - mu) ** 2 for x in data) / (len(data) - 1)

# Standard Deviation
def std_dev(data):
    return math.sqrt(population_variance(data))

# Range
def data_range(data):
    return max(data) - min(data)


# ================================
# 🟡 INTERMEDIATE LEVEL
# ================================

# Z-score
def z_score(x, mu, sigma):
    return (x - mu) / sigma
# Standardizes value

# Normal PDF
def normal_pdf(x, mu, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# Normal CDF
def normal_cdf(x, mu, sigma):
    return norm.cdf(x, mu, sigma)

# Covariance
def covariance(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    return sum((xi - mean_x)*(yi - mean_y) for xi, yi in zip(x, y)) / len(x)

# Pearson Correlation
def correlation(x, y):
    return np.corrcoef(x, y)[0,1]

# Standard Error
def standard_error(sigma, n):
    return sigma / math.sqrt(n)

# Z-test statistic
def z_test(sample_mean, population_mean, sigma, n):
    return (sample_mean - population_mean) / (sigma / math.sqrt(n))


# ================================
# 🔴 ADVANCED LEVEL
# ================================

# Bernoulli Distribution
def bernoulli(p, x):
    return p if x == 1 else (1 - p)

# Binomial Distribution
def binomial_prob(n, k, p):
    return binom.pmf(k, n, p)

# Poisson Distribution
def poisson_prob(lmbda, k):
    return poisson.pmf(k, lmbda)

# Exponential Distribution
def exponential_pdf(x, lmbda):
    return lmbda * math.exp(-lmbda * x)

# Chebyshev Inequality Bound
def chebyshev(k):
    return 1 / (k ** 2)

# Log-Normal (using numpy)
def log_normal(data):
    return np.log(data)

# Skewness
def skewness(data):
    mu = mean(data)
    sigma = std_dev(data)
    n = len(data)
    return sum(((x - mu)/sigma)**3 for x in data) / n

# Kurtosis
def kurtosis(data):
    mu = mean(data)
    sigma = std_dev(data)
    n = len(data)
    return sum(((x - mu)/sigma)**4 for x in data) / n

# Confidence Interval (Z)
def confidence_interval(mean, sigma, n, z=1.96):
    margin = z * (sigma / math.sqrt(n))
    return (mean - margin, mean + margin)

# t-test statistic
def t_test(sample_mean, population_mean, s, n):
    return (sample_mean - population_mean) / (s / math.sqrt(n))


# ================================
# 🔥 EXAMPLE USAGE
# ================================

data = [2, 4, 6, 8, 10]

print("Mean:", mean(data))
print("Variance:", population_variance(data))
print("Std Dev:", std_dev(data))
print("Z-score:", z_score(8, mean(data), std_dev(data)))
print("Binomial P(X=3):", binomial_prob(10, 3, 0.5))
print("Poisson P(X=2):", poisson_prob(3, 2))
print("Confidence Interval:", confidence_interval(mean(data), std_dev(data), len(data)))