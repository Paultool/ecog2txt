# standard libraries
import os

# third-party packages
import pandas as pd
from tensor2tensor.data_generators import text_encoder

# local
from ..utils_jgm.machine_compatibility_utils import MachineCompatibilityUtils

# paths
MCUs = MachineCompatibilityUtils()
text_dir = os.path.join(os.path.dirname(__file__), 'auxiliary')
tikz_dir = os.path.join(MCUs.get_path('tikz'), 'DSftHC')
data_dir = os.path.join(MCUs.get_path('data'), 'ecog2txt')
figs_dir = os.path.join(MCUs.get_path('figs'), 'DSftHC')

# other useful variables
EOS_token = text_encoder.EOS
pad_token = text_encoder.PAD
OOV_token = '<OOV>'

# useful sets
TOKEN_TYPES = {
    'phoneme', 'word', 'trial', 'word_sequence', 'word_piece_sequence',
    'phoneme_sequence'
}
DATA_PARTITIONS = {'training', 'validation', 'testing'}


# functions
def str2int_hook(d):
    return {int(k) if k.lstrip('-').isdigit() else k: v for k, v in d.items()}


# useful linguistic things
consonant_dict = {
    'phoneme': [
        'p', 'b', 't', 'd', 'k', 'g',
        'f', 'v', '\u03B8', '\u00F0', 's', 'z', '\u0283', '\u0292', 'h',
        't\u0283', 'd\u0292',
        'm', 'n', '\u014b',
        'l', 'r',  # '\u0279',
        'w', 'j',
    ],
    'voicing': [
        'voiceless', 'voiced', 'voiceless', 'voiced', 'voiceless', 'voiced',
        'voiceless', 'voiced', 'voiceless', 'voiced', 'voiceless',
        'voiced', 'voiceless', 'voiced', 'voiceless',
        'voiceless', 'voiced',
        'voiced', 'voiced', 'voiced',
        'voiced', 'voiced',
        'voiced', 'voiced',
    ],
    'place': [
        'bilabial', 'bilabial', 'alveolar', 'alveolar', 'velar', 'velar',
        'labiodental', 'labiodental', 'dental', 'dental', 'alveolar',
        'alveolar', 'palatal', 'palatal', 'glotal',
        'palatal', 'palatal',
        'bilabial', 'alveolar', 'velar',
        'alveolar', 'palatal',
        'labio-velar', 'palatal'
    ],
    'manner': [
        'stop', 'stop', 'stop', 'stop', 'stop', 'stop',
        'fricative', 'fricative', 'fricative', 'fricative', 'fricative',
        'fricative', 'fricative', 'fricative', 'fricative',
        'affricate', 'affricate',
        'nasal', 'nasal', 'nasal',
        'liquid', 'liquid',
        'approximant', 'approximant',
    ]
}
consonant_df = pd.DataFrame(consonant_dict)

# "Acoustic Characteristics of American English Vowels"
# Hillenbrand et al
# J. Acoustic Soc. Am., 97(5), Pt. 1
# 1995
vowel_dict = {
    'phoneme': ['i', '\u026A', 'e', '\u025B', '\u00E6', '\u0251', '\u0252', '\u0254', 'o', '\u028A', 'u', '\u028C'],
    'F1': [342, 427, 476, 580, 588, 768, 768, 652, 497, 469, 378, 623], 
    'F2': [2322, 2034, 2089, 1799, 1952, 1333, 1333, 997, 910, 1122, 997, 1200],
}
# '\u0259'? 'a'?
vowel_df = pd.DataFrame(vowel_dict)
