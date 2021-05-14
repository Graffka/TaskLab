import csv

f = open('generat1.log')
a='2021-04-19T04:55:57'
b='2021-04-19T04:56:00'
in_in='wanna top up'
out_out='wanna scoop'

in_in_popytki_nalit=0
in_in_procent_eror=0
in_in_volume_nalit=0
in_in_volme_ne_nalit=0

out_out_popytki_nalit=0
out_out_procent_error=0
out_out_volume_zabrali=0
out_out_volume_ne_zabrali=0

Volume_start=0
Volume_finish=0

i=0

Volume=0
Balance=0
for line in f:
    text=line
    if i==1: #устанавливаем объем
        Volume=int(line)
        print(Volume)
    elif i==2:
        Balance=int(line) #устанавливаем остаток в бочке
        print(Balance)
    else:
        if in_in in text: #пытаемся налить воды

            in_in_popytki_nalit = in_in_popytki_nalit+1


            test=int(line[line.rfind(" ")+1:line.rfind("l")])
            if Balance+test <= Volume:
                Balance=Balance+test
                in_in_volume_nalit = in_in_volume_nalit+test
            else: in_in_volme_ne_nalit = in_in_volme_ne_nalit+test
            print(Balance)
        if out_out in text: #пытаемся набрать воды

            out_out_popytki_nalit = out_out_popytki_nalit+1




            test = int(line[line.rfind(" ") + 1:line.rfind("l")])
            if Balance-test >= 0:

                Balance=Balance-test
                out_out_volume_zabrali = out_out_volume_zabrali+test
            else: out_out_volume_ne_zabrali = out_out_volume_zabrali+test
            print(Balance)

    if a in text: #начало
        in_in_popytki_nalit = 0
        in_in_procent_eror = 0
        in_in_volume_nalit = 0
        in_in_volme_ne_nalit = 0

        out_out_popytki_nalit = 0
        out_out_procent_error = 0
        out_out_volume_zabrali = 0
        out_out_volume_ne_zabrali = 0
    if b in text:
        myData = [["popytkiNalit", "ProcentEror", "VolumeNalit", "VolumeNeNalit", "PopytkiZabrat", "ProcentEror", "VolumeZabrali", "VolumeNeZabrali"],
                  [in_in_popytki_nalit, in_in_procent_eror, in_in_volume_nalit, in_in_volme_ne_nalit, out_out_popytki_nalit, out_out_procent_error, out_out_volume_zabrali, out_out_volume_ne_zabrali]]

        myFile = open('task3.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)

        print("Writing complete")



    i=i+1

in_in_procent_eror = 0
out_out_procent_error = 0

if __name__ == "__main__":


    print(Point(*sys.argv[1:]))