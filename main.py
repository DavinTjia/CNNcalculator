# take a user input of dimension of the image

def takeInput():
    res = input()
    # check if the input is an integer
    if res == 'r' or res == 'R':
        return res
    while not res.isdigit():
        print("Invalid input. Please enter an integer")
        res = input()
    return int(res)

def isReenter(input):
    if input == 'r' or input == 'R':
        return -1
    else:
        return 1

def main():
    progress = 0
    # take user input
    # print("Enter the dimension of the image")
    # print("Enter the width of the image")
    # width = takeInput()
    # print("Enter the height of the image")
    # height = takeInput()
    # print("Enter the number of channels of the image")
    # channels = takeInput()

    # initialize width, height and channels
    width, height, channels = 0, 0, 0

    while progress < 3:
        if progress == 0:
            print("Enter the width of the image")
            width = takeInput()
            progress += isReenter(width)
        elif progress == 1:
            print("Enter the height of the image")
            height = takeInput()
            progress += isReenter(height)
        elif progress == 2:
            print("Enter the number of channels of the image")
            channels = takeInput()
            progress += isReenter(channels)


    prev_width = width
    prev_height = height
    prev_channels = channels

    toTerminate = False
    while not toTerminate:
        print("(C)onvolution or (P)ooling or (R)evert or (T)erminate")
        print("Current dimension: " + str(width) + "x" + str(height) + "x" + str(channels))
        choice = input().upper()

        if choice == 'C':
            # ask for input channels size, output channels size, kernel size
            # , stride, and padding
            # print("Enter the number of input channels")
            # input_channels = takeInput()
            # print("Enter the number of output channels")
            # output_channels = takeInput()
            # print("Enter the kernel size")
            # kernel_size = takeInput()
            # print("Enter the stride")
            # stride = takeInput()
            # print("Enter the padding")
            # padding = takeInput()

            # intialize input channels, output channels, kernel size, stride, and padding
            output_channels, kernel_size, stride, padding = 1, 1, 1, 0

            progress = 0
            while progress < 5:
                if progress == 0:
                    print("Enter the number of input channels")
                    input_channels = takeInput()
                    progress += isReenter(input_channels)
                elif progress == 1:
                    print("Enter the number of output channels")
                    output_channels = takeInput()
                    progress += isReenter(output_channels)
                elif progress == 2:
                    print("Enter the kernel size")
                    kernel_size = takeInput()
                    progress += isReenter(kernel_size)
                elif progress == 3:
                    print("Enter the stride")
                    stride = takeInput()
                    progress += isReenter(stride)
                elif progress == 4:
                    print("Enter the padding")
                    padding = takeInput()
                    progress += isReenter(padding)

            # calculate the output width size
            output_width = int((width - kernel_size + 2*padding)/stride) + 1
            # calculate the output height size
            output_height = int((height - kernel_size + 2*padding)/stride) + 1
            # calculate the output channels size
            output_channels = output_channels

            # print the output
            print("Output dimension: " + str(output_width) + "x" + str(output_height) + "x" + str(output_channels))

            # save the previous and update the width, height, and channels
            prev_width = width
            prev_height = height
            prev_channels = channels

            width = output_width
            height = output_height
            channels = output_channels
        elif choice == 'P':
            # initialize the kernel size, stride, and padding
            kernel_size, stride, padding = 1, 1, 0

            progress = 0
            while progress < 3:
                if progress == 0:
                    print("Enter the kernel size")
                    kernel_size = takeInput()
                    progress += isReenter(kernel_size)
                elif progress == 1:
                    print("Enter the stride")
                    stride = takeInput()
                    progress += isReenter(stride)
                elif progress == 2:
                    print("Enter the padding")
                    padding = takeInput()
                    progress += isReenter(padding)

            # # ask for kernel size, stride, and padding
            # print("Enter the kernel size")
            # kernel_size = takeInput()
            # print("Enter the stride")
            # stride = takeInput()
            # print("Enter the padding")
            # padding = takeInput()

            # calculate the output width size
            output_width = int((width - kernel_size + 2*padding)/stride) + 1
            # calculate the output height size
            output_height = int((height - kernel_size + 2*padding)/stride) + 1
            # calculate the output channels size
            output_channels = channels

            # print the output
            print("Output dimension: " + str(output_width) + "x" + str(output_height) + "x" + str(output_channels))


            # save the previous and update the width, height, and channels
            prev_width = width
            prev_height = height
            prev_channels = channels

            # update the width, height, and channels
            width = output_width
            height = output_height
            channels = output_channels
        elif choice == 'R':
            # revert the width, height, and channels
            width = prev_width
            height = prev_height
            channels = prev_channels

            # print the output
            print("Reset Output dimension To: " + str(width) + "x" + str(height) + "x" + str(channels))
        elif choice == 'T':
            toTerminate = True
        else:
            print("Invalid input")



# call the main function
if __name__ == "__main__":
    main()


