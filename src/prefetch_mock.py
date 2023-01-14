
from pprint import pprint

def second_query(ids):
    database = [
        {
            "user_id": "1",
            "group_id": "11",
            "group_name": "Y"
        },
        {
            "user_id": "1",
            "group_id": "12",
            "group_name": "X"
        },
        {
            "user_id": "2",
            "group_id": "11",
            "group_name": "Y"        
        },
    ]
    return database

def all_query():
    return [
        {
            "id": "1",
            "name": "Rohan"
        },
        {
            "id": "2",
            "name": "Sajid"
        }
    ]

def map_data(data, prefetch_data):
    
    for i in range(len(data)):
        for p_rec in prefetch_data:
            if data[i]["id"] == p_rec["user_id"]:
                if "groups" in data[i]:
                    data[i]["groups"].append(
                        p_rec
                    )
                else:
                    data[i]["groups"] = [p_rec]
    return data



def main():
    data = all_query()

    ids = [rec["id"] for rec in data]
    prefetch_data = second_query(ids)

    pprint(map_data(data, prefetch_data))

main()







