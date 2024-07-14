import pandas as pd

# Step 1: Create the `x` and `y` columns
x = list(range(1, 11))
y = [32, 33.8, 35.6, 37.4, 39.2, 41, 42.8, 44.6, 46.4, 48.2]

# Step 2: Calculate the mean of `x` and `y`
mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

# Step 3: Compute the required columns
x_minus_mean_x = [xi - mean_x for xi in x]
y_minus_mean_y = [yi - mean_y for yi in y]
x_minus_mean_x_squared = [(xi - mean_x) ** 2 for xi in x]
y_minus_mean_y_squared = [(yi - mean_y) ** 2 for yi in y]
xy_minus_mean_product = [(xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)]

# Step 4: Calculate the slope m
sum_xy_product = sum(xy_minus_mean_product)
sum_x_squared = sum(x_minus_mean_x_squared)
m = sum_xy_product / sum_x_squared

# Step 5: Calculate the y-intercept c
c = mean_y - m * mean_x

# Step 6: Combine everything into a table and add the slope m and y-intercept c as constant columns
data = {
    'x': x,
    'y': y,
    'x-mean(x)': x_minus_mean_x,
    'y-mean(y)': y_minus_mean_y,
    '(x-mean(x))**2': x_minus_mean_x_squared,
    '(y-mean(y))**2': y_minus_mean_y_squared,
    '(x-mean(x))(y-mean(y))': xy_minus_mean_product,
    'm': [m] * len(x),
    'c': [c] * len(x)
}

df = pd.DataFrame(data)
print(df)
