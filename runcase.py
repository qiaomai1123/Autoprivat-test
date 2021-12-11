import pytest
import os
if __name__ == '__main__':
    # pytest.main(['-vs','--html=./report.html'])
    # pytest.main(['./testcase/test_antomate.py'])
    pytest.main(['-vs', './testcase/test_post.py'])
    # os.system("allure generate temp -o report --clean")