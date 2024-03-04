#Buatlah sebuah fungsi yang dapat menentukan apakah ketiga parameter memenuhi semua ketentuan berikut ini:
#• Ketiga parameter tersebut nilainya berbeda semua.
#• Ada kemungkinan jika diambil dua parameter dan dijumlahkan hasilnya sama dengan parameter lainnya (yang tersisa).
# Fungsi tersebut akan menghasilkan nilai True jika semua ketentuan tersebut dipenuhi. Jika tidak terpenuhi,
# maka fungsi akan menghasilkan nilai False. Fungsi anda harus diberi nama cek_angka().
def cek_angka(a, b, c):
    if a != b != c:
        return a + b == c or a + c == b or b + c == a
    else:
        return False

a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua   : "))
c = int(input("Masukkan angka ketiga  : "))

hasil = cek_angka(a, b, c)
print(hasil)

