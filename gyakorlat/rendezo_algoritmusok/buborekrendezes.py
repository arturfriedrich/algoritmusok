# bubble sort
# https://www.youtube.com/watch?v=Vca808JTbI8


def bubble_sort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


nums = [3, 6, 2, 1, 5, 4]
print("Rendezetlen lista: ", nums)
bubble_sort(nums)
print("Rendezett lista: ", nums)
