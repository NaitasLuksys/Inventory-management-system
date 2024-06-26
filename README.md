## Kursinio darbo tikslas

- Įgytas teorines žinias pritaikyti praktikoje.
- Savarankiškai atrasti papildomus šaltinius ir juose esančią informaciją pritaikyti programoje.

## Tema - *Inventory management system*

Tema yra susijusi su parduotuvės prekių kiekio papildymu naujomis prekėmis. Šioje programoje dirbama būtent su elektroninių prekių inventoriumi - mobilieji telefonai ir nešiojami kompiuteriai.

**Programos principas:**
Ši programa suteikia struktūrinį inventoriaus prekių valdymo metodą, leidžiantį pridėti naujų produktų, taikyti nuolaidas ir saugoti produktų informaciją keliuose failuose. Tai demonstruoja objektinio programavimo, failų tvarkymo ir vartotojo sąveikos principus.

##### Visa informacija apie prekes yra saugoma skirtinguose failuose:
- Faile **Smartphones.txt** yra saugoma informacija tik apie mobiliuosius telefonus *(prekės ID, telefono prekės ženklas, telefono vidinė atmintis, modelis, spalva, kaina, kiekis)*
- Faile **Laptops.txt** yra saugoma informacija tik apie nešiojamus kompiuterius *(prekės ID, kompiuterio prekės ženklas, kaina, kiekis)*
- Faile **AllProducts.txt** yra saugoma viso inventoriaus informacija, šiuo atveju, visų mobiliųjų telefonų bei nešiojamų kompiuterių informacija kartu.

**Kaip naudotis programa:**
Paleidus programą, naudotojas konsolėje turi pasirinkti, kokį veiksmą nori atlikti:

![Reference image](/screenshots/Pirma.png)
- Jei reikia pridėti naują prekę, pasirenkama pirma operacija, įvedant **1**. Toliau reikia pasirinkti kokią prekė yra pridedama, o jei naudotojas nori išeiti iš šios operacijos, konsolėje įvesti **exit**

![Reference image](/screenshots/antra.png)
- Jei naudotojas nori atlikti antrąją operaciją, įvedamas skaičius **2** ir tuomet įvedamas prekės 'ID', pvz.: *ID1236*
Tačiau, jei naudotojas nori išeiti iš šios operacijos konsolėje įvesti **exit**

![Reference image](/screenshots/trecia.png)
Įvedus 'ID', įvedamas nuolaidos dydis dešimtaine trupmena (10% atitinka 0.1):

![Reference image](/screenshots/ketvirta.png)
- Jei naudotojas nori galutinai išeiti iš programos, įvedamas skaičius **3**. Tuomet, jei buvo tokių prekių, kurioms buvo pritaikytos nuolaidos, jos yra atspausdinamos išeinant iš programos:

![Reference image](/screenshots/penkta.png)

## Programos analizė
### OOP Principai:
- **Polimorfizmas** - pagridninė objektinio programavimo koncepcija, kuri yra pasiekiama, kai operacija (metodas) gali būti vykdoma skirtingai, priklausomai nuo konkrečios klasės realizacijos. Tai pasiekiama aprašant metodus bazinėje klasėje ir perrašant atitinkamus metodus paveldinčiose klasėse.

