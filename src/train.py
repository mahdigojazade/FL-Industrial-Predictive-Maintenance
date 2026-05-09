import torch
import torch.nn as nn


def train_model(model, loader, epochs=5):

    criterion = nn.BCELoss()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001
    )

    for epoch in range(epochs):

        total_loss = 0

        for X_batch, y_batch in loader:

            optimizer.zero_grad()

            outputs = model(X_batch).squeeze()

            loss = criterion(outputs, y_batch)

            loss.backward()

            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")