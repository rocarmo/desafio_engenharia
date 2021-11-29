import docker

def print_hi():
    client = docker.from_env()
    all_contaiers = client.containers.list()
    container = client.containers.get('jenkins-blueocean')
    image = client.images.list()
    print(image)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