Programoje *Inventory Management System* polimorfizmas yra naudojamas keliais metodais:
1. **Metodas get_product_info():**
Metodas aprašomas abstrakčioje klasėje **Product**, o vaikinės klasės **Smartphones** ir **Laptops** perrašo ši metodą taip, kad atitiktų tos klasės reikalavimus ir tinkamai pateiktų informaciją apie tos klasės produktą. Polimorfizmo taikymas šiam metodui atrodo taip:
```python
    for product in products:
        product_info = product.get_product_info()
        file.write(", ".join(map(str, product_info)) + "\n")
        file.write("\n")
 # Kai šis metodas yra iškviečiamas, jis yra vykdomas pagal keikvieno produkto tipą. Pavyzdžiui, jei product yra Smartphones objektas, bus naudojama Smartphones klasės realizacija, o jei product yra Laptops objektas, bus naudojama Laptops klasės realizacija. 
```
2. **Metodas apply_discount():**
Metodas aprašomas abstrakčioje klasėje **Product**, o vaikinės klasės **Smartphones** ir **Laptops** perrašo ši metodą taip, kad taikytų nuolaidą konkrečiam produkto tipui. Polimorfizmo taikymas šiam metodui atrodo taip:
```python
    for product in factory._products:
        if product._product_id == product_id:
            selected_product = product
            break
    if selected_product is not None:
        selected_product.apply_discount(discount)
        print("Discount applied successfully!")
        inventory.apply_discount_to_selected_products(selected_product)
# Šioje vietoje apply_discount() metodas yra kviečiamas kiekvienam produkto objektui. Kadangi metodas perrašytas vaikinėse klasėse tai jis bus vykdomas, pagal konkretų objektą.

    def apply_discount_to_selected_products(self, product):
        product._price = product._discounted_price
        self._discounted_products.append(product)
 # Šis metodas gali priimti tiek Smartphones, tiek Laptops klasių objektus ir pritaikyti nuolaidą atsižvelgiant į kiekvieno produkto realizaciją.
```
- **Abstrakcija** - Python programavimo kalboje abstrakcija paslepia sudėtingas funkcijas ir detales, kurių nereikia naudotojui. Abstrakcija programoje:
```python
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, quantity):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity = quantity

    @abstractmethod
    def get_product_info(self):
        pass

    @abstractmethod
    def apply_discount(self, discount):
        pass
```
**Product** yra abstrakti bazinė klasė, turinti abstrakčius metodus *get_product_info()* ir *apply_discount()*. Abstrakčios klasės leidžia apibrėžti bendras savybes ir funkcionalumą, bet konkrečias implementacijas palieka paveldinčioms klasėms.

- **Paveldėjimas** - Python kalboje paveldėjimas suteikia galimybę sukurti naujas 'vaikines' klases, kurios paveldi visus metodus ir savybes iš 'tėvinės' klasės. Tokiu būdu, paveldėjusios klasės gali naudoti bei praplėsti 'tėvinės' klasės funkcionalumą, o jau egzistuojančių atributų nebereikia iš naujo apibrėžti. Be to, naudojantis paveldėjimu, išvengiama kodo kopijavimo.
```python
class Laptops(Product):
    additional_properties = []

    def get_product_info(self):
        base_info = [self._product_id, self._name, f"{self._price} €", self._quantity]
        return base_info

    def apply_discount(self, discount):
        self._discounted_price = self._price - (self._price * discount)

class Smartphones(Product):
    additional_properties = ['gb', 'model', 'color']

    def __init__(self, product_id, name, price, quantity, gb=None, model=None, color=None):
        super().__init__(product_id, name, price, quantity)
        self._gb = gb
        self._model = model
        self._color = color
        self._discounted_price = None
    def get_product_info(self):
        base_info = [self._product_id, self._name, self._gb, self._model, self._color, f"{self._price} €", self._quantity]
        return base_info
    
    def apply_discount(self, discount):
        self._discounted_price = self._price - (self._price * discount)
```
Klasės **Smartphones** ir **Laptops** paveldi bazinės klasės **Product** atributus, metodus bei juos realizuoja pagal poreikį. Metodai: *get_product_info* ir *apply_discount* yra pritaikomi būtent šioms klasėms, o klasė **Smartphones** prie paveldėtų bazinės klasės atributų prideda jai būdingus atributus.

