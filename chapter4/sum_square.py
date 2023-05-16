import numpy as np

def sum_square_error(y, t):
  return 0.5 * np.sum((y - t)**2)

def cross_entropy_error(y, t):
  if y.ndim == 1:
    t = t.reshape(1, t.size)
    y = y.reshape(1, y.size)
  batch_size = y.shape[0]
  delta = 1e-7
  return -np.sum(t * np.log(y[np.arange(batch_size), t] + delta)) / batch_size


if __name__ == "__main__":
  t1 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
  y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
  print(sum_square_error(np.array(y1), np.array(t1)))

  t2 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
  y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
  print(sum_square_error(np.array(y2), np.array(t2)))

  print("考査エントロピー誤差")
  print(cross_entropy_error(np.array(y1), np.array(t1)))
  print(cross_entropy_error(np.array(y2), np.array(t2)))