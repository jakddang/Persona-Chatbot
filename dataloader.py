import torch
import torch.nn as nn
import pandas as pd

from torch.utils.data import Dataset, DataLoader
from kogpt2_transformers import get_kogpt2_tokenizer
from kobert_transformers import get_tokenizer
import urllib.request


def download_ko_dataset(path: str, download=False, file_name="kor_chatbot.csv"):
    # download dataset
    if download:
        urllib.request.urlretrieve(path, filename=file_name)
    return None


class ChatbotDataset(Dataset):
    def __init__(self, path: str):
        self.data = pd.read_csv(path)
        self.tokenizer = get_kogpt2_tokenizer

    def __len__(self):
        return len(self.data["label"])

    def __getitem__(self, idx: int) -> tuple:
        return (self.data["Q"][idx], self.data["A"][idx], self.data["label"][idx])


if __name__ == "__main__":
    path = (
        "https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv"
    )
    download_ko_dataset(path, download=True, file_name="kor_chatbot.csv")
    dataset = ChatbotDataset("ko_chatbot.csv")
    dl = DataLoader(dataset, shuffle=True)
    q, a, label = next(iter(dl))
    print(q)
    print(a)
    print(label)
