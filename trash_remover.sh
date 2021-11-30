# shellcheck disable=SC2046

echo "Iniciando varredura de containers..."

if [ -z $(docker images | grep 'desafio' | awk '{ print $1 }') ]
then
  echo "Não há containers para limpar"
else
  echo "Iniciando limpeza de ambiente..."

  if [ -z  $(docker ps | grep 'desafio' | awk '{ print $1 }') ]
  then
    echo "Nenhum container foi encontrado, limpando apenas imagens..."
  else
    echo "Container encontrado, realizando a limpeza..."
    docker rm -f $(docker ps | grep 'desafio' | awk '{ print $1 }')
    echo "Limpeza de containers realizada."
  fi
  echo "Deletando imagens encontradas..."
  docker rmi -f desafio_engenharia
  echo "Varredura finalizada."
fi