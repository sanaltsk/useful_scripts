# Create tunnel to mongo in remote machine and do CRUD operations on Mongodb

# adding comment
from sshtunnel import SSHTunnelForwarder
import pymongo

def create_tunnel_and_mongo_operation(args):
    with SSHTunnelForwarder(
            (args.ip, args.port),   # 192.168.1.1 , 8080
            ssh_username="<vm_username>",
            ssh_password="<vm_password>",
            remote_bind_address=('127.0.0.1', 27017)
    ) as tunnel:
        client = pymongo.MongoClient('127.0.0.1', tunnel.local_bind_port)
        db = client["<db_name>"]
        db.authenticate('<dbusername>', "<dbpassword>")
        db["notes"].delete_one({'id': "123"})
    print("DB Operation complete")
