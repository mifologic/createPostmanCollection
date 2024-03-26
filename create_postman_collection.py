import json

product_categories = ["electronics", "jewelery", "men's clothing", "women's clothing"]  # данные, которые будут использованы в запросах

items = []  # список, в который будут сохранены сгенерированные запросы
for category in product_categories:
    item = {  # item – описание запроса Postman
        "name": f"Category {category}",
        "event": [
            {
                "listen": "test",
                "script": {
                    "exec": [
                        "pm.test(\"Status code is 200\", function () {",
                        "    pm.response.to.have.status(200);",
                        "});"
                    ],
                    "type": "text/javascript",
                    "packages": {}
                }
            }
        ],
        "request": {
            "method": "GET",
            "header": [],
            "url": {
                "raw": f"https://fakestoreapi.com/products/category/{category}",
                "protocol": "https",
                "host": [
                    "fakestoreapi",
                    "com"
                ],
                "path": [
                    "products",
                    "category",
                    f"{category}"
                ]
            }
        },
        "response": []
    }
    items.append(item)

postman_collection = {
    "info": {
        "_postman_id": "f1ad7686-7f54-44ee-a20b-534bb1f028e0",
        "name": "Generated Collection",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
        "_exporter_id": "15037634"
    },
    "item": items
}

with open('generated_collection.postman_collection.json', 'w') as f:
    json.dump(postman_collection, f)
