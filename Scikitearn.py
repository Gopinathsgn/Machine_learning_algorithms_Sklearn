from sklearn.tree import tree
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

sgn1 = tree.DecisionTreeClassifier()

sgn2 = LogisticRegression()

sgn3 = GaussianNB()

sgn4 = RandomForestClassifier()

sgn5 = KNeighborsClassifier()

sgn6 = SVC(kernel="linear", C=0.025,random_state=101)

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],[177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male',
     'male', 'female', 'female', 'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
sgn1 = sgn1.fit(X, Y)
sgn2 = sgn2.fit(X, Y)
sgn3 = sgn3.fit(X, Y)
sgn4 = sgn4.fit(X, Y)
sgn5 = sgn5.fit(X, Y)
sgn6 = sgn6.fit(X, Y)

prediction = sgn1.predict([[190, 70, 43]])
prediction2 = sgn2.predict([[190, 70, 43]])
prediction3 = sgn3.predict([[190, 70, 43]])
prediction4 = sgn4.predict([[190, 70, 43]])
prediction5 = sgn5.predict([[190, 70, 43]])
prediction6 = sgn6.predict([[190, 70, 43]])

print(prediction)
print(prediction2)
print(prediction3)
print(prediction4)
print(prediction5)
print(prediction6)
