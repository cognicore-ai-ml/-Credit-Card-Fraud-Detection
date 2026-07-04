import joblib
from sklearn.metrics import classification_report, roc_auc_score
from dataloader import loaddata

def evaluate_model(datapath, model_path="model.pkl"):
    # Load test data
    Xtrain, Xtest, ytrain, ytest = loaddata(datapath)

    # Load the trained model
    model = joblib.load(model_path)

    # Make predictions
    y_pred = model.predict(Xtest)

    # Print evaluation metrics
    print("📊 Classification Report:")
    print(classification_report(ytest, y_pred))
    print("ROC-AUC Score:", roc_auc_score(ytest, y_pred))

if __name__ == "__main__":
    evaluate_model("data/creditcard.csv")
