## GET STARTED FOR ALLURE ON UBUNTU 18

* download .deb package 
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

```bash
pytestmark = pytest.mark.skipif('2 == 2')
```
