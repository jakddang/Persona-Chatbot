import logging

import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from pre_defined_tokens import *
from transformers import AutoTokenizer
from torch.utils.data import Dataset, DataLoader

import urllib.request

U_TKN = "<usr>"
S_TKN = "<sys>"
BOS = "</s>"
EOS = "</s>"
MASK = "<unused0>"
SENT = "<unused1>"
PAD = "<pad>"


def download_ko_dataset(path: str, download=False, file_name="kor_chatbot.csv"):
    # download dataset
    if download:
        urllib.request.urlretrieve(path, filename=file_name)
    return None


class ChatbotDataset(Dataset):
    def __init__(self, path: str, model_name: str, max_len: int = 32):
        self.data = pd.read_csv(path)
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            bos_token=BOS,
            eos_token=EOS,
            unk_token="<unk>",
            pad_token=PAD,
            mask_token=MASK,
        )
        self.first = True
        self.q_token = U_TKN
        self.a_token = S_TKN
        self.sent_token = SENT
        self.bos = BOS
        self.eos = EOS
        self.mask = MASK
        self.pad = PAD
        self.max_len = max_len

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx: int) -> tuple:
        # return (self.data["Q"][idx], self.data["A"][idx], self.data["label"][idx])
        utterance = self.data.iloc[idx]
        # question
        q = utterance["Q"]
        a = utterance["A"]
        label = str(utterance["label"])
        tokenized_q = self.tokenizer.tokenize(
            self.q_token + q + self.sent_token + label
        )
        q_len = len(tokenized_q)
        tokenized_a = self.tokenizer.tokenize(self.a_token + a + self.eos)
        a_len = len(tokenized_a)
        if q_len + a_len > self.max_len:
            a_len = self.max_len - q_len
            if a_len <= 0:
                tokenized_q = tokenized_q[-(int(self.max_len / 2)) :]
                q_len = len(tokenized_q)
                a_len = self.max_len - q_len
                assert a_len > 0
            tokenized_a = tokenized_a[:a_len]
            a_len = len(tokenized_a)
            assert a_len == len(tokenized_a), f"{a_len} ==? {len(tokenized_a)}"

        labels = [self.mask] * q_len + tokenized_a[1:]

        if self.first:
            logging.info("contexts : {}".format(q))
            logging.info("toked ctx: {}".format(tokenized_q))
            logging.info("response : {}".format(a))
            logging.info("toked response : {}".format(tokenized_a))
            logging.info("labels {}".format(labels))
            self.first = False
        mask = [0] * q_len + [1] * a_len + [0] * (self.max_len - q_len - a_len)
        self.max_len
        labels_ids = self.tokenizer.convert_tokens_to_ids(labels)
        while len(labels_ids) < self.max_len:
            labels_ids += [self.tokenizer.pad_token_id]
        token_ids = self.tokenizer.convert_tokens_to_ids(tokenized_q + tokenized_a)
        while len(token_ids) < self.max_len:
            token_ids += [self.tokenizer.pad_token_id]
        return (token_ids, np.array(mask), labels_ids)


if __name__ == "__main__":
    path = (
        "https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv"
    )
    download_ko_dataset(path, download=False, file_name="kor_chatbot.csv")
    dataset = ChatbotDataset("ko_chatbot.csv", "skt/kogpt2-base-v2")
    dl = DataLoader(dataset, shuffle=True)
    q, a, label = next(iter(dl))
    print(q)
    print(a)
    print(label)
