import json
from dataset import *

training_file_name = "training_data.jsonl"
caa_file_name = "caa_data.jsonl"
validation_file_name = "validation_data.jsonl"


def prepare_date(dic_update, final_file_name):
    with open(final_file_name, 'w') as outfile:
        for entry in dic_update:
            json.dump(entry, outfile)
            outfile.write('\n')


prepare_date(training_data, "training_data.jsonl")
prepare_date(caa_training_data, "caa_data.jsonl")
prepare_date(validation_data, "validation_data.jsonl")


# ft-492Cr9PFlSQCuue5jsBKlknD