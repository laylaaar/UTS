def user():
    nama = input ("Silahkan Masukkan Nama Anda : ")
    NIM = input ("Silahkan Masukkan NIM Anda :")

    print ("Nama : "+nama)
    print ("NIM : "+NIM)
user()

def menu():
    print("Pilihan Menu Hari Ini : ")
    print("1. Sate Taichan")
    print("2. Dimsum Mix")
    print("3. Siomay Bandung")
    print("4. Exit")

    pilih=str(input("Menu Pilihan Anda : "))

    if pilih == "1" :
        print("Anda Memilih Sate Taichan")
    elif pilih == "2" :
        print(" Anda Memilih Dimsum Mix")
    elif pilih == "3" :
        print(" Anda Memilih Siomay Bandung")
    
    harga=int(input("Harga Menu: "))
    ppn = harga*(10/100)
    total = harga+ppn

    print("Total Pesanan Anda: ", int(total))

menu()
