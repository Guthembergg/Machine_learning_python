from scipy.spatial import distance

A = [1, 2]
B = [4, 0]

A2 = [5, 4, 3]
B2 = [1, 7, 9]

# calcolo della distanza fra due liste di punti con la stessa dimensione usando la formula euclidea


def euclidean_distance(a, b):
    distance = 0

    for i in range(len(a)):
        distance = distance + (a[i] - b[i]) ** 2
    return distance**0.5


print(euclidean_distance(A2, B2))

# calcolo della distanza fra due liste di punti con la stessa dimensione usando la formula manhattan
# nota manhattan sarù sempre più lunga o uguale alla euclidea perchè non considera l'ipotenusa ma tutta la distanza


def manhattan_distance(pt1, pt2):
    distance = 0
    for i in range(len(pt1)):
        distance += abs(pt1[i]-pt2[i])
    return distance

print(manhattan_distance(A2, B2))

#Hamming distance is used in spell checking algorithms. For example, the Hamming distance between the word “there” and the typo “thete” is one. Each letter is a dimension, and each dimension has the same value except for one.
def hamming_distance(pt1 , pt2):
    distance = 0
    for i in range(len(pt1)):
      if pt1[i]!= pt2[i]:
        distance+=1
    return distance

print(hamming_distance([1,2],[1,100]))
print(hamming_distance([5,4,9],[1,7,9]))

print(euclidean_distance(A2, B2))
#usando la libreria scipy
print(distance.euclidean(A2,B2))
distance.euclidean([1,2],[4,0])
distance.cityblock([1,2],[4,0])
distance.hamming([5, 4, 9], [1, 7, 9])