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
