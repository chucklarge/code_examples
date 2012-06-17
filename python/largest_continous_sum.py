def largestContinuousSum(arr):
    if len(arr)==0:
        return
    maxSum=currentSum=arr[0]
    for num in arr[1:]:
        currentSum=max(currentSum+num, num)
        maxSum=max(currentSum, maxSum)
    return maxSum

def main ():
    a = [9, 3, 4, -100, 3, 4, 8, 2]
    largest = largestContinuousSum(a)
    print largest

if __name__== "__main__":
  main()
