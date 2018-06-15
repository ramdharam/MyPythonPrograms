## write a util function (i , j , matrix )

# 1. if matrix[i][j] == dest  -> return True
# 2. if matrix[i][j] out of limits -> return
# 3. repeat this process for
#           [i+1][j]
#           [i-1][j]
#           [i][j+1]
#           [i][j-1]