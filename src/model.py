import torch.nn as nn


class Net(nn.Module):

    def __init__(self):

        super(Net, self).__init__()

        self.model = nn.Sequential(

            nn.Linear(21, 64),
            nn.ReLU(),

            nn.Linear(64, 32),
            nn.ReLU(),

            nn.Linear(32, 1),
            nn.Sigmoid()
        )

    def forward(self, x):

        return self.model(x)