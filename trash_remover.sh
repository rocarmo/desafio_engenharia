# shellcheck disable=SC2046

echo "Iniciando varredura de containers..."

if [ -z $(docker ps | grep 'desafio' | awk '{ print $1 }') ]
then
  echo "Não há containers para limpar"
else
  echo "Limpando containers encontrados..."
  docker rm -f $(docker ps | grep 'desafio' | awk '{ print $1 }')
fi

echo "Varredura de containers finalizada!"
echo "Iniciando varredura de imagens..."
if docker rmi -f desafio_engenharia
then
  echo "Imagem desafio_engenharia deletada com sucesso!"
else
  echo "Não foi encontrado imagens para apagar"
fi

echo "Fim do script"