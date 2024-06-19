'''
CSV = Comma Separated Values(valores separados por comas)
no todos los archivos usan coman podrian usar . | - entre otros 

SEP=""
Al ver el DF extraño debemos checar el CVS con un editor de texto, al identificar el delimitador que se usa se debe especificar con el parametro
SEP="adentro va el caracter que usan para dividir el DataSet"

#### ejemplo: 
#### df = pd.read_csv(data.csv, sep="|")
'''

'''
SIN NOMBRE DE COLUMNAS
Al identificar que las columnas del DF no contienen nombre podremos establecerlas utilizando
NAMES=[Adentro va el nombre de cada columna que se quiere asignar al DataSet]
#### ejemplo:
#### df = pd.read_csv(data.csv, names=['columna1', 'columna2', 'columna3'..... ])

Tambien se puede establecer con el parametro HEADER=NONE
#### df = pd.read_csv(data.csv, header=none)

para despues establecerlo usando el metodo rename:

#### df =df.rename(columns={0(el cero es indexacion):'columna1', 'columna2', 'columna3'.....}) ---> SE USAN LAS LLAVES 


### Tambien podemos definir los nombres de las columnas en una variable utilizando una lista y despues usar el parametro NAMES=llamar a la lista

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv('/datasets/gpp_modified.csv', sep='|', header=None, names=column_names)

print(data.head())
'''

'''
DECIMALES 
Generalmente para utilizar datos float se usa el "." pero en algunos paises se utiliza la COMA como separador de enteros y decimales
por lo cual generara un error ya que python no leera correctamente estos valores por lo cual se debe usar el parametro DECIMAL=","

#### ejemplo:
#### df = pd.read_csv(data.csv, names=['columna1', 'columna2', 'columna3'], decimal=",")
'''