import torch

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def evaluate_model(model, loader):

    y_true = []
    y_pred = []

    with torch.no_grad():

        for X_batch, y_batch in loader:

            outputs = model(X_batch).squeeze()

            predicted = (outputs > 0.5).float()

            y_true.extend(y_batch.numpy())

            y_pred.extend(predicted.numpy())

    accuracy = accuracy_score(y_true, y_pred)

    precision = precision_score(y_true, y_pred)

    recall = recall_score(y_true, y_pred)

    f1 = f1_score(y_true, y_pred)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")