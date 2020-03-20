error = "ERRORE! Riprova"
num = int(input("Quante volte"))
global frasi
frasi = []
def ask():
    link = input("File o link?")
    if link == "file":
        href="/Sito_Compiti_5F/files/"
        return (href)
    elif link =="link":
        href=""
        return (href)
    else:
        print (error)
        ask()

while num > 0:
    href = str(ask())
    colore =str(input("Scegli un colore (in inglese)    "))
    materia =str(input("Scegli una materia    "))
    titolo =str(input("Scegli un titolo     "))
    autore =str(input("Scegli un autore     "))
    data =str(input("Segli la data      "))
    tipo =str(input("Scegli il tipo di file    "))
    file =str(input("Scrivi il nome del file (con estensione)     "))
    print()
    testo=("| <font color=\""+colore+"\">"+materia+"</font> |"+titolo+"|"+autore+"<br>"+data+"|<a href='"+href+file+"'><img alt='"+tipo+"' width='40 px' src='/Sito_Compiti_5F/resources/"+tipo+".png'>|")
    frasi.append(str(testo))
    num -=1

for x in frasi:
    print(x)
    print()

goodbye = input("Qualunque tasto ti manderà all'inferno")
