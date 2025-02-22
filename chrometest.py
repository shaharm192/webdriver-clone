# setting up chrome browser on a desired page
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()


sleep(3)
# # opening chrome browser on a desired page
driver.get("https://www.google.com")
sleep(3)
# # # Getting browser current page URL
print("url: " + driver.current_url)
# sleep(5)
driver.refresh()
sleep(2)
# driver.close()
# # Getting browser current page title
print("title: "+driver.title)
# # Getting browser current tab handle
# print("handle: "+driver.current_window_handle)
# # Getting browser first tab handle
print("handles: "+driver.window_handles[2])
# # Getting current page source
print("source: "+driver.page_source)



# # Tip calc orig
# from selenium import webdriver
# from time import sleep
# try:
#     dr = webdriver.Chrome()
#     dr.get("file:////Users/roymoshin/Downloads/tip_calc/index.html")
#     sleep(2)
#     dr.find_element(by="id",value="billamt").send_keys("5")
#     dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[5]").click()
#     sleep(2)
#     dr.find_element(by="id",value="peopleamt").send_keys("2")
#     sleep(2)
#     # dr.find_element(by="id",value="music").send_keys("2")
#     # sleep(2)
#     dr.find_element(by="id",value="calculate").click()
#     sleep(2)
#     actual = dr.find_element(by="id",value="tip").text
#     excpected = "0.25"
#     print(f"The actual: {actual} , The excpected: {excpected}")
#
#     assert actual == excpected
# except AssertionError as e:
#     print("The actual tip is different than excpected",e)







# sleep(5)
# billamt = dr.find_element(by="id", value="billamt")
# billamt.send_keys("100")
#
# dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[3]").click()
# dr.find_element(by="id", value="peopleamt").send_keys("5")
# dr.find_element(by="id", value="calculate").click()
# actual = dr.find_element(by="id", value="tip").text
# expected = "4.00"
# print(actual)
# assert expected == actual
# sleep(10)


# import requests
# from requests.exceptions import InvalidURL
# from time import sleep
#
# try:
#     response = requests.get("https://google.com")
#     print(response)
#     print(response.status_code)
#
# except InvalidURL:
#     print("invalid url was given")



# from flask import Flask
#
# app = Flask("devops")
#
# @app.route('/devops')
# def my_func():
#     return "hello and welcome to the world of games"
#
# app.run(host="0.0.0.0", port=5001, debug=True)


# from flask import Flask, jsonify, request
# app = Flask("moshe")
# data = [
#     {"id": 1, "name": "Item 1"},
#     {"id": 2, "name": "Item 2"},
#     {"id": 3, "name": "Item 3"},
# ]
# @app.route('/items', methods=['GET'])
# def get_items():
#     return jsonify(data)
#
# @app.route('/items/<int:item_id>', methods=['GET'])
# def get_item(item_id):
#     for item in data:
#         if item['id'] == item_id:
#             return jsonify(item)
#     return jsonify({"error": "Item not found"}), 404
#
#
#
# @app.route('/items/<int:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     # modifying the data list, so you need to declare data as global to indicate that you're modifying the global variable.
#     global data
#     new_data = []
#     for item in data:
#         if item['id'] != item_id:
#             new_data.append(item)
#     data = new_data
#     return jsonify({"message": "Item deleted successfully"})
#
#
# app.run(host='127.0.0.1', port="8080")