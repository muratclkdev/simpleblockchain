import datetime,hashlib,json,itertools

chain= ["murat"]
transaction = ["genesis block has been started"]

while True:
    menu = input('''Yapmak istediğiniz işlemi seçiniz\n 
             1.Yeni blok ekle \n
             2.Zincir hashlerini görüntüle \n
             3.Zincir verilerini görüntüle \n
             4.Çıkış\n''')
    if menu == "1":
        text= input("Veri girişi \n")
        for nonce in itertools.count(start=0):
            block = {'index': len(chain) + 1,
                     'timestamp': str(datetime.datetime.now()),
                     'data': text,
                     'nonce': nonce ,
                     'previous_hash': chain[-1] }
            block = json.dumps(block)
            hash_object = hashlib.sha256(block.encode('utf-8'))
            block_hash = hash_object.hexdigest()
            if block_hash[:4] == "0000":
                chain.append(block_hash)
                transaction.append(block)
                print (block_hash + " \n --------------------- \n" + block )
                print("Ana menüye dönülüyor...")
                break
            else :
                continue

    elif menu == "2":
        for i in range (0,len(chain)):
            print(str(i+1) + ".Blok hashi \n" + str(chain[i]) + "\n -----------------")
            i++1
    elif menu == "3":
        for i in range (0,len(transaction)):
            print(str(i+1) + ".Blok verisi \n" + str(transaction[i]) + "\n -----------------")
            i++1
    elif menu == "4" :
        print("Çıkış yapılıyor...")
        break
    else:
        print("Yanlış tuşlama")
