weight, height = map(float, input("введите ваши параметры тела через пробел вес и рост").split())
imt = weight / (height * height)
print(round(imt, 1))
