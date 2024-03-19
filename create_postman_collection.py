import json


clothes_size = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']  # данные, которые будут использованы в запросах

items = []  # список, в который будут сохранены сгенерированные запросы
for size in clothes_size:
    item = {  # item – описание запроса Postman
        "name": f"Size {size}",
        "protocolProfileBehavior": {
            "disableBodyPruning": True
        },
        "request": {
            "method": "GET",
            "header": [],
            "body": {
                "mode": "raw",
                "raw": "",
                "options": {
                    "raw": {
                        "language": "json"
                    }
                }
            },
            "url": {
                "raw": f"https://ir-example.mir.prod.reco.microsoft.com/Reco/V1.0/Popular?modeling=adw&Count=5&Category=Clothing&Size={size}",
                "protocol": "https",
                "host": [
                    "ir-example",
                    "mir",
                    "prod",
                    "reco",
                    "microsoft",
                    "com"
                ],
                "path": [
                    "Reco",
                    "V1.0",
                    "Popular"
                ],
                "query": [
                    {
                        "key": "modeling",
                        "value": "adw"
                    },
                    {
                        "key": "Count",
                        "value": "5"
                    },
                    {
                        "key": "Category",
                        "value": "Clothing"
                    },
                    {
                        "key": "Size",
                        "value": f"{size}"
                    }
                ]
            }
        },
        "response": []
    }
    items.append(item)

postman_collection = {
    "info": {
        "_postman_id": "f1ad7686-7f54-44ee-a20b-534bb1f028e0",
        "name": "Test Example",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
        "_exporter_id": "15037634"
    },
    "item": items
}

with open('postman_collection.json', 'w') as f:
    json.dump(postman_collection, f)
