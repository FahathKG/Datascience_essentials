# Linear Regression

# import linear regression from sklearn

from sklearn.linear_model import LinearRegression
lreg = LinearRegression()

from sklearn.model_selection import train_test_split
x_train, x_cv, y_train, y_cv = train_test_split(df[x-variables],dfp[y-variable], test_size=0.2)

# training a linear regression model on training data
lreg.fit(x_train,y_train)

# predicting on cv
pred_cv = lreg.predict(x_cv)

# calculating mse
mse = np.mean((pred_cv-y_cv)**2)

# evaluation using R-Square
lreg.score(x_cv,y_cv)