- **Inkapsuliacija** - Inkapsuliavimas yra viena iš pagrindinių objektinio programavimo koncepcijų. Jame aprašoma duomenų apjungimo idėja ir metodai, kurie veikia su duomenimis viename vienete (klasėje). Tai apriboja tiesioginę prieigą prie kintamųjų ir metodų ir gali užkirsti kelią atsitiktiniam duomenų pakeitimui. Inkapculiacija paslepia duomenis ir jei tų duomenų reikia kitoms klasėms, jos iš pradžių turi kreiptis į tas klases, kurios turi šiuos duomenis. **'Protected'** tipo nariai negali būti pasiekiami už klasės ribų, tačiau jie gali būti pasiekiami iš pačios klase ar jos poklasių. **'Private'** tipo nariai yra panašūs į **'Protected'** narius, skirtumas yra tas, kad klasės nariai, apibrėžti kaip **'Private'**, neturėtų būti prieinami nei klasėje, nei jokia bazinė klasė.
Šioje programoje visi **Product** klasės atributai yra **'Protected'** tipo, tam, kad būtų išvengta tiesioginio duomenų keitimo.
```
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity = quantity
```
### Dizaino šablonai:
- **Singleton Pattern** - šis dizaino šablonas užtikrina, kad būtų sukurtas tik vienas klasės egzempliorus ir suteikia globalinę prieigą prie jo. Šis **'design pattern'** yra panaudotas ir aprašytas dviejose klasėse: **Inventory** ir **ProductFactory**. **Inventory** klasė užtikrina, kad visoje programoje būtų tik vienas jos egzempliorius. Tai labai svarbu, nes inventorius turi būti nuoseklus visoje sistemoje, nepaisant to, kur į jį yra kreipiamasi. Jei būtų keli egzemplioriai, galėtų kilti inventoriaus duomenų neatitikimai.
```python
class Inventory:
    _instance = None

    def __init__(self):
        if not Inventory._instance:
            Inventory._instance = self
            self._products = []
            self._discounted_products = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
```
Panašiai kaip **Inventory** klasėje, **ProductFactory** klasė įgyvendina **'singleton pattern'**, kad užtikrintų, jog visoje programoje yra tik vienas egzempliorius. Tai būtina, nes **ProductFactory** yra atsakinga už produkto egzempliorių kūrimą, o kelių egzempliorių egzistavimas gali sukelti produkto kūrimo neatitikimų.
```python
class ProductFactory:
    _instance = None

    def __init__(self):
        if not ProductFactory._instance:
            ProductFactory._instance = self
            self._products = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
```
- **Factory Method** - tai yra kūrimo **'design pattern'**, kuris suteikia sąsają superklasės objektams kurti, tačiau leidžia poklasiams keisti kuriamų objektų tipą. **Factory method** kode panaudotas **ProductFactory** klasėje - *create_product()* metodas. Šis metodas suteikia galimybę dinamiškai sukurti skirtingo tipo produktus. Metodas *create_product()* produkto kūrimo procesą padaro abstrakčiu ir taip suteikia lankstumo kode bei palengvina darbą. Su šiuo metodu galima lengvai sukurti naujus produkto tipus, nepakeičiant jau esamo kodo.
```python
    def create_product(self, product_type, *args, **kwargs):
        if product_type == "smartphone":
            product = Smartphones(*args, **kwargs)
        elif product_type == "laptop":
            product = Laptops(*args, **kwargs)
        else:
            raise ValueError("Invalid product type")
        return product
```
## Rezultatai ir apibendrinimas
- Kode panaudoti visi OOP principai, du dizaino šablonai: **Singleton** ir **Factory method**.
- Sukurti TXT tipo failai, įgyti įgūdžiai kaip dirbti su tokiais failais.
- Įgytos žinios kaip taikyti **'unittests'**.
- Daugiausiai sunkumų sukėlė skaitymas iš failų, kadangi kiekviena eilutė faile turi skirtingą kiekį informacijos.

Darydamas šį kursinį įgyjau papildomų žinių apie objektinį programavimą, išmokau rasti ir pritaikyti informaciją iš įvairių šaltinių.
Šią programą galima praplėsti pridedant naujų prekių, sukuriant naujus produktų tipus. Be to, programos funkcionalumą galima dar labiau praplėsti, pritedant klases ir metodus, kurie yra susiję su logistika, pavyzdžiui, klientų informacijos kaupimas, prekių tiekėjų informacijos kaupimas ir darbas su šia informacija.