import requests

def test_items_page_empty():
    url = "http://127.0.0.1:5000/items"
    response = requests.get(url)
    assert response.status_code == 200, "Failed: Items page did not return status code 200"
    assert "No items found" in response.text, "Failed: 'No items found' message not displayed for empty list"

if __name__ == "__main__":
    test_items_page_empty()
    print("Test passed.")