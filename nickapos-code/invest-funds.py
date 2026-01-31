def finvest(a):
    # Given equations:
    varmenu("a")
    tb = 0.75 * a
    s = 0.25 * a
    fi = s / 0.4  # From s = 0.4 * fi → fi = s / 0.4
    b = 0.6 * fi
    lb = a - fi   # From a = fi + lb → lb = a - fi
    print("a",a,"ts:",ts,"s",s,"fi",fi,"b",b,"lb",lb)

