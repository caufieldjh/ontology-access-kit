import os
import pprint
from pathlib import Path

ROOT = os.path.abspath(os.path.dirname(__file__))
INPUT_DIR = Path(ROOT) / 'input'
OUTPUT_DIR = Path(ROOT) / 'output'
SCHEMA_DIR = Path(ROOT) / '../src/linkml'

def output_path(fn: str) -> str:
    return str(Path(OUTPUT_DIR) / fn)


DIGIT = 'UBERON:0002544'
VACUOLE = 'GO:0005773'
CYTOPLASM = 'GO:0005737'
HUMAN = 'NCBITaxon:9606'
NEURON = 'CL:0000540'
CELLULAR_COMPONENT = 'GO:0005575'
CELL = 'CL:0000000'