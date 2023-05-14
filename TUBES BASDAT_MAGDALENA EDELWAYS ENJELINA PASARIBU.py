#TUGAS BUKU KONTAK STRUKDAT - BISA

class Node:
    def __init__ (self, data):
        self.prev = None
        self.data = data
        self.next = None

class Doublylist:
    def __init__ (self):
        self.head = None

    #MEMBUAT BUKU KONTAK
    def Nambah_kontak(self, data):
        # Memeriksa apakah list kosong
        if self.head is None:
            newNode = Node(data)
            newNode.prev = None
            self.head = newNode
        # Ketika list tidak kosong
        else:
            newNode = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = None

    #Menghapus kontak
    def Hapus(self):
        temp = input("Masukkan Kontak Yang Akan Dihapus : ")
        # Membuat pointer yang menunjuk ke node pertama
        current_node = self.head
        # Melakukan perulangan saat list tidak kosong
        while current_node is not None:
            # Memeriksa data pada node yang ditunjuk pointer merupakan node yang akan dihapus
            if current_node.data == temp:
                #jika node yang dicari berada pada elemen terakhir
                if current_node.next is None:
                    current_node.prev.next = None
                # jika node yang dicari berada bukan pada elemen per1tama
                elif current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                # Jika node yang dicari berada pada elemen pertama
                else:
                    self.head = current_node.next #memindahkan head ke elemen berikutnya
                    current_node.next.prev = None #menunjuk head prev menjadi none
            # Memindahkan pointer menunjuk ke node berikutnya
            current_node = current_node.next
            
    #Mencari Kontak
    def search(self, value):    
        i = 1;    
        flag = False;    
        #Node current will point to head    
        current = self.head;    
            
        #Checks whether the list is empty    
        if(self.head == None):    
            print("\n! ! ! Buku Kontak Kosong ! ! !\n");    
            return;    
        while(current != None):    
            #Compare value to be searched with each node in the list    
            if(current.data == value):    
                flag = True;    
                break;    
            current = current.next;    
            i = i + 1;    
        if(flag):
            print("Kontak Berada di List : " + str(i))
        else :
            print("Kontak Tidak ada ")

    #Melihat List Kontak
    def Lihatkontak(self):
        if self.head is None:
            print("\n= = = Buku Kontak Kosong = = =\n")
            return
        else:
            no = 0
            # Membuat pointer yang menunjuk ke node pertama
            current = self.head
            print("\n= = = Buku Kontak = = =\n")
            # Perulangan menampilkan data beserta data sebelum dan sesudahnya
            while current is not None:
                no +=1
                print(f"{no}.", current.data)
                # Menunjuk ke node berikutnya
                current = current.next


show = Doublylist()
#menu program
while True:
    print("\n= = = = = = = = = = = = = = = = = = = = = = = =")
    print(" Menu Buku Kontak : ")
    print(" 1.Membuat Buku Kontak")
    print(" 2.Menghapus Kontak ")
    print(" 3.Mencari Kontak")
    print(" 4.Melihat Buku Kontak")
    print(" 0.Keluar")
    print("= = = = = = = = = = = = = = = = = = = = = = = =\n")

    menu = int(input("Pilih Menu : "))
    if menu == 1:
        jumlah = int(input("Masukan Jumlah Buku Kontak : "))
        for i in range(jumlah):
            input_kntk = input(f"Masukkan Kontak ke-{i+1} ( Nama , Nomor ) : ")
            show.Nambah_kontak(input_kntk)
        else:
            print("\n > > Buku Kontak Berhasil di Tambahkan < < \n")

    elif menu == 2:
        show.Hapus()
        print("Data Berhasil Di Hapus ")

    elif menu == 3:
        cari_data = input("Masukkan Kontak yang mau dicari : ")
        show.search(cari_data)

    elif menu == 4:
        show.Lihatkontak()

    elif menu == 0:
        print("\n= = = = Terimakasih Sampai Berjumpa Lagi = = = = \n")
        exit()

    else:
        print("\n! ! ! ! MAAF PILIHAN ANDA TIDAK TERSEDIA DI MENU ! ! ! ! \n")