import pytest
from plant_shop import PlantShop


@pytest.fixture
def plant_shop():
    return PlantShop()


def test_user_init(plant_shop):
    assert plant_shop.get_user_by_name("kloseby0") is not None
    assert plant_shop.get_user_by_name("rpeele1") is not None
    assert plant_shop.get_user_by_name("lmangin2") is not None
    assert plant_shop.get_user_by_name("ssima3") is not None
    with pytest.raises(IndexError):
        plant_shop.get_user_by_id(4)


def test_product_init(plant_shop):
    assert plant_shop.get_product_by_name("Pale Blue-eyed Grass") is not None
    assert plant_shop.get_product_by_name("Sudangrass") is not None
    assert plant_shop.get_product_by_name("Climbing Bedstraw") is not None
    assert plant_shop.get_product_by_name("Pedilanthus") is not None
    assert plant_shop.get_product_by_name("Ames' Lady's Tresses") is not None
    with pytest.raises(IndexError):
        plant_shop.get_user_by_id(5)


def test_order_init(plant_shop):
    o = plant_shop.get_order_by_id(0)
    assert o is not None
    assert o.user_id == 0
    assert o.product_id == 1
    assert o.amount == 3
    assert o.is_paid is True
    with pytest.raises(IndexError):
        plant_shop.get_order_by_id(1)
