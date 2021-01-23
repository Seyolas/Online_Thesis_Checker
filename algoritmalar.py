import io
import docx

def içerik_hesapla(dosya):
    output = '''\nTezin İçeriği Ve Konusu:
\n'''
    output += dosya[0] + "\n" + dosya[1] + "\n" + dosya[2] + "\n" + dosya[3] + "\n" + dosya[4] + "\n" + dosya[5]+"\n"+"\n"
    return output
def önsözde_tşk_varmı(dosya):
    output = '\n'
    if "ÖN SÖZ" in dosya:#Bazı insanlar önsöz kelimesini ayrı yazdığı için bunun olup olmadığını kontrol ediyoruz.
        for i in range(dosya.index("ÖN SÖZ"), dosya.index("ÖN SÖZ") + 1):# Önsöz'ün ilk paragrafında teşekkür olup olmadığına bakıyoruz.
            if "teşekkür" or "teşekkürü" or "teşekkürlerimi" in dosya[1]:
                output += "Önsöz yazısının ilk paragrafında teşekkür bulunuyor! \n"
            else:
                output += "önsözde hata bulunamadı.('İlk paragrafta teşekkür bulunmuyor.') \n"
    elif ("TEŞEKKÜR") in dosya:#Bazı insanlarda önsöz yerine başlık olarak teşekkür yazmış bunun için uyarı veriyoruz.
        for i in range(dosya.index("TEŞEKKÜR"), dosya.index("TEŞEKKÜR") + 1):
            output += "Tezinizde ayrı bir 'TEŞEKKÜR' alanı bulunmamalıdır! 'ÖNSÖZ' içinde yer vermeniz gerekir. \n"
    elif ("ÖNSÖZ / TEŞEKKÜR") in dosya:
        for i in range(dosya.index("ÖNSÖZ / TEŞEKKÜR"), dosya.index("ÖNSÖZ / TEŞEKKÜR") + 1):
            output += "Tezinizde ayrı bir 'TEŞEKKÜR' alanı bulunmamalıdır! 'ÖNSÖZ' içinde yer vermeniz gerekir. \n"
    elif ("ÖNSÖZ/TEŞEKKÜR") in dosya:
        for i in range(dosya.index("ÖNSÖZ/TEŞEKKÜR"), dosya.index("ÖNSÖZ/TEŞEKKÜR") + 1):
            output += "Tezinizde ayrı bir 'TEŞEKKÜR' alanı bulunmamalıdır! 'ÖNSÖZ' içinde yer vermeniz gerekir. \n"

    else:
        for i in range(dosya.index("ÖNSÖZ"), dosya.index("ÖNSÖZ") + 1):
            if "teşekkür" in dosya[1]:
                output += "Önsöz yazısının ilk paragrafında teşekkür olmamalı!"
            else:
                output += "önsözde hata bulunamadı.('İlk paragrafta teşekkür bulunmuyor.')"

    return output+"\n"
def giriş_son_bölüm(dosya):#Gözlemlerime göre giriş kısmını yazmayanlar direkt bu kategoride.
    output = '\n'
    if "GİRİŞ" in dosya:
        output += "Giriş bölümünün son paragrafında tezin organizasyonu ve kapsamına yer verilmiştir. \n"
    else:
        output += "Giriş içeriğinde tezin organizasyonu ve kapsamı hakkında yeterli bilgi bulunmamaktadır. \n"
    return output+"\n"
def şekil_sayısı(dosya):
    dizi = []
    output = "\n"
    if "ŞEKİLLER LİSTESİ" not in dosya:
        output+="Tezinizde 'ŞEKİLLER LİSTESİ' bulunmuyor."
        return output + "\n"
    elif "TABLOLAR LİSTESİ" not in dosya:
        output+="Tezinizde 'TABLOLAR LİSTESİ' bulunmuyor."
        return output + "\n"
    else:
        for i in range(dosya.index("ŞEKİLLER LİSTESİ"), dosya.index("TABLOLAR LİSTESİ")):
            dizi.append(i)
        x=len(dizi)
        if x==0:
            output+="Lütfen gereken kurallara uyarak önce 'ŞEKİLLER LİSTESİ' ardından 'TABLOLAR LİSTESİ'ni yazınız."
            return output+"\n"
        return len(dizi)-2, "adet şekil bulunmaktadır."
def tablo_sayısı(dosya):
    dizi = []
    output = "\n"
    if "EKLER LİSTESİ" not in dosya:
        output += "Tezinizde 'EKLER LİSTESİ' bulunmuyor."
        return output + "\n"
    else:
        for i in range(dosya.index("TABLOLAR LİSTESİ"), dosya.index("EKLER LİSTESİ")):
            dizi.append(i)
        x = len(dizi)
        if x == 0:
            output += "Lütfen gereken kurallara uyarak 'ŞEKİLLER LİSTESİNDEN' önce 'TABLOLAR LİSTESİ' ardından 'EKLER LİSTESİ'ni yazınız."
            return output + "\n"
        return len(dizi) - 2, "adet tablo bulunmaktadır."
