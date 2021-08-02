def convert_cel_to_far(temp_celc):
    temp_far = temp_celc * 9/5 + 32
    return temp_far

def convert_far_to_cel(temp_far):
    temp_celc = (temp_far - 32) * 5/9
    return temp_celc

tf = input("Informe a temperatura em graus Fahrenheit: ");
tf_c = convert_far_to_cel(float(tf))
print(f"{tf} graus Fahrenheit = {tf_c:.2f} graus Celcius")

tc = input("Informe a temperatura em graus Celcius: ");
tc_f = convert_cel_to_far(float(tc))
print(f"{tc} graus Celcius = {tc_f:.2f} graus Fahrenheit")
