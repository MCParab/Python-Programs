import sklearn import tree

#[height, wieght, shoe size]

X=[[180,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,70,43],[171,75,42],[181,85,43]]

y=['male', 'female','female','female','male','male','male','female','male','female','male']

clf=tree.DecisionTreeClassifier()
clf.fit(X,y)
prediction =clf.predict([190,70,43])
