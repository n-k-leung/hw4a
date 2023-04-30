def cacti_number(arr):

   count=0
   for i in range (len(arr)):
     for j in range (len(arr[0])):

       notNextTo = True
       if arr[i][j] == 0 :
            if (i > 0 and arr[i-1][j] != 0):
                notNextTo = False
            elif (i < len(arr) - 1 and arr[i+1][j] != 0):
                notNextTo = False
            elif (j > 0 and arr[i][j-1] != 0):
                notNextTo = False
            elif (j < len(arr[0]) - 1 and arr[i][j+1] != 0):
                notNextTo = False

            if notNextTo == True:
                arr[i][j] = 1;
                count = count + 1;

   return count
