import pytest

class Testapi():
    @pytest.mark.parametrize('args', ['ss', '33'])
    def test_args1(self, args):
        print(args)

    @pytest.mark.parametrize('args2,sum', [['ss', 33],['ee', 22]])
    def test_args21(self, args2,sum):
        print(args2,sum)

if __name__=='__main__':
    pytest.main(['-vs', 'testapi.py'])