from __future__ import print_function

import os
from string import Template

print("This script will create the DR, DR2, DS, DS_IS, DS_IS_runningBW, and DS_runningBW variations for semileptonic tW samples. This should be executed from this very folder.")

do_boosted = True
top_pt_threshold = 250 # minimum top pt in GeV for boosted samples

dict_DRS = {
    "DR"              : 1,
    "DR2"             : 2,
    "DS_IS"           : 3,
    "DS_IS_runningBW" : 4,
    "DS"              : 5,
    "DS_runningBW"    : 6,
}

dict_DECAYMODES = {
    "tHadWLep": {
        "DECAY_WfromTOP": "q q~",
        "DECAY_WfromANTITOP": "q q~",
        "DECAY_Wplus": "l+ vl",
        "DECAY_Wminus": "l- vl~",
    },
    "tLepWHad": {
        "DECAY_WfromTOP": "l+ vl",
        "DECAY_WfromANTITOP": "l- vl~",
        "DECAY_Wplus": "q q~",
        "DECAY_Wminus": "q q~",
    },
}

template_prefix = "template_ST_tW_5f_NLO_semilep"
sample_basename = "ST_tW_5f_NLO_"

def copy_card(sample_name, card_postfix, substitute={}):
    card = open(template_prefix + card_postfix, "r")
    card = Template(card.read())
    card = card.substitute(substitute)
    with open("../" + sample_name + "/" + sample_name + card_postfix, "w") as newcard:
        newcard.write(str(card))

for decaymode in dict_DECAYMODES.keys():
    for boosted in [True, False]:
        if boosted and not do_boosted:
            continue
        for drs in dict_DRS.keys():
            sample_name = sample_basename + decaymode + ("_TopPt{}toInf".format(str(top_pt_threshold)) if boosted else "") + "_{}".format(drs)
            print("Creating cards for " + sample_name)
            os.system("mkdir -p ../" + sample_name)
            # Copy run card:
            substitute = {
                "DRS_ISTR": dict_DRS[drs],
                "PT_MIN_PDG": "6:{}".format(str(top_pt_threshold)) if boosted else "",
            }
            copy_card(sample_name, "_run_card.dat", substitute)
            # Copy proc card:
            substitute = {
                "OUTPUT_NAME": sample_name,
            }
            copy_card(sample_name, "_proc_card.dat", substitute)
            # Copy madspin card:
            substitute = dict_DECAYMODES[decaymode]
            copy_card(sample_name, "_madspin_card.dat", substitute)
            # Copy customization card:
            copy_card(sample_name, "_customizecards.dat")
