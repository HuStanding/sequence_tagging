import pandas as pd
import codecs

INPUT_TRAIN_DATA = "data/CoNLL-2003/train.txt"
INPUT_DEV_DATA = "data/CoNLL-2003/dev.txt"
INPUT_TEST_DATA = "data/CoNLL-2003/test.txt"

OUT_TRAIN_DATA = "data/train.txt"
OUT_DEV_DATA = "data/dev.txt"
OUT_TEST_DATA = "data/test.txt"

TAGS_DATA = "data/tags.txt"

def convert(input_file, out_file):
    with codecs.open(input_file, "r")  as infile:
        with codecs.open(out_file, "w") as outfile:
            inlines = infile.readlines()
            for line in inlines:
                line = line.split()
                if line:
                    outfile.writelines(line[0] + " " + line[-1] + "\n")
                else:
                    outfile.writelines("\n")


if __name__ == "__main__":
    convert(INPUT_TRAIN_DATA, OUT_TRAIN_DATA)
    convert(INPUT_DEV_DATA, OUT_DEV_DATA)
    convert(INPUT_TEST_DATA, OUT_TEST_DATA)
