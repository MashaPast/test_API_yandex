## GET STARTED FOR ALLURE ON UBUNTU 18

* download .deb package https://launchpad.net/~qameta/+archive/ubuntu/allure/+files/allure_2.4.1~xenial_all.deb
* execute following commands:
```bash
sudo dpkg -i allure_2.4.1_xenial_all.deb
allure --version
pip3 install -Iv allure-pytest==2.7.1

```
* how to use
```bash
pytest --alluredir=./report_dir test_API.py
allure serve /home/krab/PycharmProjects/tests_API_yandex/report_dir/
```

## GET STARTED FOR ALLURE 2.13.2 ON UBUNTU 19
* download allure-commandline-2.13.2.tgz from   https://bintray.com/qameta/maven/allure2/2.13.2#files/io%2Fqameta%2Fallure%2Fallure-commandline%2F2.13.2
* extract to 'programs' folder
* set $PATH in .bashrc
```bash
nano .bashrc
PATH=$PATH:/home/masha/programs/allure-2.13.2/bin
```
## PYTHONPATH FOR EXECUTING MODULES FROM PACKAGES 

```bash
echo $PYTHONPATH 
PYTHONPATH=$PYTHONPATH:$(pwd) pytest websocket_API/ticker/test_ticker_ws.py 
```
## GENERATING HTML REPORT

```bash
pytest --html=report.html
```
## SKIPPING MODULE PYTEST

global variable:
pytestmark = pytest.mark.skipif('2 == 2')

## RUN ORDER OF TESTS
```bash
pip3 install pytest-ordering
```
@pytest.mark.run(order=2)
