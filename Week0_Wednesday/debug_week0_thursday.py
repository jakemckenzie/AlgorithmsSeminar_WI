import array as arr
v = arr.array([1,2,3,45,69,-3])
def debug_week0_thursday(vector):
    max,min = vector[0],vector[0];
    for elem in vector[1:]:
        if elem > max:
            max = elem
        if elem < min:
            min = elem
    print(str(min)+", " +str(max));
debug_week0_thursday(v)