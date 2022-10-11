import lanches
   codigo, quantidade = imput().split('')
   codigo = int (codigo)
   quantidade = int (quantidade)

  
    {
      "codigo": 1,
      "especificacao": "cachorro quente"
      "preco": 4,00
    },

    {
      "codigo": 2,
      "especificacao": "X-salada"
      "preco": 4,50
    },

    {

      "codigo": 3,
      "especificacao": "X-Bacon",
      "preco": 5,00
    }

    {
      "codigo": 4,
      "especificacao": "Torrada simples",
      "preco": 2,00
    }

    {
      "codigo": 5,
      "especificacao": "refrigerente",
      "preco": 1,50
    }

   
      Lanches = [...]
      soma = lanches[codigo-1] ["preco"]* quantidade

      print("total: R${:2.F}".format(soma))