def kaynak_sayısı(dosya):
    dizi = []
    output = "\n"
    if "EKLER" not in dosya:
        try:
            for i in range(dosya.index("KAYNAKLAR"), dosya.index("ÖZGEÇMİŞ")):
                dizi.append(i)
            return len(dizi), "adet kaynak bulunmaktadır."
            return " "

        except ValueError:
            output += '''Tezinizde  KAYNAKLAR bölümünden sonra gelmesi gereken 'EKLER' içeriğinin bulunmadığını tespit ettik.(Bu düzeltmeniz gereken bir hata değildir) \n
                  Fakat 'EKLER' bölümünü kullanmadıysanız KAYNAKLAR bölümünden sonra ÖZGEÇMİŞ bilgilerinizi yazmanız gerekir.\n
                  Zaten ÖZGEÇMİŞ bilgilerinizi yazdıysanız lütfen başlık kısmını ÖZGEÇMİŞ yapınız.(Aksi takdirde bu hatayı almaya devam edeceksiniz ve kaynak sayınızı hesaplayamayacağız.)\n'''
    else:

        for i in range(dosya.index("KAYNAKLAR"), dosya.index("EKLER")):# kaynaklar ile ekler kısımları arasındaki her bir paragrafı bir diziye ekleyip dizinin
            dizi.append(i)                                              #uzunluğunu yani kaynak sayısını elde ediyoruz
        return len(dizi), "adet kaynak bulunmaktadır."
        return " "
    return output+"\n"
def kaynak_istatistik(dosya):# internet sitelerini herkes kopyala yapıştır yaptığı için başlarında her zaman 'https' kelimesi bulunuyor. Bunların sayını hesaplamak yeterli.
    matching = [s for s in dosya if "http" in s]
    if len(matching)==0:
        return "kaynaklarda hiç internet sitesi bulunmuyor."
    else:
        return "kaynakların ", len(matching), "tanesi internet sitesidir."

def blok_atıf(dosya):
    output = '\n'
    dizi = []
    char = []
    blok = list()
    s = "s"
    for i in dosya:
        dizi.append(i)
    for i in dizi:
        char.extend(i)

    for i in range(len(char)):
        if char[i] == "-":
            try:
                if char[i + 1] == "]":
                    blok.append(1)
                elif char[i + 2] == "]":
                    blok.append(1)
                elif char[i + 3] == "]":
                    blok.append(1)
                elif char[i + 4] == "]":
                    blok.append(1)
                else:
                    continue
            except IndexError:
                continue


    if len(blok)==0:
        output+="Tezinizde blok atıf verme bulunamadı\n"
        return output
    else:
        output+="Tezinizde blok atıf verme var ! \n"
        return output

def to_txt(document, TFN):  # Geçiçi Dosya ismi
    with io.open(TFN, "w+", encoding="utf-8") as of:  # stands for an OutputFile

        # fonksiyonlarda outputları okuyup sırayla temp.txt dosyasına yazıyoruz.
        of.write(str(içerik_hesapla(document)))
        of.write(str(önsözde_tşk_varmı(document)))
        of.write(str(giriş_son_bölüm(document)))
        of.write(str(şekil_sayısı(document)))
        of.write(str(tablo_sayısı(document)))
        of.write(str(kaynak_sayısı(document)))
        of.write(str(kaynak_istatistik(document)))
        of.write(str(blok_atıf(document)))


def process(filename):# word dosyasını ön işlemden geçiriyoruz.
    doc = docx.Document(filename)
    result = [p.text for p in doc.paragraphs]#docx kütüphanesini kullanarak her bir paragrafı bir dizi elemanı olarak diziye atıyoruz.
    result = list(filter(None, result))# result değişkenindeki boş karakterleri siliyoruz.


    for i in result: #sayfa numaralarını ve tek(harf,rakam,simge,şekil) stringlerin birer eleman olarak anılmaması için siliyoruz.
        if len(i) == 2 and i.isnumeric() or len(i) == 1:
            result.remove(i)

    if "KAYNAKÇA" in result:#Kaynak sayısını hesaplayabilmemiz için başlangıç değerimiz 'KAYNAKLAR' stringi olacak. Bazı insanlar 'kaynakça' yazıyor bunu değiştiriyoruz.
        result = [i.replace("KAYNAKÇA", "KAYNAKLAR") for i in result]

    to_txt(result, filename + '.txt')

    return filename + '.txt'