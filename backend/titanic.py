def learn(PassengerClass,No_siblings,No_children,female,male) :

    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier

    data=[{"PassC":PassengerClass,"Sib":No_siblings,"chi":No_children,"fem":female,"mal":male}]
    test=pd.DataFrame(data)
    train_data = pd.read_csv("C:/Users/alimo/Desktop/titanic/train.csv")
    y = train_data["Survived"]

    features = ["Pclass", "Sex", "SibSp", "Parch"]
    X = pd.get_dummies(train_data[features])
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X, y)
    predictions = model.predict(test)
    return(predictions[0])
