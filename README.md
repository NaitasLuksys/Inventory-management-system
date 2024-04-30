## Kursinio darbo tikslas

- Įgytas teorines žinias pritaikyti praktikoje.
- Savarankiškai atrasti papildomus šaltinius ir juose esančią informaciją pritaikyti programoje.

## Tema - *Inventory management system*

Tema yra susijusi su parduotuvės prekių kiekio papildymu naujomis prekėmis. Šioje programoje dirbama būtent su elektroninių prekių inventoriumi (mobilieji telefonai ir nešiojami kompiuteriai).

**Programos principas:**
Ši programa suteikia struktūrinį inventoriaus prekių valdymo metodą, leidžiantį pridėti naujų produktų, taikyti nuolaidas ir saugoti produktų informaciją keliuose failuose. Tai demonstruoja objektinio programavimo, failų tvarkymo ir vartotojo sąveikos principus.

##### Visa informacija apie prekes yra saugoma skirtinguose failuose:
- Faile **Smartphones.txt** yra saugoma informacija apie mobiliuosius telefonus *(prekės ID, telefono prekės ženklas, telefono vidinė atmintis, modelis, spalva, kaina, kiekis)*
- Faile **Laptops.txt** yra saugoma informacija apie nešiojamus kompiuterius *(prekės ID, kompiuterio prekės ženklas, kaina, kiekis)*
- Faile **AllProducts.txt** yra saugoma viso inventoriaus informacija, šiuo atveju, visų mobiliųjų telefonų bei nešiojamų kompiuterių informacija kartu.

**Kaip naudotis programa:**
Paleidus programą, naudotojas konsolėje turi pasirinkti, kokį veiksmą nori atlikti:

![Reference image](/screenshots/Pirma.png)
- Jei reikia pridėti naują prekę, pasirenkama pirma operacija - įvedant **1**. Toliau reikia pasirinkti kokią prekė yra pridedama, o jei naudotojas nori išeiti iš šios operacijos, konsolėje įvesti: **exit**

![Reference image](/screenshots/antra.png)
- Jei naudotojas nori atlikti antrąją operaciją, įvedamas skaičius **2** ir tuomet įvedamas prekės 'ID', pvz.: *ID1236*
Tačiau, jei naudotojas nori išeiti iš šios operacijos konsolėje įvesti **exit**

![Reference image](/screenshots/trecia.png)
Įvedus 'ID', įvedamas nuolaidos dydis dešimtaine trupmena 10% atitinka 0.1:

![Reference image](/screenshots/ketvirta.png)
- Jei naudotojas nori galutinai išeiti iš programos, įvedamas skaičius **3**. Tuomet, jei buvo tokių prekių, kurioms buvo pritaikytos nuolaidos, jos yra atspausdinamos išeinant iš programos:

![Reference image](/screenshots/penkta.png)

## Programos analizė

