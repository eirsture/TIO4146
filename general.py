def print_num(num):
    return format(num, ".4f")

def format_float(num):
    return float(format(num, ".4f"))

def capm(r_f, r_m, b_p, variable_name="p", market_premium=None):
    if market_premium:
        print("r_{%s}=r_{f}+MRP \cdot \\beta_{%s}" % (variable_name, variable_name))
        print("r_{%s}=%s+%s \cdot %s" % (variable_name, r_f, market_premium, b_p))
        r_p = float(format(r_f + market_premium * b_p, ".4f"))
    else:
        print("r_{%s}=r_{f}+\left(r_{m}-r_{f}\\right) \cdot \\beta_{%s}" % (variable_name, variable_name))
        print("r_{%s}=%s+\left(%s-%s\\right) \cdot %s" % (variable_name, r_f, r_m, r_f, b_p))
        r_p = float(format(r_f + (r_m-r_f)*b_p, ".4f"))

    print("r_{%s} = %s" % (variable_name, r_p))
    return r_p

def wacc_after_tax(r_d, r_e, D, E, V, tax):
    wacc = float(format(r_e*(E/V) + r_d*(1-tax)*(D/V), ".4f"))
    print(f'WACC: {print_num(wacc)}')
    return wacc

def unlevered_cash_flow(cash_flow, occ, tax_rate=None, tax_done=True):
    if tax_done:
        c_flow = format_float(cash_flow/occ)
        print("Cash\:flow = \\frac{Cash\:flow}{r_{a}}")
        print("Cash\:flow = \\frac{%s}{%s}" % (c_flow, occ))
    else:
        c_flow = format_float((1-tax_rate)*cash_flow/occ)
        print("Cash\:flow = (1-\\tau) \cdot \\frac{Cash\:flow}{r_{a}}")
        print("Cash\:flow = (1-\\tau) \cdot \\frac{%s}{%s}" % (tax_rate, c_flow, occ))
    print(f'\'Unlevered\' cash flow = {c_flow}')
    return c_flow

def npv(cash_flow, investment):
    npv = format_float(cash_flow - investment)
    print("NPV = Cash flow - Investment")
    print("NPV = %s - %s" % (cash_flow, investment))
    print(f'NPV = {npv}')
    return npv

def yearly_interest_charge(debt, interest_rate):
    charge = format_float(interest_rate*debt)
    print("Yearly\:interest\:charge =  D \\cdot r_d")
    print("Yearly\:interest\:charge =  %s \\cdot %s" % (debt, interest_rate))
    print(f'Yearly\:interest\:charge = {charge}')
    return charge

def tax_advantage(tax, interest_charge):
    t_a = format_float(tax*interest_charge)
    print("Yearly\:tax\:advantage =  Tax\:rate \\cdot Yearly\:interest\:charge")
    print("Yearly\:tax\:advantage =  %s \\cdot %s" % (tax, interest_charge))
    print(f'Yearly\:tax\:advantage = {t_a}')
    return t_a

def tax_shield(debt, interest_rate, tax_rate, debt_type, occ=None):
    # debt_type can be: ("predetermined", "periodically", "continuously")
    interest_charge = format_float(yearly_interest_charge(debt, interest_rate))
    tax_advg = format_float(tax_advantage(tax_rate, interest_charge))

    if debt_type == "periodically":
        print(f'Debt is rebalanced periodically')
        print("Tax\:shield = \\frac{Tax\:advantage}{r_{a}} \cdot \\frac{1+r_{a}}{1+r_{d}}")
        print("Tax\:shield = \\frac{%s}{%s} \cdot \\frac{1+%s}{1+%s}" % (tax_advg, occ, occ, interest_rate))
        tax_shield = tax_advg / occ
        tax_shield = format_float(tax_shield * (1 + occ) / (1 + interest_rate))
    elif debt_type == "continuously":
        print("Tax\:shield = \\frac{Tax\:advantage}{r_{a}}")
        print("Tax\:shield = \\frac{%s}{%s}" % (tax_advg, occ))
        print(f'Debt is rebalanced continuously')
        tax_shield = format_float(tax_advg / occ)
    elif debt_type == "predetermined":
        print(f'Debt is predetermined')
        print("Tax\:shield = \\frac{Tax\:advantage}{r_{d}}")
        print("Tax\:shield = \\frac{%s}{%s}" % (tax_advg, interest_rate))
        tax_shield = format_float(tax_advg / interest_rate)

    print(f'Tax\:shield = {tax_shield}')
    return tax_shield

def apv(npv, tax_shield):
    apv = format_float(npv + tax_shield)
    print("APV = NPV + Tax shield")
    print("APV = %s + %s" % (npv, tax_shield))
    print(f'APV = {apv}')
    return apv

if __name__ == '__main__':
    r_f = None  # Risk-free interest rate
    r_m = None  # Return of market
    b_p = None  # Beta of return you need calculated, e.g. asset
    mrp = None  # Market risk premium = Return of market - Risk-free interest rate

    capm(r_f, r_m, b_p, variable_name="p", market_premium=None)
