let nums = [3, 6, 2, 1, 5, 4]

function bubble_sort(a) {
    for (let i = 0; i < a.length; i++) {
        for (let j = 0; j < (a.length - i - 1); j++) {
            if (a[j] > a[j+1]) {
                let swap = a[j]
                a[j] = a[j+1]
                a[j+1] = swap
            }
        }
    }
    return a
}

document.getElementById("unsorted").textContent += "Unsorted array: " + nums
document.getElementById("sorted").textContent += "Sorted array: " + bubble_sort(nums)