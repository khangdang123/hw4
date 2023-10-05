def cacti_number(func):
    def wrapper(arr):
        rows = len(arr)
        cols = len(arr[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 0:
                    if (i == 0 or arr[i-1][j] == 0) and \
                       (i == rows-1 or arr[i+1][j] == 0) and \
                       (j == 0 or arr[i][j-1] == 0) and \
                       (j == cols-1 or arr[i][j+1] == 0) and \
                       (i == 0 or j == 0 or arr[i-1][j-1] == 0) and \
                       (i == 0 or j == cols-1 or arr[i-1][j+1] == 0) and \
                       (i == rows-1 or j == 0 or arr[i+1][j-1] == 0) and \
                       (i == rows-1 or j == cols-1 or arr[i+1][j+1] == 0):
                        arr[i][j] = 1
                        count += 1
        return count
    return wrapper
    
