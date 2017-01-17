from sys import maxint


class MaxSubArray(object):
  def find_max_sub_array(self, data_list):
    return self._find_max_sub_array(data_list, 0, len(data_list) - 1)

  def _find_max_sub_array_local(self, data_list, low, high, index):
    sum = 0
    left_low = index
    left_sum_max = -maxint - 1
    for id in xrange(index, low - 1, -1):
      sum += data_list[id]
      if sum > left_sum_max:
        left_sum_max = sum
        left_low = id

    sum = 0
    right_high = index + 1
    right_sum_max = -maxint - 1
    for id in range(index + 1, high + 1):
      sum += data_list[id]
      if sum > right_sum_max:
        right_sum_max = sum
        right_high = id

    return left_low, right_high, left_sum_max + right_sum_max

  def _find_max_sub_array(self, data_list, low, high):
    if low == high:
      return low, low, data_list[low]

    mid = (low + high) / 2

    local_low, local_high, local_max = self._find_max_sub_array_local(
      data_list, low, high, mid)
    low_left, high_left, max_left = self._find_max_sub_array(
      data_list, low, mid)
    low_right, high_right, max_right = self._find_max_sub_array(
      data_list, mid + 1, high)

    if local_max >= max_left and local_max >= max_right:
      return local_low, local_high, local_max

    if max_left >= local_max and max_left >= max_right:
      return low_left, high_left, max_left

    return low_right, high_right, max_right


if __name__ == "__main__":
  max_sub = MaxSubArray()
  data_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  low, high, max = max_sub.find_max_sub_array(data_list)
  print low, high, max
