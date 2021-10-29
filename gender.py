from sklearn import tree

# [height, weight, shoe size]
characteristic = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47],
                  [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43],
                  ]

idetifiers = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male',
              'female', 'male']

clf = tree.DecisionTreeClassifier()

clf.fit(characteristic, idetifiers)

user_input = []
while len(user_input) < 3:
    print("Please enter the person's height, then weight, then shoe size")
    user_input.append(int(input()))

prediction = clf.predict([user_input])

print(prediction)
