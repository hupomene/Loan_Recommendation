
from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/',methods=['POST'])
def Loan_Decision():
    Veteran_Flag = request.form['V']
    Credit_score = request.form['C']
    Delinquency_amount = request.form['D']
    Minimum_down_payment = request.form['MDP']
    Maximum_Monthly_Income = request.form['MMI']
    Typical_Max_Front_Ratio = request.form['TMFR']
    Max_Back_Ratio = request.form['MBR']
    Max_Mortgage_Amount = request.form['MMA']
    Minimum_Monthly_Reserves= request.form['MMR']
    Judgment_number = request.form['JN']
    Payment_plan_flag = request.form['PPF']
    Late_Payment_Flag = request.form['LPF']
    Foreclosure_Num = request.form['FN']
    Bankruptcy_Year_ch7 = request.form['BCH7']
    Bankruptcy_Year_ch13_Discharge = request.form['BCH13DC']
    Bankruptcy_Year_ch13_Dismissal = request.form['BCH13DS']
    Occupancy = request.form['OC']

    downpayment = float(Minimum_down_payment)
    credit_score = int(Credit_score)
    loan_amt = float(Max_Mortgage_Amount)
    reserves = int(Minimum_Monthly_Reserves)
    monthly_income = float(Maximum_Monthly_Income)
    front_ratio = float(Typical_Max_Front_Ratio)
    back_ratio = float(Max_Back_Ratio)
    Delinquency_amount = float(Delinquency_amount)
    Judgment_number = int(Judgment_number)
    veteran_flag = Veteran_Flag
    Payment_plan_flag = Payment_plan_flag
    Late_Payment_Flag = Late_Payment_Flag
    Foreclosure_Num = int(Foreclosure_Num)
    Bankruptcy_Year_ch7 = int(Bankruptcy_Year_ch7)
    Bankruptcy_Year_ch13_Discharge = int(Bankruptcy_Year_ch13_Discharge)
    Bankruptcy_Year_ch13_Dismissal = int(Bankruptcy_Year_ch13_Dismissal)
    Occupancy = int(Occupancy)


    downpament_percent = (downpayment / loan_amt) * 100
    # VA

    if ((veteran_flag == 'Y') & (credit_score >= 580) & (back_ratio <= 67.0) & (Judgment_number == 0) & (
            Payment_plan_flag == 'Y')
            & (Late_Payment_Flag == 'N') & (Foreclosure_Num >= 2) & (Bankruptcy_Year_ch7 >= 2)
            & ((Bankruptcy_Year_ch13_Discharge >= 1) or (Bankruptcy_Year_ch13_Dismissal >= 1)) & (Occupancy == 1)):
        Loan_VA = 'Y'
    else:
        Loan_VA = 'N'

    # Conventional
    # Primary - Fannie Mae
    if ((credit_score >= 620.0) & (3.0 <= downpament_percent) & (loan_amt <= 647200) & (reserves >= 0)
            & (back_ratio <= 50.0) & (Judgment_number == 0) & (Payment_plan_flag == 'Y')
            & (Late_Payment_Flag == 'N') & (Foreclosure_Num >= 7) & (Bankruptcy_Year_ch7 >= 4)
            & ((Bankruptcy_Year_ch13_Discharge >= 2) or (Bankruptcy_Year_ch13_Dismissal >= 4)) & (Occupancy == 1)):
        Loan_CV_FMae_P = 'Y'
    else:
        Loan_CV_FMae_P = 'N'

    # Second Home - Fannie Mae
    if ((credit_score >= 620.0) & (10.0 <= downpament_percent) & (loan_amt <= 647200) & (reserves >= 2)
            & (back_ratio <= 50.0) & (Delinquency_amount <= 5000) & (Judgment_number == 0) & (Payment_plan_flag == 'Y')
            & (Late_Payment_Flag == 'N') & (Foreclosure_Num >= 7) & (Bankruptcy_Year_ch7 >= 4)
            & ((Bankruptcy_Year_ch13_Discharge >= 2) or (Bankruptcy_Year_ch13_Dismissal >= 4)) & (Occupancy == 2)):
        Loan_CV_FMae_S = 'Y'
    else:
        Loan_CV_FMae_S = 'N'

    # Invesstment - Fannie Mae
    if ((credit_score >= 620.0) & (15.0 <= downpament_percent) & (loan_amt <= 647200) & (reserves >= 6)
            & (back_ratio <= 50.0) & (Delinquency_amount <= 5000) & (Judgment_number == 0) & (Payment_plan_flag == 'Y')
            & (Late_Payment_Flag == 'N') & (Foreclosure_Num >= 7) & (Bankruptcy_Year_ch7 >= 4)
            & ((Bankruptcy_Year_ch13_Discharge >= 2) or (Bankruptcy_Year_ch13_Dismissal >= 4)) & (Occupancy == 3)):
        Loan_CV_FMae_I = 'Y'
    else:
        Loan_CV_FMae_I = 'N'

    # Primary - Fannie Mac
    if ((credit_score >= 620.0) & (3.0 <= downpament_percent) & (loan_amt <= 647200) & (reserves >= 0)
            & (back_ratio <= 50.9) & (Judgment_number == 0) & (Payment_plan_flag == 'Y')
            & (Late_Payment_Flag == 'N') & (Foreclosure_Num >= 7) & (Bankruptcy_Year_ch7 >= 4)
            & ((Bankruptcy_Year_ch13_Discharge >= 2) or (Bankruptcy_Year_ch13_Dismissal >= 4)) & (Occupancy == 1)):
        Loan_CV_FMac_P = 'Y'
    else:
        Loan_CV_FMac_P = 'N'

    # Second Home - Fannie Mac
    if ((credit_score >= 620.0) & (10.0 <= downpament_percent) & (loan_amt <= 647200) & (reserves >= 2)
            & (back_ratio <= 50.9) & (Delinquency_amount <= 5000) & (Judgment_number == 0) & (Payment_plan_flag == 'Y')
            & (Late_Payment_Flag == 'N') & (Foreclosure_Num >= 7) & (Bankruptcy_Year_ch7 >= 4)
            & ((Bankruptcy_Year_ch13_Discharge >= 2) or (Bankruptcy_Year_ch13_Dismissal >= 4)) & (Occupancy == 2)):
        Loan_CV_FMac_S = 'Y'
    else:
        Loan_CV_FMac_S = 'N'

    # Invesstment - Fannie Mac
    if ((credit_score >= 620.0) & (15.0 <= downpament_percent) & (loan_amt <= 647200) & (reserves >= 6)
            & (back_ratio <= 50.9) & (Delinquency_amount <= 5000) & (Judgment_number == 0) & (Payment_plan_flag == 'Y')
            & (Late_Payment_Flag == 'N') & (Foreclosure_Num >= 7) & (Bankruptcy_Year_ch7 >= 4)
            & ((Bankruptcy_Year_ch13_Discharge >= 2) or (Bankruptcy_Year_ch13_Dismissal >= 4)) & (Occupancy == 3)):
        Loan_CV_FMac_I = 'Y'
    else:
        Loan_CV_FMac_I = 'N'

    # FHA
    if ((580 <= credit_score) & (3.5 <= downpament_percent) & (loan_amt <= 420680) & (reserves >= 0)
            & (back_ratio <= 56.9) & (Delinquency_amount <= 2000) & (Judgment_number == 0) & (Payment_plan_flag == 'Y')
            & (Late_Payment_Flag == 'N') & (Foreclosure_Num >= 3) & (Bankruptcy_Year_ch7 >= 2)
            & ((Bankruptcy_Year_ch13_Discharge >= 1) or (Bankruptcy_Year_ch13_Dismissal >= 1)) & (Occupancy == 1)):
        Loan_FHA = 'Y'
    else:
        Loan_FHA = 'N'

    # USDA
    if ((580 <= credit_score) & (0.0 <= downpament_percent) & (loan_amt <= 375000) & (reserves >= 0)
            & (monthly_income <= 7525.00) & (front_ratio <= 31.9) & (back_ratio <= 45.0) & (Judgment_number == 0)
            & (Payment_plan_flag == 'Y') & (Late_Payment_Flag == 'N') & (Foreclosure_Num >= 3)
            & (Bankruptcy_Year_ch7 >= 3) & (
                    (Bankruptcy_Year_ch13_Discharge >= 1) or (Bankruptcy_Year_ch13_Dismissal >= 1))
            & (Occupancy == 1)):
        Loan_USDA = 'Y'
    else:
        Loan_USDA = 'N'

    # Return for Loan recommendation
    Loan_Y_N = [Loan_VA, Loan_CV_FMae_P, Loan_CV_FMae_S, Loan_CV_FMae_I, Loan_CV_FMac_P, Loan_CV_FMac_S, Loan_CV_FMac_I,
                Loan_FHA, Loan_USDA]
    Loan_List = ['VA', 'Conventional- Fannie Mae', 'Conventional- Fannie Mae', 'Conventional- Fannie Mae',
                 'Conventional- Freddie Mac', 'Conventional- Freddie Mac', 'Conventional- Freddie Mac',
                 'FHA', 'USDA']

    Loan = []
    k = 0
    for i in Loan_Y_N:
        if (i == 'Y'):
            name = Loan_List[k]
            Loan.append(name)
        k += 1

    return jsonify({'Loan Recommendation': Loan})


if __name__ == "__main__":
    app.run(debug=True)