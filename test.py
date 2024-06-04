# -*- coding: utf-8 -*-
"""Test script for jingyu_tsao_question_1.py"""

import pandas as pd
from main import process_file

if __name__ == "__main__":
    file_path = "./test_input_question_1.txt"
    df = process_file(file_path)
    print(df)
