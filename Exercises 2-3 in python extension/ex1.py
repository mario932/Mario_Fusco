import math

def calculate_series(x, n):
    series_terms = []
    for i in range(n):
        term = x**i / math.factorial(i)
        series_terms.append(term)
    return series_terms

x_value = int(input('insert x_value: '))
num_terms = int(input('insert n_value: '))

if __name__ == '__main__':
    print("Script is running directly")
    calculate_series(x_value,num_terms)


    # Calculate the first N terms of the series for e^x
    series_terms_array = calculate_series(x_value, num_terms)
    print(f"The first {num_terms} terms of the series for e^{x_value} are: {series_terms_array}")
    
    # Calculate sum of the series
    sum_of_series = sum(series_terms_array)
    print(f"The sum of the series for e^{x_value} is: {sum_of_series}")

