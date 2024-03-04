#Buatlah fungsi-fungsi konversi suhu menggunakan lambda function. Fungsi-fungsi yang harus anda implementasikan:
#• Celcius to Fahrenheit. F = (9/5) ∗C + 32
#• Celcius to Reamur. R = 0.8 ∗C
#Berikan contoh penggunaannya untuk test-case berikut ini:
#• Input C = 100. Output F = 212.
#• Input C = 80. Output R = 64.
#• Input = 0. Output F = 32.

# Lambda function untuk konversi Celcius ke Fahrenheit: F = (9/5) ∗C + 32
cfahrenheit = lambda C: (9/5) * C + 32

# Lambda function untuk konversi Celcius ke Reamur: R = 0.8 ∗C
creamur = lambda C: 0.8 * C

print("Input C = 100. Output F =", cfahrenheit(100))
print("Input C = 80. Output R =", creamur(80))
print("Input C = 0. Output F =", cfahrenheit(0))

