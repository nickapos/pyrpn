#!/usr/bin/env python3

def s_rates():
  varmenu("salary")
  tax_allowance=12500
  tax_allowance_threshold=100000
  top_rate=0.48
  top_rate_thres=125140
  if salary >= top_rate_thres:
     tax_allowance =0
  elif salary >= tax_allowance_threshold:
    diff=salary-tax_allowance_threshold
    tax_allowance=tax_allowance-diff/2
    salary=salary-tax_allowance
  else:
    salary=salary-tax_allowance
  adv_rate=0.45
  adv_rate_thres=75000
  adv_diff= top_rate_thres-adv_rate_thres
  high_rate=0.42
  high_rate_thres=43663
  high_diff=adv_rate_thres-high_rate_thres
  interm_rate=0.21
  interm_rate_thres=27492
  interm_diff=high_rate_thres-interm_rate_thres
  basic_rate=0.2
  basic_rate_thres=15398
  basic_diff=interm_rate_thres-basic_rate_thres
  start_rate=0.19
  start_rate_thres=12571
  start_diff=basic_rate_thres-start_rate_thres
  tax=0
  tax_list=[]
  adv_tax=adv_diff*adv_rate
  high_tax=high_diff*high_rate
  interm_tax=interm_diff*interm_rate
  basic_tax=basic_diff*basic_rate
  start_tax=start_diff*start_rate
  if salary >= top_rate_thres:
    top_diff=salary-top_rate_thres
    top_tax=top_diff*top_rate
    tax=top_tax+adv_tax+high_tax+interm_tax+basic_tax+start_tax
  elif salary >= adv_rate_thres:
    adv_diff= salary-adv_rate_thres
    adv_tax=adv_diff*adv_rate
    tax=adv_tax+high_tax+interm_tax+basic_tax+start_tax
  elif salary >= high_rate_thres:
    high_diff=salary-high_rate_thres
    high_tax=high_diff*high_rate
    tax=high_tax+interm_tax+basic_tax+start_tax
  elif salary >= interm_rate_thres:
    interm_diff=salary-interm_rate_thres
    interm_tax=interm_diff*interm_rate
    tax=interm_tax+basic_tax+start_tax
  elif salary >= basic_rate_thres:
    basic_diff=salary-basic_rate_thres
    basic_tax=basic_diff*basic_rate
    tax=basic_tax+start_tax
  else:
    start_tax=salary*start_rate
    tax_list.append(start_tax)
    tax=start_tax
  PRX(top_diff)
  PRX(adv_diff)
  PRX(high_diff)
  PRX(basic_diff)
  PRX(start_diff)
