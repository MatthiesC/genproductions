# ST_tW_5f_NLO_semilep

This directory contains templates for the creation of cards for the tW process at NLO with semileptonic decays.

Executing `python create_cards.py` (both python2 and python3 work) will create several new directories on the same directory level. Different directories will be created for the two possible semileptonic decay modes (either hadronic top + leptonic associated W *or* leptonic top + hadronic associated W). There will be six different versions for each decay mode, using different settings from the MadSTR plugin: DR, DR2, DS, DS_runningBW, DS_IS, DS_IS_runningBW.

Furthermore, there is the option to create separate cards which include a cut on the transverse momentum of the generated top quark; this can be controlled via the `do_boosted` boolean at the top of the python script. The cut can be set with the `top_pt_threshold` variable, also at the top of the script.
