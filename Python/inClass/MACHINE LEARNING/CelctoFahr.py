import pandas as pd

# Define the values of x and y
x = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = pd.Series([32, 33.8, 35.6, 37.4, 39.2, 41, 42.8, 44.6, 46.4, 48.2])

# Calculate the means of x and y
mean_x = x.mean()
mean_y = y.mean()

# Calculate the intermediate columns
x_minus_mean_x = x - mean_x
y_minus_mean_y = y - mean_y
x_minus_mean_x_sq = x_minus_mean_x ** 2
y_minus_mean_y_sq = y_minus_mean_y ** 2
x_minus_mean_x_y_minus_mean_y = x_minus_mean_x * y_minus_mean_y

# Calculate slope (m) and intercept (c) for the linear regression line
m = sum(x_minus_mean_x_y_minus_mean_y) / sum(x_minus_mean_x_sq)
c = mean_y - m * mean_x

# Create the DataFrame
df = pd.DataFrame({
    'x': x,
    'y': y,
    'x - mean(x)': x_minus_mean_x,
    'y - mean(y)': y_minus_mean_y,
    '(x - mean(x))^2': x_minus_mean_x_sq,
    '(y - mean(y))^2': y_minus_mean_y_sq,
    '(x - mean(x))(y - mean(y))': x_minus_mean_x_y_minus_mean_y,
})

# Add the calculated m and c values to the DataFrame
df['m'] = m
df['c'] = c

# Print the DataFrame
print(df)

df.to_excel('CeltoFahr.xlsx', index=False)