
for i in range(1, 1000000):
    print(i)
    num = sorted([x for x in str(i)])
    num_2x = sorted([x for x in str(i*2)])

    if num == num_2x:
        num_3x = sorted([x for x in str(i*3)])

        if num_2x == num_3x:
            num_4x = sorted([x for x in str(i*4)])

            if num_3x == num_4x:
                num_5x = sorted([x for x in str(i*5)])

                if num_4x == num_5x:
                    num_6x = sorted([x for x in str(i*6)])

                    if num_5x == num_6x:
                        print(i)
                        break