from sklearn import linear_model
m, n = map(int, input('Enter number of observed features(M) and feature sets(N) : ').split())
X, Y = [], []
for i in range(n):
    x = [0]
    elements = list(map(float, input('Space-separated values of features (Decimals) : ').split()))
    for j in range(len(elements)):
        if j < m:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_
q = int(input('Enter number of feature seats to query : '))
new_X = []
for i in range(q):
    x = [0]
    elements = list(map(float, input('Space-separated values of m describing the feature sets(Decimals) : ').split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)
result = model.predict(new_X)
for i in range(len(result)):
    print("Value of Y would be : ", round(result[i],2))
