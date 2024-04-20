import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

def partition(array, low, high):
    pivot = array[high]  # Pivot is the last element
    i = low
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i

def quick_sort(array, low, high, steps):
    if low < high:
        pi = partition(array, low, high)
        steps.append((array.copy(), pi))
        quick_sort(array, low, pi - 1, steps)
        quick_sort(array, pi + 1, high, steps)

def update_plot(data, pivot_idx):
    for i, (bar, height) in enumerate(zip(bars, data)):
        bar.set_height(height)
        if i == pivot_idx:
            bar.set_color('red')  # Color for pivot element
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f'Pivot: {height}', ha='center', va='bottom')
        elif i < pivot_idx:
            bar.set_color('pink')  # Color for sorted elements
        else:
            bar.set_color('dodgerblue')  # Color for unsorted elements
    plt.draw()

def next_step(event):
    global step
    if step < len(steps) - 1:
        step += 1
        update_plot(*steps[step])

def prev_step(event):
    global step
    if step > 0:
        step -= 1
        update_plot(*steps[step])

def sort_directly(event):
    global step
    step = len(steps) - 1
    update_plot(*steps[step])

# User input for array elements
arr = []
val = int(input("Enter number of values to sort :"))
while len(arr) < val:
    arr = list(map(int, input(f"Enter at least {val} elements of the array separated by spaces: ").split()))

x = []  # Generate x values for bars
for i in range(1, len(arr) + 1):
    x.append(i)

fig, ax = plt.subplots()
ax.set_title('Quick Sort Visualization')

# Create bars with input values as x tick labels
bars = plt.bar(x, arr, color='dodgerblue')  # Initial color for unsorted elements
plt.xticks(x, arr)  # Set x tick labels to input values
plt.xlim(0, max(x) + 1)
plt.ylim(0, max(arr) + 2)  # Increased y limit to accommodate pivot text
plt.yticks(range(0, max(arr) + 2))  # Increased y ticks to accommodate pivot text

# Adjust button positions
ax_next = plt.axes([0.6, 0.01, 0.1, 0.05])
ax_prev = plt.axes([0.4, 0.01, 0.1, 0.05])
ax_sort = plt.axes([0.5, 0.01, 0.1, 0.05])

btn_prev = Button(ax_prev, '<- Previous')
btn_next = Button(ax_next, 'Next ->')
btn_sort = Button(ax_sort, 'Final Sort')

btn_next.on_clicked(next_step)
btn_prev.on_clicked(prev_step)
btn_sort.on_clicked(sort_directly)

steps = []
quick_sort(arr, 0, len(arr) - 1, steps)

step = 0
update_plot(*steps[step])

plt.show()