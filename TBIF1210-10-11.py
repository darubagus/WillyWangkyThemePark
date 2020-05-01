#version 1.0 
#April 25th 2020

import csv
import uuid as u
import hashlib as h

def cek_role(id_user,user):
    '''
    fungsi cek_role adalah sebuah fungsi tambahann untuk mengecek peran dari user,
    fungsi ini digunakkan untuk memutuskan apakah program akan masuk ke menu admin atau menu pemain
    '''
    i=1
    while (user[i]!=None):
        if (i==id_user):
            return user[i][5]
        else:
            i+=1

def hash_pass(password):
    '''
    fungsi hash_pass adalah fungsi untuk mengubah password user menjadi string random
    '''
    salt = u.uuid4().hex
    return h.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_pass, user_pass):
    '''
    fungsi check_password adalah sebuah fungsi untuk mencocokkan antara password yang diinput oleh user saat login dengan password yang tersimpan di database
    '''
    password, salt = hashed_pass.split(':')
    return password == h.sha256(salt.encode()+ user_pass.encode()).hexdigest()

def load(): #CLEAR
    '''
    I.S data terdefinisi di dalam file .csv
    F.S seluruh data sudah dituliskan di dalam array 
    '''
    user=[None for i in range(201)]
    wahana=[None for i in range(201)]
    pembelian=[None for i in range(201)]
    penggunaan=[None for i in range(201)]
    tiket=[None for i in range(201)]
    refund=[None for i in range(201)]
    kritiksaran=[None for i in range(201)]
    kehilangan=[None for i in range(201)]

    file = input("Masukkan nama File User: ")
    with open(file, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i=0
        for row in readCSV:
            user[i]=row
            i+=1

    file =  input("Masukkan nama File Daftar Wahana: ")
    with open(file, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i=0
        for row in readCSV:
            wahana[i]=row
            i+=1

    file = input("Masukkan nama File Pembelian Tiket: ")
    with open(file, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i=0
        for row in readCSV:
            pembelian[i]=row
            i+=1

    file =  input("Masukkan nama File Penggunaan Tiket: ")
    with open(file, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i=0
        for row in readCSV:
            penggunaan[i]=row
            i+=1

    file = input("Masukkan nama File Kepemilikan Tiket: ")
    with open(file, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i=0
        for row in readCSV:
            tiket[i]=row
            i+=1

    file = input("Masukkan nama File Refund Tiket: ")
    with open(file, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i=0
        for row in readCSV:
            refund[i]=row
            i+=1

    file = input("Masukkan nama File Kritik dan Saran: ")
    with open(file, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i=0
        for row in readCSV:
            kritiksaran[i]=row
            i+=1
    file = input("Masukkan nama File Kehilangan tiket: ")
    with open(file, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i=0
        for row in readCSV:
            kehilangan[i]=row
            i+=1

    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")

    return user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan
    
def save(user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan): #CLEAR
    '''
    I.S seluruh data tersimpan dalam beberapa array
    F.S data terbaru sudah dituliskan ke dalam file .csv}
    '''
    file = input("Masukkan nama File User: ")
    with open(file, 'w', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        for i in range(201):
            if (user[i]!=None):
                writeCSV.writerow(user[i])
            else:
                break
    
    file = input("Masukkan nama File Daftar Wahana: ")
    with open(file, 'w', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        for i in range(201):
            if (wahana[i]!=None):
                writeCSV.writerow(wahana[i])
            else:
                break
    
    file = input("Masukkan nama File Pembelian Tiket: ")
    with open(file, 'w', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        for i in range(201):
            if (pembelian[i]!=None):
                writeCSV.writerow(pembelian[i])
            else:
                break

    file = input("Masukkan nama File Penggunaan Tiket: ")
    with open(file, 'w', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        for i in range(201):
            if (penggunaan[i]!=None):
                writeCSV.writerow(penggunaan[i])
            else:
                break
    
    file = input("Masukkan nama File Kepemilikan Tiket: ")
    with open(file, 'w', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        for i in range(201):
            if (tiket[i]!=None):
                if (tiket[i][3]!='0'):
                    writeCSV.writerow(tiket[i])
            else:
                break
        
    file = input("Masukkan nama File Refund Tiket: ")
    with open(file, 'w', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        for i in range(201):
            if (refund[i]!=None):
                writeCSV.writerow(refund[i])
            else:
                break
    
    file = input("Masukkan nama File Kritik dan Saran: ")
    with open(file, 'w', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        for i in range(201):
            if (kritiksaran[i]!=None):
                writeCSV.writerow(kritiksaran[i])
            else:
                break

    file = input("Masukkan nama File Kehilangan Tiket: ")
    with open(file, 'w', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        for i in range(201):
            if (kehilangan[i]!=None):
                writeCSV.writerow(kehilangan[i])
            else:
                break

    print("Data berhasil disimpan!")

def searchUname(user,uname):  #CLEAR
    '''
    fungsi searchUname adalah fungsi tambahan untuk mengecek apakah username terkait ada di dalam database
    '''
    cek = False
    i = 1

    while not(cek) and (user[i]==None):
        if ((user[i][3]==uname)):
            cek = True
        else:
            i+=1
    
    return cek,i

def signup(user):  #CLEAR
    '''
    I.S data pengguna dalam bentuk array
    F.S data pemain telah ditambah dengan data input
    '''
    nama = input("Masukkan nama pemain: ")
    dofbirth = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    height = input("Masukkan tinggi badan pemain (cm): ")
    uname = input("Masukkan username pemain: ")
    password = input("Masukkan password pemain: ")
    role= 'pemain'
    saldo= 0
    subscription = 'basic'

    exist,i = searchUname(user,uname)

    while exist:
        print("username tidak tersedia.")
        uname = input("Masukkan username pemain: ")
        exist,i = searchUname(user,uname)
    
    encrypted_pass = hash_pass(password)

    print("Selamat menjadi pemain,"+ nama+ ". Selamat bermain.")

    content = [nama,dofbirth,height,uname,encrypted_pass,role,saldo,subscription] 

    i=0
    while (user[i]!=None):
        i+=1
    user[i]=content

    return user

def exit(user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran,kehilangan): #CLEAR
    '''
    procedure exit dapat dijalankan oleh user. Saat perintah ini dijalankan akan muncul prompt untuk save data,
    apabila user akan menyimpan data, maka data program akan disave
    I.S seluruh data tersimpan di dalam array
    F.S jika user melakukan input “Y” maka seluruh data di dalam array akan di-store ke dalam file .csv masing-masing
    '''
    pil = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ?")
    
    while (pil!='Y' and pil!='N'):
        pil = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ?")
    
    if (pil=='Y'):
        save(user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran,kehilangan)

def login(user): #CLEAR
    '''
    I.S data pengguna dalam bentuk array
    F.S menunjukkan pengguna login bila username dan password sesuai, serta mengembalikan address pengguna

    Bila username/password tidak sesuai, maka akan ditampilkan pesan kesalahan
    '''
    uname = input("Masukkan username: ")
    password = input("Masukkan password: ")

    cek = False
    i = 1

    while not(cek) and (user[i]!=None):
        if ((user[i][3]==uname)):
            cek = True
        else:
            i+=1
    
    status_pass = check_password(user[i][4],password)

    if cek:
        if status_pass:
            print("Selamat bersenang-senang, "+user[i][0]+"!")
            return i
    else:
        print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")

def cari_pemain(user): #CLEAR
    '''
    I.S data pengguna dalam bentuk array
    F.S mencetak identitas pemain (nama, tgl lahir, dan tinggi badan dengan input username
    '''
    uname = input("Masukkan username: ")

    cek = False
    i = 1

    while not(cek) and (user[0]!=None):
        if ((user[i][3]==uname)):
            cek = True
        else:
            i+=1

    if cek:
        print("Nama Pemain: "+user[i][0])
        print("Tinggi Pemain: "+user[i][2])
        print("Tanggal Lahir Pemain: "+user[i][1])
    else:
        print("Ups, username yang kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")

def hitung_umur(birthdate,hari_ini): #CLEAR
    '''
    fungsi hitung_umur adalah sebuah fungsi tambahan untuk menghitung berapa umur dari user terkait dalam rangka
    syarat untuk membeli tiket wahana
    '''
    born= [0 for i in range(3)]
    today =[0 for i in range(3)]

    born = birthdate.split('/')
    tgl_lahir = int(born[0])
    bln_lahir = int(born[1])
    thn_lahir = int(born[2])
    #tahun lahir jadi ['tgl', 'bln, 'thn']
    today = hari_ini.split('/')
    tgl_now = int(today[0])
    bln_now = int(today[1])
    thn_now = int(today[2])
    #tahun sekarang jadi ['tgl', 'bln, 'thn']

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

    if (tgl_lahir>tgl_now):
        bln_now -= 1
        tgl_now = tgl_now+ month[bln_lahir-1]

    if (bln_lahir)>bln_now:
        thn_now = thn_now-1
        bln_now = bln_now+12

    umur = thn_now-thn_lahir

    return umur

def cari_semua(wahana, choiceAge, choiceHeight): #CLEAR
    '''
    fungsi cari_tinggi adalah sebuah fungsi tambahan untuk mencari wahana berdasarkan kriteria tinggi terkait
    '''
    i = 0
    result = [None for i in range(201)]

    if (choiceHeight==int(1)):
        conditionHeight = '>=170'  
    else:
        conditionHeight = 'tanpa batasan'

    if (choiceAge==int(1)):
        conditionAge = 'anak-anak'  
    elif (choiceAge==int(2)):
        conditionAge = 'dewasa'
    else:
        conditionAge = 'semua umur'

    j=0
    baris_wahana = hitung_baris(wahana)

    for i in range(baris_wahana):
        if (wahana[i][4]==conditionHeight) and (wahana[i][3]==conditionAge):
            result[j]=wahana[i]
            j+=1

    
    return result

def cari(wahana): #CLEAR
    '''
    I.S data wahana dalam bentuk array
    F.S mencetak identitas wahana yang sesuai dengan input syarat tinggi dan umur
    '''
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print()
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")

    age = int(input("Batasan umur pemain: "))
    
    while not(age==int(1) or age==int(2) or age==int(3)):
        print("Batasan umur tidak valid!")
        age = input("Batasan umur pemain: ")

    height = int(input("Batasan tinggi badan: "))

    while not(height==int(1) or height==int(2)):
        print("Batasan tinggi badan tidak valid!")
        height = input("Batasan tinggi badan: ")

    result = cari_semua(wahana,age,height)
    i=0
    print("Hasil pencarian: ")
    if (result[i]==None):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu.")
    else:
        while (result[i]!=None):
            print(str(result[i][0])+" | "+str(result[i][1])+" | "+str(result[i][2]))
            i+=1
        
def cekWahana(wahana,id_wahana): #CLEAR
    '''
    fungsi cekWahana adalah fungsi tambahan untuk membantu fungsi beli_tiket dalam mengecek syarat dari sebuah wahana
    '''
    i=1
    cek = False
    wahanaPilihan = []
    while (wahana[i]!=None) and not(cek):
        if (wahana[i][0]==id_wahana):
            cek=True
        else:
            i+=1
    if cek :
        wahanaPilihan = wahana[i]
    
    if (wahanaPilihan[3]=='dewasa'):
        if (wahanaPilihan[4]=='>=170'):
            cond= 'dewasa>=170'
        elif (wahanaPilihan[4]=='tanpa batasan'):
            cond= 'dewasa'
    elif (wahanaPilihan[3]=='anak-anak'): 
        if (wahanaPilihan[4]=='>=170'):
            cond= 'anak>=170'
        elif (wahanaPilihan[4]=='tanpa batasan'):
            cond= 'anak'
    else:
        if (wahanaPilihan[4]=='>=170'):
            cond= 'SU>=170'
        elif (wahanaPilihan[4]=='tanpa batasan'):
            cond= 'SU'

    return cond  

def beli_tiket(user,wahana,id_user,pembelian,tiket): #CLEAR
    '''
    I.S data pembelian tiket dan kepemilikan tiket dalam bentuk array
    Syarat : pemain harus memenuhi kriteria umur dan tinggi badan untuk membeli tiket sebuah wahana
    F.S data pembelian tiket dan kepemilikan tiket tersimpan dalam array sesuai input
    '''
    id_wahana = input("Masukkan ID wahana: ")  
    tanggal = input("Masukkan tanggal hari ini (dd/mm/yy): ")
    jml_tiket = int(input("Jumlah tiket yang dibeli: "))

    i=1
    cek = False
    while (wahana[i]!=None) and not(cek):
        if (wahana[i][0]==id_wahana):
            cek=True
        else:
            i+=1
    
    cek = cekWahana(wahana,id_wahana)

    umur = hitung_umur(user[id_user][1],tanggal)
    saldo = int(user[id_user][6])
    harga= int(wahana[i][2])
    umur= int(umur)

    if (cek=='dewasa>=170'):
        if (int(user[id_user][2])<170) or (umur<17):
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
        elif (saldo<(jml_tiket*harga)):
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")
        else:
            content_tiket = [user[id_user][3],tanggal,id_wahana,jml_tiket]
            content_pembelian = [user[id_user][3], tanggal, id_wahana, jml_tiket]
            if (user[id_user][7]=='gold'):
                user[id_user][6] = str(saldo-int(0.5*int(jml_tiket*harga)))
            else:    
                user[id_user][6] = str(saldo-int(jml_tiket*harga))
            print("Selamat bersenang-senang di "+wahana[i][1])

            j=0
            while (tiket[j]!=None):
                j+=1
            tiket[j]=content_tiket
    
            k=0
            while (pembelian[k]!=None):
                k+=1
            pembelian[k]=content_pembelian
    elif (cek=='dewasa'):
        if (umur<17):
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
        elif (saldo<(jml_tiket*harga)):
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")
        else:
            content_tiket = [user[id_user][3],tanggal,id_wahana,jml_tiket]
            content_pembelian = [user[id_user][3], tanggal, id_wahana, jml_tiket]
            if (user[id_user][7]=='gold'):
                user[id_user][6] = str(saldo-int(0.5*int(jml_tiket*harga)))
            else:    
                user[id_user][6] = str(saldo-int(jml_tiket*harga))
            print("Selamat bersenang-senang di "+wahana[i][1])

            j=0
            while (tiket[j]!=None):
                j+=1
            tiket[j]=content_tiket
    
            k=0
            while (pembelian[k]!=None):
                k+=1
            pembelian[k]=content_pembelian
    elif (cek=='anak>=170'):
        if (int(user[id_user][2])<170) or (umur>17):
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
        elif (saldo<(jml_tiket*harga)):
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")
        else:
            content_tiket = [user[id_user][3],tanggal,id_wahana,jml_tiket]
            content_pembelian = [user[id_user][3], tanggal, id_wahana, jml_tiket]
            if (user[id_user][7]=='gold'):
                user[id_user][6] = str(saldo-int(0.5*int(jml_tiket*harga)))
            else:    
                user[id_user][6] = str(saldo-int(jml_tiket*harga))
            print("Selamat bersenang-senang di "+wahana[i][1])

            j=0
            while (tiket[j]!=None):
                j+=1
            tiket[j]=content_tiket
    
            k=0
            while (pembelian[k]!=None):
                k+=1
            pembelian[k]=content_pembelian
    elif (cek=='anak'):
        if (umur>17):
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
        elif (saldo<(tiket*harga)):
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")
        else:
            content_tiket = [user[id_user][3],tanggal,id_wahana,jml_tiket]
            content_pembelian = [user[id_user][3], tanggal, id_wahana, jml_tiket]
            if (user[id_user][7]=='gold'):
                user[id_user][6] = str(saldo-int(0.5*int(jml_tiket*harga)))
            else:    
                user[id_user][6] = str(saldo-int(jml_tiket*harga))
            print("Selamat bersenang-senang di "+wahana[i][1])

            j=0
            while (tiket[j]!=None):
                j+=1
            tiket[j]=content_tiket
    
            k=0
            while (pembelian[k]!=None):
                k+=1
            pembelian[k]=content_pembelian
    elif (cek=='SU>=170'):
        if (int(user[id_user][2])<170):
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
        elif (saldo<(jml_tiket*harga)):
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")
        else:
            content_tiket = [user[id_user][3],tanggal,id_wahana,jml_tiket]
            content_pembelian = [user[id_user][3], tanggal, id_wahana, jml_tiket]
            if (user[id_user][7]=='gold'):
                user[id_user][6] = str(saldo-int(0.5*int(jml_tiket*harga)))
            else:    
                user[id_user][6] = str(saldo-int(jml_tiket*harga))
            print("Selamat bersenang-senang di "+wahana[i][1])

            j=0
            while (tiket[j]!=None):
                j+=1
            tiket[j]=content_tiket
    
            k=0
            while (pembelian[k]!=None):
                k+=1
            pembelian[k]=content_pembelian
    elif (cek=='SU'):
        if (saldo<(jml_tiket*harga)):
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")
        else:
            content_tiket = [user[id_user][3],tanggal,id_wahana,jml_tiket]
            content_pembelian = [user[id_user][3], tanggal, id_wahana, jml_tiket]
            if (user[id_user][7]=='gold'):
                user[id_user][6] = str(saldo-int(0.5*int(jml_tiket*harga)))
            else:    
                user[id_user][6] = str(saldo-int(jml_tiket*harga))
            print("Selamat bersenang-senang di "+wahana[i][1])

            j=0
            while (tiket[j]!=None):
                j+=1
            tiket[j]=content_tiket
    
            k=0
            while (pembelian[k]!=None):
                k+=1
            pembelian[k]=content_pembelian
    

    return tiket,pembelian, user

def cari_wahana(wahana,id_wahana): #ADDITIONAL FUCTION 
    #fungsi cari_wahana merupakan fungsi tambahan untuk mencari address wahana dan keberadaan wahana
    #mengembalikan True jika wahana ada, dan false jika sebaliknya, serta mengembalikan address wahana
    i=0
    cek = False
	
    while not(cek) and (wahana[i]!=None):
        if (wahana[i][0]==id_wahana):
            cek = True
        else:
            i+=1
    return cek,i

def frefund(user,wahana,refund,tiket,id_user):
    '''
    I.S data kepemilikan tiket dan pemain tersimpan dalam array
    F.S data kepemilikan tiket di update, data saldo pemain diupdate, dan data refund ditambahkan ke dalam array refund

    Jumlah uang yang di-refund jika pemain memiliki tiket terkait yaitu 50% dari (hargatiket*jumlah_tiket)
    Jika pemain tidak memiliki tiket terkait, akan ditampilkan pesan kesalahan.
    '''
    id_wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini (dd/mm/yyyy): ")
    jml_tiket = int(input("Jumlah tiket yang di-refund: "))

    cek = False
    cek_wahana,idx = cari_wahana(wahana,id_wahana)

    if cek_wahana:
        harga_wahana = int(wahana[idx][2])

    uang_refund = int((0.5)*(harga_wahana)*int(jml_tiket))
    
    uname = user[id_user][3]
    
    j=0
    while (tiket[j]!=None and not(cek)):
        if ((tiket[j][2]==id_wahana) and int(tiket[j][3])<=jml_tiket):
            cek=True
        else:
            j+=1
    
    if cek:
        user[id_user][6] = str(int(user[id_user][6]) + (uang_refund))
        tiket[id_user][3] = str(int(tiket[id_user][3]) - int(jml_tiket))
        print("Uang refund telah kami berikan ke akun Anda.")

        content = [uname, tanggal, id_wahana, jml_tiket]

        i=0
        while (refund[i]!=None):
            i+=1
        refund[i]=content
    else:
        print("Anda tidak memiliki tiket terkait.")

    return refund,tiket    

def kritik_saran(user, id_user, kritiksaran):
    '''
    Fungsi kritik_saran dapat digunakan oleh pemain untuk memberikan kritik dan saran terhadap suatu wahana
    I.S data kritiksaran disimpan dalam array
    F.S data kritiksaran di update dengan input pengguna
    '''
    ID_wahana = input("Masukkan ID wahana: ")
    tanggal_kritik = input("Masukkan tanggal pelaporan: ")
    isi_kritik = input("Kritik/saran anda: ")

    uname = user[id_user][3]

    content = [uname,tanggal_kritik,ID_wahana,isi_kritik]

    i=0
    while (kritiksaran[i]!=None):
        i+=1

    kritiksaran[i]=content

    print("Kritik dan saran Anda kami terima.")

    return kritiksaran

def main(user, id_user, penggunaan, tiket):
    '''
    I.S data kepemilikan tiket tersimpan dalam array
    F.S data kepemilikan tiket di update dan data penggunaan tiket ditambahkan ke dalam array penggunaan
    '''
    id_wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini (dd/mm/yyyy):")
    jml_tiket = int(input("Jumlah tiket yang akan digunakan: "))

    uname = user[id_user][3]


    i = 0
    cek=False
    while (not(cek) and tiket[i]!=None):
        if ((tiket[i][2]==id_wahana) and (int(tiket[i][3])>=jml_tiket) and (tiket[i][0]==uname)):
            cek=True
        else:
            i+=1
    
    if cek:
        tiket[i][3] = str(int(tiket[i][3])-jml_tiket)
        print("Terimakasih telah bermain.")

        content = [uname, tanggal, id_wahana,jml_tiket]

        i=0
        while (penggunaan[i]!=None):
            i+=1

        penggunaan[i]=content
    else:
        print("Tiket Anda tidak valid dalam sistem kami.")

    return penggunaan,tiket

def hitung_baris(arr): #FUNGSI TAMBAHAN
    '''
    fungsi hitung_baris adalah fungsi tambahan untuk menghitung jumlah baris dari sebuah array
    '''
    baris = 0  # Inisialisasi
    while (arr[baris]!=None):  # Penghitungan dengan looping
        baris += 1
    return baris

def sort_Arr(arr): #CLEAR
    '''
    function sort_Arr adalah fungsi bantuan untuk mengurutkan array laporan secara alfabetis membesar
    '''
    i=1
    while (arr[i]!=None):
        idx_min=i
        j=i+1
        while (arr[j]!=None):
            if arr[idx_min][2] > arr[j][2]:
                idx_min = j
            j+=1
        arr[i], arr[idx_min] = arr[idx_min],arr[i]
        i+=1
    
    return arr
    
def lihat_laporan(kritiksaran): #CLEAR
    '''
    Procedure lihat_laporan dapat digunakan oleh admin untuk melihat kritik dan saran yang dimasukkan oleh pemain
    Tampilan diurutkan secara alfabetis berdasarkan ID_wahana
    I.S data kritiksaran tersimpan dalam array
    F.S data kritiksaran ditampilkan secara terurut berdasarkan id_wahana
    '''
    kritiksaran = sort_Arr(kritiksaran)
    baris = hitung_baris(kritiksaran)

    print("Kritik dan saran: ")
    i=1
    while (i<baris):
        print(kritiksaran[i][2]+" | "+kritiksaran[i][1]+" | "+kritiksaran[i][0]+" | "+kritiksaran[i][3])
        i+=1

def tambah_wahana(wahana): #CLEAR
    '''
    Function tambah_wahana dapat dilakukan oleh admin untuk menambahkan wahana baru ke dalam manajemen wahana
    I.S data wahana tersimpan di dalam sebuah array
    F.S data wahana diupdate dan ditambahkan dengan input pengguna
    '''
    print("Masukkan Informasi Wahana yang ditambahkan:")
    id_wahana = input("Masukkan ID_Wahana:")
    nama = input("Masukkan Nama Wahana:")
    harga = input("Masukkan Harga Tiket:")
    batas = input("Batasan umur:")
    tinggi = input("Batasan tinggi badan:")

    content= [id_wahana, nama, harga, batas, tinggi] #Content baru

    i=0
    while (wahana[i]!=None):
        i+=1

    wahana[i]= content
    print()
    print("Info wahana telah ditambahkan!")

    return wahana

def topup(user): #CLEAR
    '''
    Function topup dapat dilakukan oleh admin untuk menambahkan saldo terhadap seorang pemain
    I.S data pengguna tersimpan dalam sebuah array
    F.S data pengguna di dalam array di update dan pengguna yang di-topup saldonya akan diupdate saldonya
    '''
    username = input("Masukkan username: ")
    saldo = int(input("Masukkan saldo yang di top-up: "))

    i = 0
    while (user[i][3]) != username:
        i +=1

    saldo_prev = int(user[i][6])
    saldo_new = int(saldo_prev+saldo)

    user[i][6]= str(saldo_new)
    print("Top up berhasil. Saldo ", user[i][3], " bertambah menjadi", user[i][6])

    return user

def riwayat_wahana(penggunaan): #CLEAR
    '''
    Procedure riwayat_wahana menampilkan riwayat penggunaan dari wahana tertentu
    Format Tampilan : Tanggal_Bermain | Username Pengguna | Jumlah Tiket
    I.S data penggunaan wahana tersimpan dalam array
    F.S riwayat penggunaan wahana dengan id_wahana sesuai input pengguna 
    '''
    id_wahana = input("Masukkan ID Wahana: ")

    baris = hitung_baris(penggunaan)

    for i in range(baris):
        if (penggunaan[i][2]==id_wahana):
            print(penggunaan[i][1]+" | "+penggunaan[i][0]+" | "+penggunaan[i][3])
    
def tiket_pemain(tiket,wahana): #CLEAR
    '''
    procedure tiket_pemain menampilkan jumlah tiket yang dimiliki pemain tertentu
    Format tampilan : ID_wahana | Nama_Wahana | Jumlah Tiket
    I.S data kepemilikan tiket tersimpan dalam sebuah array
    F.S ditampilkan seluruh tiket yang dimiliki oleh pemain dengan username sesuai input
    '''
    uname = input("Masukkan Username: ")

    baris = hitung_baris(tiket)

    print("Riwayat: ")
    for i in range(baris):
        if ((tiket[i][0]==uname) and (int(tiket[i][3])!=0)):
            cek, j = cari_wahana(wahana,tiket[i][2])
            print(tiket[i][2]+" | "+wahana[j][1]+" | "+tiket[i][3])

def upgrade_gold(user): #CLEAR
    '''
    fungsi upgrade_gold mengubah status subscription dari user dengan cara membayar sejumlah 500000
    setelah memiliki akun gold, maka username terkait mendapatkan fasilita setengah harga
    input: username

    I.S data user tersimpan dalam array
    Proses: saldo user yang akan diupgrade dikurangi 500000
    F.S data user dalam array di update dengan status subscriptionn plan user yang baru 

    '''
    username = input("Masukkan username: ")

    i = 0
    while (user[i][3]) != username:
        i = i + 1

    saldo=int(user[i][6])

    if (((saldo-500000) >= 0) and (user[i][7]!='gold')):
        user[i][6] = str(saldo-500000)
        user[i][7] = "gold"
        print("Akun Anda telah diupgrade.")
    elif ((user[i][7]=='gold')):
        print("Anda sudah memiliki akun gold.")
    else:
        print("Saldo anda tidak cukup untuk upgrade.")

    return user

def tiket_hilang(tiket,kehilangan):
    '''
    Fungsi tiket_hilang menerima laporan kehilangan tiket dari user
    input : username,tanggal, id_wahana, dan jumlah_tiket.
    jika tiket terkait ada, maka tiket hilang akan disimpan ke dalam array kehilangan dan 
    tiket terkait di array tiket dikurangi.

    I.S data tiket_hilang tersedia di dalam sebuah array
    F.S data tiket hilang input dari user disimpan di dalam array tiket_hilang

    '''
    username = input("Masukkan Username: ")
    tanggal = input("Tanggal kehilangan tiket: ")
    id_wahana = input("ID wahana: ")
    jml_tiket = int(input("Jumlah tiket yang hilang: "))

    baris_tiket = hitung_baris(tiket)

    adr_tiket = cari_tiket(tiket,username,id_wahana)

    if (adr_tiket!=0):
        tiket[adr_tiket][3]=str(int(tiket[adr_tiket][3])-jml_tiket)

        content = [username,tanggal,id_wahana,jml_tiket]
        print("Laporan kehilangan tiket Anda telah direkam.")

        i=0
        while (kehilangan[i]!=None):
            i+=1
        kehilangan[i]=content
    else:
        print("Anda tidak memiliki tiket terkait.")
    
    return tiket,kehilangan
        
def cari_tiket(tiket,username,id_wahana):
    '''
    Fungsi cari_tiket adalah fungsi tambahan untuk membantu fungsi tiket_hilang
    dalam memastikan apakah username pelapor memiliki tiket terkait atau tidak.
    fungsi mengembalikan address dari tiket terkait atau 0 jika tidak ada tiket terkait.
    '''
    cek=False
    i=0
    while (tiket[i]!=None and not(cek)):
        if (tiket[i][0]==username and tiket[i][2]==id_wahana):
            cek = True
        else:
            i+=1
    if cek:
        return(i)
    else:
        return(0)

def best_wahana(pembelian,wahana):
    '''
    Procedure best_wahana menampilkan 3 wahana terbaik berdasarkan
    jumlah penjualan tiket
    I.S data pembelian tiket wahana tersimpan di dalam sebuah array
    F.S Ditampilkan 3 identitas wahana dengan pembelian terbanyak
    '''
    baris_wahana = hitung_baris(wahana)
    baris_pembelian = hitung_baris(pembelian)

    rankArray = [None for i in range(baris_wahana)]

    for i in range(1,baris_wahana):
        count=0
        for j in range(1,baris_pembelian):
            if (wahana[i][0]==pembelian[j][2]):
                count+=int(pembelian[j][3])
        content = [wahana[i][0],wahana[i][1],count]
        k=0
        while (rankArray[k]!=None):
            k+=1
        rankArray[k]=content

    baris_rank = hitung_baris(rankArray)


    for i in range(baris_rank):
        idx_max=i
        for j in range(i+1, baris_rank):
            if rankArray[idx_max][2] < rankArray[j][2]:
                idx_max = j
        rankArray[i],rankArray[idx_max] = rankArray[idx_max],rankArray[i]
    

    for i in range(3):
        idx=str(i+1)
        print(idx+" | "+rankArray[i][0]+" | "+rankArray[i][1]+" | "+str(rankArray[i][2]))

def welcomescreen():
    print("===========================================")
    print("                                           ")
    print("                                           ")
    print("Selamat datang di Willy Wangky's Theme Park")
    print("                                           ")
    print("                                           ")
    print("===========================================")

def display_pemain():
    '''
    Procedure display menu pemain
    '''
    print("===========================================")
    print("                MENU PEMAIN                ")
    print("===========================================")
    print("1. Pencarian Wahana")
    print("2. Pembelian Tiket")
    print("3. Menggunakan Tiket")
    print("4. Refund")
    print("5. Kritik Saran")
    print("6. Lihat Best Wahana")
    print("7. Lapor Kehilangan Tiket")
    print("8. Exit")
    print("===========================================")

def display_admin():
    '''
    Procedure display menu admin
    '''
    print("===========================================")
    print("                 MENU ADMIN                ")
    print("===========================================")
    print("1. Sign Up User")
    print("2. Pencarian Pemain")
    print("3. Pencarian Wahana")
    print("4. View Kritik Saran")
    print("5. Menambahkan Wahana Baru")
    print("6. Top Up saldo")
    print("7. Upgrade Golden Account")
    print("8. Lihat Riwayat Penggunaan Wahana")
    print("9. Lihat Jumlah Tiket Pemain")
    print("10. Exit")
    print("===========================================")

def menu_admin(user,wahana,pembelian,penggunaan,tiket,refund,kritiksaran,kehilangan):
    '''
    Procedure menu admin
    '''
    
    status = True
    while (status):
        display_admin()
        flag = int(input("Pilih: "))
        if (flag==1):
            user = signup(user)
            input("Press any key...")
        elif (flag==2):
            cari_pemain(user)
            input("Press any key...")
        elif (flag==3):
            cari(wahana)
            input("Press any key...")
        elif (flag==4):
            lihat_laporan(kritiksaran)
            input("Press any key...")
        elif (flag==5):
            wahana = tambah_wahana(wahana)
            input("Press any key...")
        elif (flag==6):
            user = topup(user)
            input("Press any key...")
        elif (flag==7):
            user = upgrade_gold(user)
            input("Press any key...")
        elif (flag==8):
            riwayat_wahana(penggunaan)
            input("Press any key...")
        elif(flag==9):
            tiket_pemain(tiket,wahana)
            input("Press any key...")
        elif (flag==10):
            exit(user,wahana,pembelian,penggunaan,tiket,refund,kritiksaran,kehilangan)
            status=False

def menu_pemain(user,wahana,pembelian,penggunaan,tiket,refund,kritiksaran,kehilangan,id_user):
    '''
    Procedure menu pemain
    '''
    status=True
    while status:
        display_pemain()
        flag = int(input("Pilih: "))
        if (flag==1):
            cari(wahana)
            input("Press any key...")
        elif (flag==2):
            tiket,pembelian,user = beli_tiket(user,wahana,id_user,pembelian,tiket)
            input("Press any key...")
        elif (flag==3):
            penggunaan,tiket = main(user,id_user,penggunaan,tiket)
            input("Press any key...")
        elif (flag==4):
            refund,tiket = frefund(user,wahana,refund,tiket,id_user)
            input("Press any key...")
        elif (flag==5):
            kritiksaran = kritik_saran(user,id_user,kritiksaran)
            input("Press any key...")
        elif (flag==6):
            best_wahana(pembelian,wahana)
            input("Press any key...")
        elif (flag==7):
            tiket,kehilangan = tiket_hilang(tiket,kehilangan)
            input("Press any key...")
        elif (flag==8):
            exit(user,wahana,pembelian,penggunaan,tiket,refund,kritiksaran,kehilangan)
            status=False

#MAIN PROGRAM
nMax=201

main_user=[None for i in range(nMax)]
main_wahana=[None for i in range(nMax)]
main_pembelian=[None for i in range(nMax)]
main_penggunaan=[None for i in range(nMax)]
main_tiket=[None for i in range(nMax)]
main_refund=[None for i in range(nMax)]
main_kritiksaran=[None for i in range(nMax)]
main_kehilangan=[None for i in range(nMax)]

welcomescreen()
main_user, main_wahana, main_pembelian, main_penggunaan, main_tiket, main_refund, main_kritiksaran, main_kehilangan = load()
id_user = login(main_user)
role = cek_role(id_user,main_user)
if (role=='admin'):
    menu_admin(main_user, main_wahana, main_pembelian, main_penggunaan, main_tiket, main_refund, main_kritiksaran, main_kehilangan)
else:
    menu_pemain(main_user, main_wahana, main_pembelian, main_penggunaan, main_tiket, main_refund, main_kritiksaran, main_kehilangan,id_user)


