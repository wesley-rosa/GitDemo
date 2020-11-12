import pytest


# @pytest.fixture(scope="class") - Se quiser que execute apenas 1 vez na classe, use dessa forma
#  se quiser que execute pra todos os testes dentro da classe, use da forma abaixo:
@pytest.fixture()
def setup():
    print("I'll execute it firstly")
    yield
    print("Execute last")


@pytest.fixture()
def dataLoad():
    print ("User profile is being created")
    return ["Wesley", "Rosa", "https://rahulshetty.com"]


@pytest.fixture(params=[("chrome", "Wesley"), "firefox", "IE"])
def crossBrowser(request):
    return request.param