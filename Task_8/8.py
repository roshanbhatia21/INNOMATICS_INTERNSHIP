import statistics as st
def correlation_coefficient(n, dt_x, dt_y):
    mean_x = st.mean(dt_x)
    mean_y = st.mean(dt_y)
    std_x = st.pstdev(dt_x)
    std_y = st.pstdev(dt_y)
    c = 0
    for i in range(n):
        c = c + (dt_x[i] - mean_x) * (dt_y[i] - mean_y)
    return c / (n * std_x * std_y)