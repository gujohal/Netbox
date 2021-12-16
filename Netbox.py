import os



def redis_Netbox():
    os.system('sudo apt install -y redis-server')
    os.system('sudo apt install -y python3 python3-pip python3-venv python3-dev' +
              ' build-essential libxml2-dev libxslt1-dev libffi-dev libpq-dev libssl-dev zlib1g-dev')
    os.system('sudo pip3 install --upgrade pip')
    os.system(
        'sudo wget https://github.com/netbox-community/netbox/archive/v3.0.10.tar.gz')
    os.system('sudo tar -xzf v3.0.10.tar.gz -C /opt')
    os.system('sudo ln -s /opt/netbox-3.0.10/ /opt/netbox')
    os.system('sudo adduser --system --group netbox')
    os.system('sudo chown --recursive netbox /opt/netbox/netbox/media/')
    os.system('cd /opt/netbox/netbox/netbox/')


def main():
   
    redis_Netbox()


if __name__ == "__main__":
    main()
