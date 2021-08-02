def get_cats_with_hats(array_of_cats):
    cats_with_hats = []
    for i in range(1,100 + 1):
        for cat in range(1,100 + 1):
            if cat % i == 0:
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True
    cats_with_hats = [n for n in range(0, len(array_of_cats)) if array_of_cats[n] is True]
    return cats_with_hats                  


cats = [False] * (100+1)
print(get_cats_with_hats(cats))

