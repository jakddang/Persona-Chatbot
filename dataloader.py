import torch
import torch.nn as nn
import pandas as pd

from torch.utils.data import Dataset, DataLoader
from kogpt2_transformers import get_kogpt2_tokenizer
from kobert_transformers import get_tokenizer
import urllib.request


def download_ko_dataset(path: str):
    # download dataset
    urllib.request.urlretrieve(path, filename="kor_chatbot.csv")
    return None


class ChatbotDataset(Dataset):
    def __init__(self, path: str):
        self.data = pd.read_csv(path)
        self.tokenizer = get_kogpt2_tokenizer
        self.data = []

        # bos_token_id = list(self.tokenizer.bos_token_id)
        # eos_token_id = list(self.tokenizer.eos_token_id)
        # pad_token_id = list(self.tokenizer.pad_token_id)

    def __len__(self):
        return len(self.data["label"])

    def __getitem__(self, idx):
        return (self.data["Q"][idx], self.data["A"][idx], self.data["label"][idx])


if __name__ == "__main__":
    path = (
        "https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv"
    )
    # download_ko_dataset(path)
    dataset = ChatbotDataset("ko_chatbot.csv")
    # print(pd.read_csv('ko_chatbot.csv')['Q'])
    dl = DataLoader(dataset, shuffle=True)
    q, a, label = next(iter(dl))
    print(q)
    print(a)
    print(label)
