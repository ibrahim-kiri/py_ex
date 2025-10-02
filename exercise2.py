def cur_prev_number():

    print("Printing current and previous number and their sum in range(10)")

    prev_num = 0

    # loop from 1 to 10
    for i in range(1, 11):
        
        x_sum = prev_num + i
        print("Current Number", i, "Previous Number", prev_num, "Sum: ", x_sum)

        # modify previous number
        # set it to the current number
        prev_num = i
        

res = cur_prev_number()

