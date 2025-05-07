n = int(input("Please enter the matrix length: "))
mat = [[0 for j in range(n)] for i in range(n)] # Filling initial matrix with 0 for n*n matrix
counter = 1 # Counter to fill the numbers in matrix
top, left, bottom, right = 0,0, n-1, n-1 # Defining boundary of matrix (not visited)
while counter <= (n*n): #Stop when n*n matrix is filled
    for j in range(left, right + 1): #Move right
        if counter > n*n: break # Break the loop to preserve from additional element gathering
        mat[top][j] = counter
        counter += 1 #Counter: Element to fill in the matrix
    top += 1 #Restrict top boundary by 1
    for i in range(top, bottom + 1): #Move bottom
        if counter > n*n: break
        mat[i][right] = counter
        counter += 1
    right -= 1 #Restrict right boundary by 1
    for j in range(right, left - 1, -1): #Move left
        if counter > n*n: break
        mat[bottom][j] = counter
        counter += 1
    bottom -= 1 #Restrict bottom boundary by 1
    for i in range(bottom, top - 1, -1): #Move top
        if counter > n*n: break
        mat[i][left] = counter
        counter += 1
    left += 1 #Restrict left boundary by 1

print("Raw format: ", mat)

print("Printing in proper format: ")
#Printing in proper format
for i in range(n):
    formatted_str = ""
    for j in range(n):
        formatted_str += str(mat[i][j]) + "\t"
    print(formatted_str)    

