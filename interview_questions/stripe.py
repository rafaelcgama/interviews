### Stripe ###

def combine(mylist):
    mydict = {}
    for lan in mylist:
        key = lan
        mydict[lan] = [lan]
        if len(lan) == 5:
            key = lan[:2]
        mydict[key] = mydict.get(key, list()) + [lan]

    return mydict


def is_accepted_simple(client, server):
    myclient = [lan.strip() for lan in client.split(",")]
    return set(myclient).intersection(set(server))


def is_accepted(client, server):
    accepted_langs = []
    dict_server = combine(server)
    for client_lan in client.split(","):
        cleaned_client_lan = client_lan.strip()
        server_langs = dict_server.get(cleaned_client_lan, None)
        if server_langs:
            accepted_langs += list(set(server_langs) - set(accepted_langs))

    return accepted_langs

if __name__ == '__main__':
    client = "fr-FR, fr"
    server = ["en-US", "fr-FR", "fr-CA"]
