# Resolução para # 2 Web Api

Para rodar o app:

1. Crie um ambiente com o virtualenv
```
virtualenv env
```
2. Instale as dependencias do projeto usando requirements.txt
>> pip install -r requirements.txt

3. Ative o ambiente
>> source env/Scripts/activate (para bash)

4. Rode o programa
>> python app.py

Acesse http://localhost:5000/api/doc para ter acesso à documentação Swagger e usar os endpoints ou utilize o navegador ou POSTMAN para realizar as requisições GET e POST com query string, por exemplo: http://localhost:5000/api/residencias?neighbourhood_group=Manhattan
