# Enwau Ffug Cymraeg
Dyma ffeiliau i'w hychwanegu at lyfrgell Faker er mwyn creu enwau personol ac enwau lleoedd Cymraeg a Chymreig ffug.

Byddwn yn eu cyflwyno i lyfrgell Faker yn fuan, ond yn y cyfamser gellir eu hail-enwi fel __init__.py a'u gosod o fewn ffolder cy_GB yn y ffolder 'person' (ar gyfer yr enwau personol) ac yn yr un modd yn y ffolder 'address' ar gyfer yr enwau lleoedd.

## Defnyddio

```
from faker import Faker
fake = Faker('cy_GB')
for _ in range(10):
    print(fake.name())
```

Enghreifftiau:

```
Ms Olwen Dunn
Simon Pugh
Jordan Webb
Anne Davies
Eleri Smith
Edryd Ahmed
Dr Barry Reeves
Charlie Phillips
Leigh Ingram
```

# Fake Welsh Names
These are additional files for the Faker library to enable the creation of fake Welsh-language and geographicaly Welsh personal names and place-names.

They will be submitted to the Faker libray shortly, but in the meantime they can be renamed as __init__.py and placed within a cy_GB folder in the 'person' folder (for the personal names) and likewise in the 'address' folder for the place-names.

## Usage

```
from faker import Faker
fake = Faker('cy_GB')
for _ in range(10):
    print(fake.name())
```

Enghreifftiau:

```
Ms Olwen Dunn
Simon Pugh
Jordan Webb
Anne Davies
Eleri Smith
Edryd Ahmed
Dr Barry Reeves
Charlie Phillips
Leigh Ingram
```
