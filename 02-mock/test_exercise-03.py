import pytest
from plant_shop import PlantShop
from unittest.mock import Mock, patch

_users = [
    {
        "username": "kloseby0",
        "first_name": "Kleon",
        "last_name": "Loseby",
        "email": "kloseby0@exblog.jp",
    },
    {
        "username": "rpeele1",
        "first_name": "Ruthanne",
        "last_name": "Peele",
        "email": "rpeele1@alexa.com",
    },
    {
        "username": "lmangin2",
        "first_name": "Lamar",
        "last_name": "Mangin",
        "email": "lmangin2@msu.edu",
    },
    {
        "username": "ssima3",
        "first_name": "Spenser",
        "last_name": "Sima",
        "email": "ssima3@tripadvisor.com",
    },
]

_products = [
    {
        "name": "Pale Blue-eyed Grass",
        "sku": "ac5a71e7c937649ad36939049aa066e0",
        "in_storage": 10,
        "ordered": 6,
    },
    {
        "name": "Sudangrass",
        "sku": "452f463364ea8d35451a98dab8f4f289",
        "in_storage": 15,
        "ordered": 3,
    },
    {
        "name": "Climbing Bedstraw",
        "sku": "81a0396fa72e05bd8fc1c781d23519b8",
        "in_storage": 7,
        "ordered": 2,
    },
    {
        "name": "Pedilanthus",
        "sku": "57e34d3ba073dbcdf8f79ac8667e1637",
        "in_storage": 9,
        "ordered": 0,
    },
    {
        "name": "Ames' Lady's Tresses",
        "sku": "d835f3da395823d1b4cb606489d1a2ec",
        "in_storage": 7,
        "ordered": 0,
    },
]
_orders = [{"user_id": 0, "product_id": 1, "amount": 3, "paid": True}]


@pytest.fixture
def plant_shop_obj(create_database_mock):
    return PlantShop(create_database_mock)


@pytest.fixture()
def create_database_mock():
    with patch("db.DB") as patch_database:
        patch_database.list_tables.return_value = {"users": _users, "products": _products, "orders": _orders}
        patch_database.get_table.return_value = [{
            "username": "kloseby0",
            "first_name": "Kleon",
            "last_name": "Loseby",
            "email": "kloseby0@exblog.jp"
        }]


def test_user(plant_shop_obj):
    assert plant_shop_obj.get_user_by_name("kloseby0") is not None

# def test_user_init(plant_shop):
#     assert plant_shop.get_user_by_name("kloseby0") is not None
#     assert plant_shop.get_user_by_name("rpeele1") is not None
#     assert plant_shop.get_user_by_name("lmangin2") is not None
#     assert plant_shop.get_user_by_name("ssima3") is not None
#     with pytest.raises(IndexError):
#         plant_shop.get_user_by_id(4)
#
#
# def test_product_init(plant_shop):
#     assert plant_shop.get_product_by_name("Pale Blue-eyed Grass") is not None
#     assert plant_shop.get_product_by_name("Sudangrass") is not None
#     assert plant_shop.get_product_by_name("Climbing Bedstraw") is not None
#     assert plant_shop.get_product_by_name("Pedilanthus") is not None
#     assert plant_shop.get_product_by_name("Ames' Lady's Tresses") is not None
#     with pytest.raises(IndexError):
#         plant_shop.get_user_by_id(5)
#
#
# def test_order_init(plant_shop):
#     o = plant_shop.get_order_by_id(0)
#     assert o is not None
#     assert o.user_id == 0
#     assert o.product_id == 1
#     assert o.amount == 3
#     assert o.is_paid is True
#     with pytest.raises(IndexError):
#         plant_shop.get_order_by_id(1)
