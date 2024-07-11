import pytest


@pytest.fixture(params=["a","c","b"])
def demo_fixture(request):
    print(request.param)


# @pytest.mark.parametrize("a,b,final", [(2,6,8), (1,3,4), (10,5,15)])
# def testadd(a,b,final):
#     assert a+b ++ final

# def testadditemtocart(demo_fixture):
#     print("Item added successfully")
#
# def testremoveitemtocart(demo_fixture):
#     print("Removed item from cart successfully")