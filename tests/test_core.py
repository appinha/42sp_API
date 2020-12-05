def test_hello_data(client):
	response = client.get("/hello")
	assert response.data == b'"Hello, World!"\n'
