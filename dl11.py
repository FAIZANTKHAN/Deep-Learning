import numpy as np

y_predicted = np.array([1, 1, 0, 0, 1])
y_true = np.array([0.30, 0.7, 1, 0, 0.5])


# Mean Absolute Error
def mae(y_true, y_predicted):
    total_error = 0
    for yt, yp in zip(y_true, y_predicted):
        total_error += abs(yt - yp)
    print("Total error:", total_error)
    mae = total_error / len(y_true)
    print("MAE:", mae)
    return mae


print(mae(y_true, y_predicted))

# Or(using numpy )
print(np.mean(np.abs(y_predicted - y_true)))

# Implement Log Loss or Binary Cross Entropy

epsilon = 1e-15


def log_loss(y_true, y_predicted):
    y_predicted_new = [max(i, epsilon) for i in y_predicted]
    y_predicted_new = [min(i, 1 - epsilon) for i in y_predicted_new]
    y_predicted_new = np.array(y_predicted_new)
    return -np.mean(y_true * np.log(y_predicted_new) + (1 - y_true) * np.log(1 - y_predicted_new))


print(log_loss(y_true, y_predicted))


# Mean Squared Error
def mse(y_true, y_predicted):
    total_error = 0
    for yt, yp in zip(y_true, y_predicted):
        total_error += (yt - yp) ** 2
    print("Total Squared Error:", total_error)
    Mse = total_error / len(y_true)
    print("Mean Squared Error:", Mse)
    return Mse

print(mse(y_true,y_predicted))

#Or(with numpy)
print(np.mean(np.square(y_true-y_predicted)))
