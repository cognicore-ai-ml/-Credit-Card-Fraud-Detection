import joblib
from xgboost import XGBClassifier
from dataloader import loaddata

def trainandsavemodel(datapath, model_path="model.pkl"):
    # Load training and test sets
    Xtrain, Xtest, ytrain, ytest = loaddata(datapath)

    # Initialize and train the model
    model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    model.fit(Xtrain, ytrain)

    # Save the trained model
    joblib.dump(model, model_path)
    print("✅ Model trained and saved as", model_path)

if __name__ == "__main__":
    trainandsavemodel("data/creditcard.csv")
