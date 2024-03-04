#Buatlah sebuah fungsi yang dapat menentukan apakah minimal dua dari tiga parameter yang diberikan memiliki digit paling kanan yang sama.
# Fungsi tersebut menghasilkan nilai True jika memenuhi dan False jika tidak memenuhi.
# Gunakan fungsi tersebut untuk mengecek beberapa test-case berikut ini:
# • Input = 30, 20, 18. Output yang diharapkan = True
# • Input = 145, 5, 100. Output yang diharapkan = True
# • Input = 71, 187, 18. Output yang diharapkan = False
# • Input = 1024, 14, 94. Output yang diharapkan = True
# • Input = 53, 8900, 658. Output yang diharapkan = False
# Ketiga bilangan tersebut diinputkan oleh pengguna, sehingga anda perlu membaca input dari pengguna.
# Fungsi anda harus diberi nama cek_digit_belakang().

def cek_digit_belakang(a, b, c):
    a = a % 10
    b = b % 10
    c = c % 10

    if a == b or a == c or b == c:
        return True
    else:
        return False

nputA = int(input("Masukkan angka 1 = "))
nputB = int(input("Masukkan angka 2 = "))
nputC = int(input("Masukkan angka 3 = "))

hasil = cek_digit_belakang(nputA, nputB, nputC)
print(hasil)
