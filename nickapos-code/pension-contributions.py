def p_cont():
  varmenu("yob","year", "sal","rais","cont")
  end=70-(year-yob)
  sal_li=[sal]
  cont_li=[sal*cont]
  csu=sal*cont
  ssu=sal
  sal1=sal
  for i in range(end):
    #print("sal:",sal,"cont:",sal*contr)
    sal1=sal1*(1+rais)
    sal_li.append(sal1)
    cont_li.append(sal1*cont)
    csu=csu+sal1*cont
    ssu=ssu+sal1
  print("ssu:",ssu,"csu:",csu)

