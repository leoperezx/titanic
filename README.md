# Machine Learning Sample

### Ejercicio de practica tomado de [Kaggle](https://www.kaggle.com)

Se descarga la información de la pagina de Kaggle.com la cual contiene tres archivos:
`train.csv`
`test.csv`
`gender_submission.csv`

### Replico el procedimiento de [@Aladdin Persson](https://www.youtube.com/watch?v=pUSi5xexT4Q&t=925s)

En este canal de youtube, *Aladdin Persson* explica muchos temas de machine learning utililzando Python.
Dentro de las operaciones realizadas se encuentran:
- Carga de los archivos train.csv y test.csv.
- Comprobar los dataframe.
- Crear la función *clean* (retiar columnas que no se usan y rellena valores en blanco).
- Utiliza la librería *sklearn* para el *machine learning* en python.
- Con la *sklearn* reemplaza los valores cualitativos nominales por unos cuantitativos.
	- La asignación para la columna "Sex" es la siguiente: `["Female","Male"] => ["0","1"]`
	- La asignación para la columna "Embarked" es la siguiente: `["C","Q","S","U"] =>["0","1","2","3"]`
- Data frame limpio y listo para usar. Se imprime para su comprobación.
