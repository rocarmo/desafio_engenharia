# shellcheck disable=SC2046

echo "Iniciando varredura de containers..."

if [ -z $(docker ps | grep 'desafio' | awk '{ print $1 }') ] || [ -z $(docker images | grep 'desafio') ]
then
  echo "Não há containers para limpar"
else
  echo "Limpando containers encontrados..."
  docker rm -f $(docker ps | grep 'desafio' | awk '{ print $1 }')
  echo "Varredura de containers finalizada!"
  echo "Iniciando varredura de imagens..."
  docker rmi -f desafio_engenharia
  echo "Varredura finalizada."
fi