from sorting_algorithms import *
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim


def update_plot(arr, bars, iterations):
    for bar, val in zip(bars, arr):
        # update the height of bar each time arr changes
        bar.set_height(val)
    # update the number of iterations
    iterations[0] += 1
    # update text
    text.set_text('Number of operations: {}'.format(iterations[0]))

if __name__ == "__main__":
    # input array choices
    print('Do you want to enter your own array?\
    If no then an array of random values of length 50 will be taken(y/n): ')
    arr_choice = input()
    if arr_choice  == 'y' or arr_choice == 'Y':
        print('Enter array elements(space separated): ')
        arr = list(map(int, input().split()))
    elif arr_choice == 'n' or arr_choice == 'N':
        print('A list of random values between 1-50 is created')
        arr = list(range(1, 50))
        random.shuffle(arr)
        print('arr: {}'.format(arr))
        # set title and generator.
        print('Select the algorithm you want to visualize: ')
        print('s for selection sort')
        print('i for insertion sort')
        algo_choice = input()
        if algo_choice == 's':
            generator = selection_sort(arr)
            title = 'Selection Sort'
        elif algo_choice == 'i':
            generator = insertion_sort(arr)
            title = 'Insertion Sort'
            # visualization part begins here.
        # First create subplots.
        fig, ax = plt.subplots()
        # set the title
        ax.set_title(title)
        # set text, ax.transAxes sets the coordinates of the axis such that
        # bottom left: (0,0) & top-right: (1,1)
        text = ax.text(x=0.02, y=0.95,s="", transform=ax.transAxes)
        # configure the bar size and alignment.
        bars = ax.bar(x=range(len(arr)), height=arr, align='edge')
        # not a number but a list because list is passed as reference.
        # update plot
        iterations = [0]
        # Animation part
        animation = anim.FuncAnimation(fig, func=update_plot, 
        fargs=(bars, iterations), frames=generator, interval=1, repeat=False)
        plt.show()
    else:
        print('invalid input')
        input('Press Enter to exit... ')   



    